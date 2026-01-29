import sys
import os
from datetime import datetime, timedelta

# Add parent directory to path to import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.sprint import Sprint
from app.models.task import Task
from app.models.user import User
from app.utils.security import hash_password
from sqlalchemy import text


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
            # Ignore if column already exists
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

        # 1b. Create Wilmer User (Owner)
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
            },  # Added missing task
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
                # Use explicit days_offset if available, else fallback to week calculation (though all have offset now)
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

        # 5. SEED LUMINA DASHBOARD DATA (Restoring previous content)
        print("Seeding Lumina Dashboard Data...")
        from app.models.lumina import (
            LuminaDeliverable,
            LuminaTask,
        )  # Local import to avoid circular issues

        lumina_days = [
            {
                "title": "📅 DÍA 1: Análisis y Conocimiento",
                "reference": "Referencia: Práctica Clase 7",
                "tasks": [
                    "Leer juntos y conocer la Empresa.",
                    "Definir Roles.",
                    "Generar preguntas en el documento para evacuar dudas.",
                    "Registrar en el Doc: gestor de versiones.",
                ],
            },
            {
                "title": "🏗️ DÍA 2: HU-Modelo de Datos",
                "reference": "Referencia: Práctica Clase 8",
                "tasks": [
                    "Creación de objetos Custom - Standard.",
                    "Relación entre Objetos.",
                    "Campos personalizados.",
                    "Registrar en el Doc: gestor de versiones.",
                    "Crear las HU en TRELLO.",
                ],
            },
            {
                "title": "🎨 DÍA 3: HU - Creación de la APP",
                "reference": "Referencia: Práctica Clase 9",
                "tasks": [
                    "Tener en cuenta el diseño.",
                    "Lograr hacer el dominio personalizado.",
                    "Agregar el Logo y colores.",
                ],
            },
            {
                "title": "🧪 DÍA 4: HU - Creación de los Formularios",
                "reference": "Referencia: Práctica Clase 10",
                "tasks": [
                    "Campos adicionales.",
                    "Reglas de validación y campos formula.",
                    "Registrar en el Doc: gestor de versiones.",
                    "Crear las HU en TRELLO.",
                ],
            },
        ]

        for day_data in lumina_days:
            # Check if day exists by reference
            day = (
                db.query(LuminaDeliverable)
                .filter(LuminaDeliverable.reference == day_data["reference"])
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

                # Add tasks
                for task_desc in day_data["tasks"]:
                    task = LuminaTask(
                        deliverable_id=day.id, description=task_desc, is_completed=False
                    )
                    db.add(task)
                db.commit()
            else:
                print(f"Day exists: {day_data['title']}")

        print("Seeding completed successfully!")

    except Exception as e:
        print(f"Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
