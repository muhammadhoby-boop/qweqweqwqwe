import json
import os

DB_FILE = "tasks.json"


def load(path=DB_FILE):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save(tasks, path=DB_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add(tasks, title):
    task_id = max((t["id"] for t in tasks), default=0) + 1
    tasks.append({"id": task_id, "title": title, "done": False})
    return task_id


def mark_done(tasks, task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            return True
    return False


def delete(tasks, task_id):
    before = len(tasks)
    tasks[:] = [t for t in tasks if t["id"] != task_id]
    return len(tasks) < before
