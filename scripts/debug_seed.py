"""Debug script to test seed parsing logic"""

import re
from pathlib import Path

# Read the checklist
checklist_path = Path("content/Lumina_Tech/Archivos_intermedios/Checklist_por_dia.md")
content = checklist_path.read_text(encoding="utf-8")

# Patterns (copied from seed_data.py)
day_pattern = re.compile(r"^##\s+📅\s+(Día\s+\d+.*)", re.MULTILINE)
source_pattern = re.compile(r"\*\*Fuente\*\*:\s+\[(.*?)\]\((.*?)\)")
task_pattern = re.compile(r"^\d+\.\s+\*\*(.*)\*\*", re.MULTILINE)
link_pattern = re.compile(r"\[.*?\]\((.*?)\)")

days = []
current_day = None

for line in content.splitlines():
    # Match Day Header
    day_match = day_pattern.match(line)
    if day_match:
        if current_day:
            days.append(current_day)

        day_title = day_match.group(1)
        ref_part = day_title.split(":")[0]
        current_day = {
            "title": f"📅 {day_title}",
            "reference": f"Log: {ref_part}",
            "source_link": None,
            "tasks": [],
        }
        continue

    # Match Source Link
    source_match = source_pattern.search(line)
    if source_match and current_day:
        raw_label = source_match.group(1).replace("[", "").replace("]", "")
        raw_path = source_match.group(2)
        clean_path = raw_path.replace("../../", "").replace("../", "")
        current_day["source_label"] = f"Fuente: {raw_label}"
        current_day["source_link"] = clean_path
        continue

    # Match Task Title
    task_match = task_pattern.match(line)
    if task_match and current_day:
        title = task_match.group(1).rstrip(".")
        current_day["tasks"].append({"desc": title, "path": None})
        # REMOVED: continue  # ← This was the bug

    # Match Link
    link_match = link_pattern.search(line)
    if link_match and current_day and current_day["tasks"]:
        rel_path = link_match.group(1)
        # Clean up '../Bitacoras_Sprint_1/' from the path
        rel_path = rel_path.replace("../Bitacoras_Sprint_1/", "")
        full_path = f"Lumina_Tech/Bitacoras_Sprint_1/{rel_path}"
        current_day["tasks"][-1]["path"] = full_path

if current_day:
    days.append(current_day)

# Print results
print(f"\n{'='*80}")
print(f"PARSED {len(days)} DAYS")
print(f"{'='*80}\n")

for day in days:
    print(f"📅 {day['title']}")
    print(f"   Tasks: {len(day['tasks'])}")

    for i, task in enumerate(day["tasks"][:3], 1):  # Show first 3 tasks
        print(f"   {i}. {task['desc'][:50]}...")
        print(f"      doc_path: {task['path'] or '❌ NONE'}")

    if len(day["tasks"]) > 3:
        print(f"   ... and {len(day['tasks']) - 3} more tasks")
    print()

# Check if ANY task has a path
tasks_with_path = sum(1 for day in days for task in day["tasks"] if task["path"])
total_tasks = sum(len(day["tasks"]) for day in days)

print(f"\n{'='*80}")
print(f"SUMMARY: {tasks_with_path}/{total_tasks} tasks have doc_path")
print(f"{'='*80}\n")

if tasks_with_path == 0:
    print("❌ ERROR: NO TASKS HAVE doc_path!")
    print("This means the parsing is still broken.")
else:
    print(f"✅ SUCCESS: {tasks_with_path} tasks have doc_path")
