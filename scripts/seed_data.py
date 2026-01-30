import sys
import os
import re
from datetime import datetime, timedelta

# Add parent directory to path to import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.sprint import Sprint
from app.models.task import Task
from app.models.user import User
from app.utils.security import hash_password
from sqlalchemy import text


def parse_lumina_checklist():
    """
    Parses content/Lumina_Tech/Archivos_intermedios/Checklist_por_dia.md
    to extract Days, Tasks, and File Links.
    """
    file_path = os.path.join(
        "content", "Lumina_Tech", "Archivos_intermedios", "Checklist_por_dia.md"
    )

    if not os.path.exists(file_path):
        print(f"Warning: Checklist file not found at {file_path}")
        return []

    days = []
    current_day = None

    # Regex patterns
    day_pattern = re.compile(r"^##\s+📅\s+(Día\s+\d+:.+)")
    task_pattern = re.compile(r"^\d+\.\s+\*\*(.+?)\*\*")
    link_pattern = re.compile(r"\[Ver Tarea\]\((dia_\d+/[^)]+)\)")
    source_pattern = re.compile(r"\*\*Fuente\*\*:\s+\[.+\]\((.+)\)")

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # Match Day Header
            day_match = day_pattern.match(line)
            if day_match:
                if current_day:
                    days.append(current_day)

                day_title = day_match.group(1)  # e.g. "Día 0: Análisis..."
                # Extract simple day "Día X" for reference
                ref_part = day_title.split(":")[0]
                current_day = {
                    "title": f"📅 {day_title}",
                    "reference": f"Log: {ref_part}",
                    "source_link": None, # Init source link
                    "tasks": [],
                }
                continue

            # Match Source Link (Usually right after day header)
            source_match = source_pattern.search(line)
            if source_match and current_day:
                 raw_path = source_match.group(1)
                 # Clean up path (remove ../../)
                 clean_path = raw_path.replace("../../", "").replace("../", "")
                 current_day["source_link"] = clean_path
                 continue
            
            # Match Task Title
            task_match = task_pattern.match(line)
            if task_match and current_day:
                title = task_match.group(1).rstrip(".")  # Remove trailing dot
                current_day["tasks"].append({"desc": title, "path": None})
                continue

            # Match Link
            link_match = link_pattern.search(line)
            if link_match and current_day and current_day["tasks"]:
                # Attach link to the last task
                rel_path = link_match.group(1)
                full_path = f"Lumina_Tech/{rel_path}"
                current_day["tasks"][-1]["path"] = full_path

    if current_day:
        days.append(current_day)

    return days


def seed_data():
    db = SessionLocal()

    try:
        # ... (omitted) ...

        # 5. SEED LUMINA DASHBOARD DATA (Backend Native Mode)
        print("Seeding Lumina Dashboard Data (Backend Native)...")
        from app.models.lumina import (
            LuminaDeliverable,
            LuminaTask,
        )

        # CLEANUP: Remove duplicates by wiping Lumina data first
        print("  - Cleaning up old Lumina data...")
        db.query(LuminaTask).delete()
        db.query(LuminaDeliverable).delete()
        db.commit()

        lumina_days = parse_lumina_checklist()

        if not lumina_days:
            # Fallback for resiliency
            print("Warning: No data parsed from checklist. Running basic seed.")

        for day_data in lumina_days:
            # Check if day exists (it shouldn't after cleanup, but good practice)
            day = (
                db.query(LuminaDeliverable)
                .filter(LuminaDeliverable.title == day_data["title"])
                .first()
            )

            if not day:
                print(f"Creating Day: {day_data['title']}")
                day = LuminaDeliverable(
                    title=day_data["title"],
                    reference=day_data["reference"],
                    source_link=day_data.get("source_link"), # Add source link
                )
                db.add(day)
                db.commit()
                db.refresh(day)

            for task_info in day_data["tasks"]:
                description = task_info["desc"]
                doc_path = task_info["path"]

                # FILTER: Skip administrative/Trello tasks
                if description.startswith("Mover a"):
                    continue

                print(f"  + Task: {description}")
                task = LuminaTask(
                    deliverable_id=day.id,
                    description=description,
                    doc_path=doc_path,
                    is_completed=False,
                )
                db.add(task)

            db.commit()

        print("Seeding completed successfully!")

    except Exception as e:
        print(f"Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
