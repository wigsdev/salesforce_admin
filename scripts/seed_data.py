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
                    "tasks": [],
                }
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
        # 0. QUICK MIGRATION CHECK (Bypass Alembic issues)
        try:
            db.execute(text("ALTER TABLE tasks ADD COLUMN due_date TIMESTAMP"))
            db.commit()
            print("Migration: Added due_date column to tasks table.")
        except Exception:
            db.rollback()
            pass

        # 1. Create Default Users if not exist
        if not db.query(User).filter(User.email == "admin@admin.com").first():
            admin = User(
                email="admin@admin.com",
                name="Admin User",
                password_hash=hash_password("admin123"),
                role="admin",
                team="Staff",
            )
            db.add(admin)

        if not db.query(User).filter(User.email == "student@test.com").first():
            print("Creating student user...")
            student = User(
                email="student@test.com",
                name="Student Test",
                password_hash=hash_password("student123"),
                role="student",
                team="Admin Force",
            )
            db.add(student)

        if not db.query(User).filter(User.email == "karlwgs1989@gmail.com").first():
            print("Creating Wilmer's user...")
            wilmer = User(
                email="karlwgs1989@gmail.com",
                name="Wilmer G",
                password_hash=hash_password("admin123"),
                role="admin",
                team="Visionary Admins",
            )
            db.add(wilmer)

        db.commit()

        # 2. Get or Create Sprint 1
        sprint1 = db.query(Sprint).filter(Sprint.number == 1).first()
        if not sprint1:
            print("Creating Sprint 1...")
            sprint1 = Sprint(
                name="Fundamentos y Modelado de Datos",
                description="Introducción a Salesforce, configuración de org, seguridad y reportes.",
                number=1,
                start_date=datetime(2026, 1, 5),
                end_date=datetime(2026, 2, 6),
            )
            db.add(sprint1)
            db.commit()
            db.refresh(sprint1)
        else:
            print("Sprint 1 already exists. Skipping creation.")

        # 4. Create Tasks for Sprint 1
        print("Seeding Tasks...")

        tasks_data = [
            # Semana 1 (Deadline: Friday Jan 9 -> +4 days)
            {
                "title": "Fundamentos básicos de SF",
                "category": "Teoria",
                "path": "curriculum/sprint1/clase1.md",
                "week": 1,
                "days_offset": 4,
            },
            {
                "title": "Rol Administrador",
                "category": "Practica",
                "path": "curriculum/sprint1/practica1.md",
                "week": 1,
                "days_offset": 4,
            },
            {
                "title": "Modelado de Datos I",
                "category": "Teoria",
                "path": "curriculum/sprint1/clase2.md",
                "week": 1,
                "days_offset": 4,
            },
            {
                "title": "Modelado de Datos II",
                "category": "Teoria",
                "path": "curriculum/sprint1/clase3.md",
                "week": 1,
                "days_offset": 4,
            },
            # SB Object -> Deadline Jan 16 (+11 days)
            {
                "title": "SB - Object and Relationship",
                "category": "Superbadge",
                "path": "Superbadges/Object_Relationship.md",
                "week": 1,
                "days_offset": 11,
            },
            # Semana 2 (Deadline: Friday Jan 16 -> +11 days)
            {
                "title": "Gestión de Usuarios",
                "category": "Teoria",
                "path": "curriculum/sprint1/clase4.md",
                "week": 2,
                "days_offset": 11,
            },
            {
                "title": "Fórmulas y Validaciones",
                "category": "Teoria",
                "path": "curriculum/sprint1/clase5.md",
                "week": 2,
                "days_offset": 11,
            },
            {
                "title": "Calidad de datos y jerarquía",
                "category": "Teoria",
                "path": "curriculum/sprint1/clase6.md",
                "week": 2,
                "days_offset": 11,
            },
            # SB General -> Deadline Jan 23 (+18 days)
            {
                "title": "Superbadge (General)",
                "category": "Superbadge",
                "path": "Superbadges/General.md",
                "week": 2,
                "days_offset": 18,
            },
            # Semana 3 (Deadline: Friday Jan 23 -> +18 days)
            {
                "title": "Seguridad I",
                "category": "Teoria",
                "path": "curriculum/sprint1/clase7.md",
                "week": 3,
                "days_offset": 18,
            },
            {
                "title": "Seguridad II",
                "category": "Teoria",
                "path": "curriculum/sprint1/clase8.md",
                "week": 3,
                "days_offset": 18,
            },
            {
                "title": "Seguridad III",
                "category": "Teoria",
                "path": "curriculum/sprint1/clase9.md",
                "week": 3,
                "days_offset": 18,
            },
            # SB Seguridad -> Deadline Jan 30 (+25 days)
            {
                "title": "SB - Seguridad",
                "category": "Superbadge",
                "path": "Superbadges/Security.md",
                "week": 3,
                "days_offset": 25,
            },
            # Semana 4 (Deadline: Friday Jan 30 -> +25 days)
            {
                "title": "Reportes y Tableros",
                "category": "Teoria",
                "path": "curriculum/sprint1/clase10.md",
                "week": 4,
                "days_offset": 25,
            },
            {
                "title": "Gestor de Datos",
                "category": "Teoria",
                "path": "curriculum/sprint1/clase11.md",
                "week": 4,
                "days_offset": 25,
            },
            {
                "title": "Service Cloud Basics",
                "category": "Teoria",
                "path": "curriculum/sprint1/clase12.md",
                "week": 4,
                "days_offset": 25,
            },
            # Final Deadline: Friday Feb 6 -> +32 days
            {
                "title": "SB - Seguridad o Data Import",
                "category": "Superbadge",
                "path": "Superbadges/Data_Import.md",
                "week": 4,
                "days_offset": 32,
            },
        ]

        for task_info in tasks_data:
            exists = (
                db.query(Task)
                .filter(Task.title == task_info["title"], Task.sprint_id == sprint1.id)
                .first()
            )
            if not exists:
                days = task_info.get("days_offset", task_info["week"] * 7)
                due_date = sprint1.start_date + timedelta(days=days)

                print(f"Adding task: {task_info['title']} (Due: {due_date})")
                task = Task(
                    title=task_info["title"],
                    category=task_info["category"],
                    markdown_path=task_info["path"],
                    sprint_id=sprint1.id,
                    due_date=due_date,
                )
                db.add(task)

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
