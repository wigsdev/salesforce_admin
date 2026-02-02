"""
Quick script to check what the API is actually returning
"""

import requests

# Test production API
url = "https://admin-salesforce.onrender.com/api/lumina/days"

try:
    response = requests.get(url)
    response.raise_for_status()
    days = response.json()

    print(f"\n{'='*80}")
    print("PRODUCTION API RESPONSE")
    print(f"{'='*80}\n")

    total_tasks = 0
    tasks_with_path = 0

    for day in days:
        print(f"📅 {day['title']}")
        print(f"   Tasks: {len(day['tasks'])}")

        for i, task in enumerate(day["tasks"][:3], 1):
            total_tasks += 1
            doc_path = task.get("doc_path")
            if doc_path:
                tasks_with_path += 1

            print(f"   {i}. {task['desc'][:50]}...")
            print(f"      doc_path: {doc_path or '❌ NULL'}")

        if len(day["tasks"]) > 3:
            # Count remaining tasks
            for task in day["tasks"][3:]:
                total_tasks += 1
                if task.get("doc_path"):
                    tasks_with_path += 1
            print(f"   ... and {len(day['tasks']) - 3} more tasks")
        print()

    print(f"\n{'='*80}")
    print(f"SUMMARY: {tasks_with_path}/{total_tasks} tasks have doc_path in PRODUCTION")
    print(f"{'='*80}\n")

    if tasks_with_path == 0:
        print("❌ CONFIRMED: Database has NULL doc_path values")
        print("✅ SOLUTION: Need to re-run seed to update database")
    else:
        print(f"✅ {tasks_with_path} tasks have doc_path")
        print("⚠️  If icons still don't show, it's a frontend issue")

except Exception as e:
    print(f"❌ Error: {e}")
