import re
from pathlib import Path
from typing import Dict, Any
from sqlalchemy.orm import Session

from app.models.lumina import LuminaDeliverable, LuminaTask


class LuminaService:
    def __init__(self, content_root: str):
        self.content_root = Path(content_root)
        self.lumina_root = self.content_root / "Lumina_Tech"

    def sync_structure(self, db: Session):
        """
        Scans content directory and populates DB if missing.
        Acts as a 'Seeder'.
        """
        if not self.lumina_root.exists():
            return

        target_dir = self.lumina_root / "Gestor_de_Versiones"
        if not target_dir.exists():
            return

        # 1. Exclusions (Future Sprints / Read Only)
        excluded_prefixes = ["08", "09", "10", "REF"]

        # 2. Weights Logic
        # Core Deliverables (High Impact)
        core_files = ["01", "02", "03", "04"]
        # Support Deliverables (Medium Impact)
        support_files = ["14", "11", "12", "13"]

        for file_path in target_dir.glob("*.md"):
            # Check Exclusions
            if any(file_path.name.startswith(p) for p in excluded_prefixes):
                continue

            rel_path = f"Lumina_Tech/Gestor_de_Versiones/{file_path.name}"

            # Check if exists
            deliverable = db.query(LuminaDeliverable).filter_by(path=rel_path).first()

            if not deliverable:
                role_name = file_path.stem.replace("_", " ").title()

                # Assign Weight
                weight = 0  # Default (Info)

                prefix = file_path.name[:2]
                if prefix in core_files:
                    weight = 30
                elif prefix in support_files:
                    weight = 10

                deliverable = LuminaDeliverable(
                    title=role_name, path=rel_path, role=role_name, weight=weight
                )
                db.add(deliverable)
                db.commit()
                db.refresh(deliverable)

                # Parse and Create Tasks
                self._parse_and_create_tasks(db, deliverable, file_path)
            else:
                # Update existing if needed (Weights might have changed)
                # Calculate expected weight
                role_name = file_path.stem.replace("_", " ").title()
                expected_weight = 0
                prefix = file_path.name[:2]
                if prefix in core_files:
                    expected_weight = 30
                elif prefix in support_files:
                    expected_weight = 10

                if deliverable.weight != expected_weight:
                    deliverable.weight = expected_weight
                    db.commit()

    def _parse_and_create_tasks(
        self, db: Session, deliverable: LuminaDeliverable, file_path: Path
    ):
        try:
            content = file_path.read_text(encoding="utf-8")
            pattern = re.compile(r"- \[([ xX])\] (.*)")
            matches = pattern.findall(content)

            if matches:
                # If tasks found, sync them
                for status_char, description in matches:
                    is_completed = status_char.lower() == "x"
                    task = LuminaTask(
                        deliverable_id=deliverable.id,
                        description=description.strip(),
                        is_completed=is_completed,
                    )
                    db.add(task)
                db.commit()

            # 3. Smart Injection (Auto-Content)
            # If NO tasks found and it is a CORE/SUPPORT file, inject default checklist
            elif deliverable.weight > 0:
                self._inject_default_checklist(db, deliverable, file_path)

        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    def _inject_default_checklist(
        self, db: Session, deliverable: LuminaDeliverable, file_path: Path
    ):
        """
        Appends a standard validation checklist to the MD file and adds to DB.
        """
        checklist_content = "\n\n---\n\n## ✅ Checklist de Validación (Estándar)\n"
        tasks = [
            "Lectura y comprensión del documento",
            "Validación de requerimientos con el equipo",
            "Implementación preliminar en Sandbox",
            "Revisión de pares (Peer Review)",
        ]

        # Write to File
        try:
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(checklist_content)
                for t in tasks:
                    f.write(f"- [ ] {t}\n")

            # Write to DB
            for t in tasks:
                task = LuminaTask(
                    deliverable_id=deliverable.id, description=t, is_completed=False
                )
                db.add(task)
            db.commit()

        except Exception as e:
            print(f"Error injecting content: {e}")

    def get_stats(self, db: Session) -> Dict[str, Any]:
        """
        Calculate weighted progress metrics from DB.
        """
        # Ensure sync
        self.sync_structure(db)

        deliverables = db.query(LuminaDeliverable).all()

        stats = {
            "global": {"percent": 0},
            "roles": {},  # We'll group by Role Category or Filename for now
            "deliverables": [],
        }

        total_weight = 0
        earned_weight = 0

        for d in deliverables:
            # Skip if weight is 0 (Info files) from Global calculation?
            # Or keep them but they add 0.

            tasks = d.tasks
            total_tasks = len(tasks)
            completed_tasks = sum(1 for t in tasks if t.is_completed)

            pct = 0
            if total_tasks > 0:
                pct = int((completed_tasks / total_tasks) * 100)

            # Weighted Calc
            total_weight += d.weight
            earned_weight += (pct / 100) * d.weight

            # Simplified Role Aggregation
            stats["roles"][d.role] = {
                "total": total_tasks,
                "completed": completed_tasks,
                "percent": pct,
                "weight": d.weight,
            }

            stats["deliverables"].append(
                {
                    "id": d.id,
                    "title": d.title,
                    "path": d.path,
                    "percent": pct,
                    "weight": d.weight,  # For UI
                    "tasks": [
                        {"id": t.id, "desc": t.description, "done": t.is_completed}
                        for t in tasks
                    ],
                }
            )

        if total_weight > 0:
            stats["global"]["percent"] = int((earned_weight / total_weight) * 100)

        return stats

    def toggle_task(self, db: Session, task_id: int) -> Dict[str, Any]:
        """
        Toggles task and returns updated stats for immediate UI reactivity.
        """
        task = db.query(LuminaTask).get(task_id)
        if task:
            task.is_completed = not task.is_completed
            db.commit()

            # Recalculate Deliverable Percent
            # We could optimize this, but for MVP re-querying is fine
            d = task.deliverable
            all_tasks = d.tasks
            d_pct = int(
                (sum(1 for t in all_tasks if t.is_completed) / len(all_tasks)) * 100
            )

            # Recalculate Global (Quick Estimate or Full?)
            # Let's do a full recalc to be safe
            full_stats = self.get_stats(db)

            return {
                "is_completed": task.is_completed,
                "deliverable_percent": d_pct,
                "deliverable_id": d.id,
                "global_percent": full_stats["global"]["percent"],
            }

        return {}
