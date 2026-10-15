
import csv
import os

CSV_FILE = "tasks.csv"
FIELDS = ["task_id", "description", "priority", "status"]
PRIORITIES = {"low", "medium", "high"}
STATUSES = {"pending", "completed"}


def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()


def load_tasks():
    initialize_csv()
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def add_task(description, priority):
    if not description.strip():
        raise ValueError("Description cannot be empty")
    if priority not in PRIORITIES:
        raise ValueError("Priority must be low, medium, or high")

    tasks = load_tasks()
    task_id = max((int(t["task_id"]) for t in tasks), default=0) + 1

    task = {
        "task_id": str(task_id),
        "description": description.strip(),
        "priority": priority,
        "status": "pending",
    }

    tasks.append(task)
    save_tasks(tasks)
    return task


def save_tasks(tasks):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(tasks)


def list_tasks():
    return load_tasks()


def update_status(task_id, status):
    if status not in STATUSES:
        raise ValueError("Status must be pending or completed")

    tasks = load_tasks()
    for task in tasks:
        if int(task["task_id"]) == task_id:
            task["status"] = status
            save_tasks(tasks)
            return task

    raise ValueError(f"Task {task_id} not found")


def summarize_tasks():
    tasks = load_tasks()

    summary = {
        "pending": sum(t["status"] == "pending" for t in tasks),
        "completed": sum(t["status"] == "completed" for t in tasks),
        "by_priority": {
            priority: sum(t["priority"] == priority for t in tasks)
            for priority in ("low", "medium", "high")
        },
    }
def tasks_by_priority():
    order = {"high": 0, "medium": 1, "low": 2}
    return sorted(
        load_tasks(),
        key=lambda task: order[task["priority"]]
    )

if __name__ == "__main__":
    initialize_csv()
    print("Task Manager")
    print("Tasks:", list_tasks())
    print("Summary:", summarize_tasks())
