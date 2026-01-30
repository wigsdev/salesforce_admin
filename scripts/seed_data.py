import sys
import os
import re

# Add parent directory to path to import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal


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
    source_pattern = re.compile(r"\*\*Fuente\*\*:\s+\[(.+)\]\((.+)\)")

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
                    "source_link": None,  # Init source link
                    "tasks": [],
                }
                continue

            # Match Source Link (Usually right after day header)
            source_match = source_pattern.search(line)
            if source_match and current_day:
                raw_label = source_match.group(1).replace("[", "").replace("]", "")
                raw_path = source_match.group(2)

                # Clean up path (remove ../../)
                clean_path = raw_path.replace("../../", "").replace("../", "")

                current_day["source_label"] = f"Fuente: {raw_label}"
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

        # 5. SEED LUMINA DASHBOARD DATA (Smart Sync)
        print("Seeding Lumina Dashboard Data (Smart Sync)...")
        from app.models.lumina import (
            LuminaDeliverable,
            LuminaTask,
        )

        lumina_days = parse_lumina_checklist()

        if not lumina_days:
            print("Warning: No data parsed from checklist. Skipping sync.")

        # Track active IDs to prune legacy data later
        active_day_ids = []

        for day_data in lumina_days:
            # 1. Sync Day (Deliverable)
            day = (
                db.query(LuminaDeliverable)
                .filter(LuminaDeliverable.title == day_data["title"])
                .first()
            )

            if day:
                # Update existing day fields (except content usually stays same, but good for links)
                day.reference = ""
                day.source_link = day_data.get("source_link")
                day.source_label = day_data.get("source_label")
                print(f"  ~ Updating Day: {day.title}")
            else:
                # Create new day
                print(f"  + Creating Day: {day_data['title']}")
                day = LuminaDeliverable(
                    title=day_data["title"],
                    reference="",
                    source_link=day_data.get("source_link"),
                    source_label=day_data.get("source_label"),
                )
                db.add(day)

            db.flush()
            db.refresh(day)
            active_day_ids.append(day.id)

            # 2. Sync Tasks
            current_tasks = (
                db.query(LuminaTask).filter(LuminaTask.deliverable_id == day.id).all()
            )
            # Map description -> Task object for quick lookups
            task_map = {t.description: t for t in current_tasks}
            active_task_ids = []

            for task_info in day_data["tasks"]:
                description = task_info["desc"]
                doc_path = task_info["path"]

                # FILTER: Skip administrative/Trello tasks
                if description.startswith("Mover a"):
                    continue

                if description in task_map:
                    # Task exists - Update metadata, PRESERVE is_completed
                    existing_task = task_map[description]
                    existing_task.doc_path = doc_path
                    active_task_ids.append(existing_task.id)
                    # print(f"    ~ Synced Task: {description}") # Noise reduction
                else:
                    # Task is new - Create it
                    print(f"    + New Task: {description}")
                    new_task = LuminaTask(
                        deliverable_id=day.id,
                        description=description,
                        doc_path=doc_path,
                        is_completed=False,
                    )
                    db.add(new_task)
                    db.flush()  # Flush to get ID if needed immediately
                    db.refresh(new_task)
                    active_task_ids.append(new_task.id)

            # 3. Prune Tasks (Delete tasks in DB that are no longer in Markdown)
            for old_task in current_tasks:
                if old_task.id not in active_task_ids:
                    print(f"    - Removing Obsolete Task: {old_task.description}")
                    db.delete(old_task)

            # db.commit() removed for atomicity

        # 4. Prune Days (Delete days in DB that are no longer in Markdown)
        all_days = db.query(LuminaDeliverable).all()
        for old_day in all_days:
            if old_day.id not in active_day_ids:
                print(f"  - Removing Obsolete Day: {old_day.title}")
                db.delete(old_day)

        db.commit()
        print("Sync completed successfully!")

    except Exception as e:
        print(f"Error seeding data: {e}")
        db.rollback()
        raise e  # Critical: Re-raise for robust deployment failure
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
