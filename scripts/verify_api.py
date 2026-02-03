import requests

try:
    r = requests.get("http://localhost:8000/api/curriculum/sprints")
    print(f"Status: {r.status_code}")

    if r.status_code == 200:
        data = r.json()
        print(f"\nSprints: {len(data)}")

        for sprint in data:
            tasks = sprint.get("tasks", [])
            print(f"\n  Sprint {sprint['number']}: {sprint['name']}")
            print(f"  Start: {sprint['start_date']}")
            print(f"  End: {sprint['end_date']}")
            print(f"  Tasks: {len(tasks)}")

            if tasks:
                print("\n  Task List:")
                for i, task in enumerate(tasks, 1):
                    print(
                        f"    {i}. {task['title']} ({task['category']}) - Due: {task.get('due_date', 'N/A')}"
                    )
    else:
        print(f"Error: {r.text}")

except Exception as e:
    print(f"Error: {e}")
