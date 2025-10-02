# Author: Adeoluwa (Ade) Olateru-Olagbegi
# Project: Task Manager App
# Date: 08/05/2025
# Description: Lightweight Python app that manages tasks with add, edit, 
# and completion features. Stores data in JSON for persistence.

import json

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task_name):
    tasks = load_tasks()
    tasks.append({"task": task_name, "completed": False})
    save_tasks(tasks)

def edit_task(index, new_name):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["task"] = new_name
        save_tasks(tasks)

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)

def view_tasks():
    return load_tasks()


# -------------------------
# Test Calls
# -------------------------
add_task("Finish resume update")
add_task("Study for CS exam")
print("Tasks after adding:", view_tasks())

edit_task(0, "Finish resume and upload to LinkedIn")
print("Tasks after editing first task:", view_tasks())

complete_task(1)
print("Tasks after completing second task:", view_tasks())