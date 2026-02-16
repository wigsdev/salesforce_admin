"""
Curriculum Seed Script - Universal Sprint/Task Seeder (Smart Sync)

Uses parse_schedule.py to read schedules/sprintN_schedule.md files
and synchronize the database with Sprint and Task data.

Implements "Smart Sync" (Upsert) strategy:
- Detects existing records
- Updates metadata (Title, Description, Dates) without changing IDs
- Preserves User Progress linked to Task IDs
- ONLY inserts new records

Author: AI Agent (Gemini)
Date: 2026-02-15
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
    Seed curriculum data from schedule files using Smart Sync (Upsert)

    Args:
        schedule_files: List of paths to schedule markdown files
        clear_existing: DEPRECATED - Kept for signature compatibility but ignored for safety.
                        We strictly use Smart Sync to avoid data loss.
    """
    db = SessionLocal()

    try:
        print("\n" + "=" * 80)
        print("🌱 SEEDING CURRICULUM DATA (SMART SYNC MODE)")
        print("=" * 80 + "\n")

        if clear_existing:
            print("⚠️  WARNING: 'clear_existing' flag ignored to protect User Progress.")
            print("   Using Smart Sync (Upsert) instead of Delete-All.\n")

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

            # --- SPRINT SYNC ---
            # Check if sprint already exists by Number
            sprint = (
                db.query(Sprint).filter(Sprint.number == sprint_data["number"]).first()
            )

            if sprint:
                # Update existing Sprint
                print(f"   🔄 Updating Sprint {sprint.number}...")
                sprint.name = sprint_data["name"]
                sprint.description = sprint_data["description"] or "Sprint curriculum"
                sprint.start_date = sprint_data["start_date"]
                sprint.end_date = sprint_data["end_date"]
                # Keep existing ID and is_active status
            else:
                # Create new Sprint
                print(f"   ✨ Creating Sprint {sprint_data['number']}...")
                sprint = Sprint(
                    number=sprint_data["number"],
                    name=sprint_data["name"],
                    description=sprint_data["description"] or "Sprint curriculum",
                    start_date=sprint_data["start_date"],
                    end_date=sprint_data["end_date"],
                    is_active=True,
                )
                db.add(sprint)

            # Commit Sprint changes to get ID for Tasks
            db.commit()
            db.refresh(sprint)

            # --- TASKS SYNC ---
            print(f"   📝 Syncing {len(sprint_data['tasks'])} tasks...")
            tasks_synced = 0
            tasks_created = 0
            tasks_updated = 0

            for task_data in sprint_data["tasks"]:
                # Check if task already exists by Markdown Path (Unique Key)
                # We use markdown_path as key because titles can change slightly
                existing_task = (
                    db.query(Task)
                    .filter(Task.markdown_path == task_data["markdown_path"])
                    .first()
                )

                if existing_task:
                    # UPDATE existing task
                    # Only update fields that should sync from markdown
                    existing_task.title = task_data["title"]
                    existing_task.category = task_data["category"]
                    existing_task.sprint_id = sprint.id
                    existing_task.due_date = task_data["due_date"]
                    existing_task.description = (
                        f"Semana {task_data['week']} - {task_data['category']}"
                    )
                    # Keep existing ID and order_index (unless we want to sync order too)
                    tasks_updated += 1
                else:
                    # CREATE new task
                    new_task = Task(
                        title=task_data["title"],
                        category=task_data["category"],
                        markdown_path=task_data["markdown_path"],
                        sprint_id=sprint.id,
                        due_date=task_data["due_date"],
                        description=f"Semana {task_data['week']} - {task_data['category']}",
                    )
                    db.add(new_task)
                    tasks_created += 1

                tasks_synced += 1
                # print(
                #     f"      {status_icon} {task_data['title']} ({task_data['category']})"
                # )

            db.commit()
            print(
                f"   ✅ Sprint {sprint.number} Synced: {tasks_created} New, {tasks_updated} Updated.\n"
            )

        print("=" * 80)
        print("✅ CURRICULUM SYNC COMPLETED")
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

    # Seed curriculum (Smart Sync Mode - clear_existing is ignored inside)
    seed_curriculum(schedule_files, clear_existing=False)


if __name__ == "__main__":
    main()
