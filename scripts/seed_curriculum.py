"""
Curriculum Seed Script - Universal Sprint/Task Seeder

Uses parse_schedule.py to read schedules/sprintN_schedule.md files
and populate the database with Sprint and Task data.

Author: AI Agent (Gemini)
Date: 2026-02-02
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database import SessionLocal
from app.models.sprint import Sprint
from app.models.task import Task
from scripts.parse_schedule import parse_schedule_file


def seed_curriculum(schedule_files: list[str], clear_existing: bool = False):
    """
    Seed curriculum data from schedule files

    Args:
        schedule_files: List of paths to schedule markdown files
        clear_existing: If True, clear existing Sprint/Task data before seeding
    """
    db = SessionLocal()

    try:
        print("\n" + "=" * 80)
        print("🌱 SEEDING CURRICULUM DATA")
        print("=" * 80 + "\n")

        # Clear existing data if requested
        if clear_existing:
            print("🧹 Clearing existing curriculum data...")
            deleted_tasks = db.query(Task).delete()
            deleted_sprints = db.query(Sprint).delete()
            db.commit()
            print(
                f"   ✅ Deleted {deleted_tasks} tasks and {deleted_sprints} sprints\n"
            )

        # Process each schedule file
        for schedule_path in schedule_files:
            print(f"📄 Processing: {schedule_path}")

            # Parse schedule file
            try:
                sprint_data = parse_schedule_file(schedule_path)
            except FileNotFoundError:
                print(f"   ⚠️  File not found: {schedule_path}")
                continue
            except Exception as e:
                print(f"   ❌ Error parsing file: {e}")
                continue

            # Check if sprint already exists
            existing_sprint = (
                db.query(Sprint).filter(Sprint.number == sprint_data["number"]).first()
            )

            if existing_sprint:
                print(
                    f"   ⚠️  Sprint {sprint_data['number']} already exists, skipping..."
                )
                continue

            # Create Sprint
            print(f"   📊 Creating Sprint {sprint_data['number']}...")
            sprint = Sprint(
                number=sprint_data["number"],
                name=sprint_data["name"],
                description=sprint_data["description"] or "Sprint curriculum",
                start_date=sprint_data["start_date"],
                end_date=sprint_data["end_date"],
                is_active=True,
            )
            db.add(sprint)
            db.commit()
            db.refresh(sprint)
            print(
                f"   ✅ Sprint {sprint.number} created (ID: {sprint.id}, {sprint.start_date} - {sprint.end_date})"
            )

            # Create Tasks
            print(f"   📝 Creating {len(sprint_data['tasks'])} tasks...")
            tasks_created = 0

            for task_data in sprint_data["tasks"]:
                # Check if task already exists
                existing_task = (
                    db.query(Task)
                    .filter(
                        Task.title == task_data["title"], Task.sprint_id == sprint.id
                    )
                    .first()
                )

                if existing_task:
                    print(f"      ⚠️  Task '{task_data['title']}' already exists")
                    continue

                # Create task
                task = Task(
                    title=task_data["title"],
                    category=task_data["category"],
                    markdown_path=task_data["markdown_path"],
                    sprint_id=sprint.id,
                    due_date=task_data["due_date"],
                    description=f"Semana {task_data['week']} - {task_data['category']}",
                )
                db.add(task)
                tasks_created += 1

                print(
                    f"      ✅ {task_data['title']} ({task_data['category']}, Due: {task_data['due_date'].strftime('%Y-%m-%d')})"
                )

            db.commit()
            print(f"   ✅ {tasks_created} tasks created for Sprint {sprint.number}\n")

        print("=" * 80)
        print("✅ CURRICULUM SEEDING COMPLETED")
        print("=" * 80 + "\n")

        # Summary
        total_sprints = db.query(Sprint).count()
        total_tasks = db.query(Task).count()
        print("📊 Database Summary:")
        print(f"   - Sprints: {total_sprints}")
        print(f"   - Tasks: {total_tasks}")
        print()

    except Exception as e:
        print(f"\n❌ Error seeding curriculum: {e}")
        db.rollback()
        raise
    finally:
        db.close()


def main():
    """Main entry point"""
    # List of schedule files to process
    schedule_files = [
        "schedules/sprint1_schedule.md",
        "schedules/sprint2_schedule.md",
        "schedules/sprint3_schedule.md",
        "schedules/sprint4_schedule.md",
    ]

    # Seed curriculum (clear existing data)
    seed_curriculum(schedule_files, clear_existing=True)


if __name__ == "__main__":
    main()
