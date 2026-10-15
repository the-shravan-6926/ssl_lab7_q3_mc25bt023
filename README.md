# Task Manager

A Python command-line task manager that stores task records in a CSV file.

## Task Fields
- **Task ID:** Unique numeric identifier.
- **Description:** Task details.
- **Priority:** `low`, `medium`, or `high`.
- **Status:** `pending` or `completed`.

## Features
- Add tasks with a description and priority.
- List all tasks.
- Update a task's status.
- Sort tasks by priority.
- Summarize tasks by status and priority.

## Requirements
- Python 3.10 or later.
- No external packages required.

## Run the Application
```bash
python task_manager.py
```

## Run Tests
```bash
python -m unittest -v
```

## Example Output
```text
Task Manager
Tasks: [...]
Tasks sorted by priority: [...]
Task summary: {'pending': 2, 'completed': 1, ...}
```

## Data Storage
Tasks are stored in `tasks.csv`. The application creates this file with the required headers if it does not exist.
