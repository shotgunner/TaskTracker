#!/usr/bin/env python3
import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def get_next_id(tasks):
    return max([task['id'] for task in tasks], default=0) + 1

def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task updated successfully (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Task deleted successfully (ID: {task_id})")

def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as {status} (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found")

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python task-cli.py <command> [args...]")
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) == 3:
        add_task(sys.argv[2])
    elif command == "update" and len(sys.argv) == 4:
        update_task(int(sys.argv[2]), sys.argv[3])
    elif command == "delete" and len(sys.argv) == 3:
        delete_task(int(sys.argv[2]))
    elif command == "mark-in-progress" and len(sys.argv) == 3:
        mark_task(int(sys.argv[2]), "in-progress")
    elif command == "mark-done" and len(sys.argv) == 3:
        mark_task(int(sys.argv[2]), "done")
    elif command == "list":
        if len(sys.argv) == 2:
            list_tasks()
        elif len(sys.argv) == 3 and sys.argv[2] in ["done", "todo", "in-progress"]:
            list_tasks(sys.argv[2])
        else:
            print("Invalid list command")
    else:
        print("Invalid command or arguments")

if __name__ == "__main__":
    main()
