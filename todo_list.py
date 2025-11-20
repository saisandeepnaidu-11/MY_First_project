import json
def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{i+1}. {task['title']} [{status}]")
add_task("Finish Python project")
list_tasks()
