import json
import argparse

TASKS_DB = 'tasks.json'

def load_tasks():
    with open(TASKS_DB, 'r') as f:
        tasks = json.load(f)
        if tasks is None:
            return []
        return tasks

def save_tasks(tasks: list):
    with open(TASKS_DB, 'w') as f:
        json.dump(tasks, f)

def add(description: str = ""):
    """
    Add a task with 
    Args:
        description (str): _description_
    """
    tasks = load_tasks()

    tasks.append({
        "id": len(tasks) + 1, # need a better mechanism here
        "description": description,
        "done": False
    })

    save_tasks(tasks)


parser = argparse.ArgumentParser(description='simple task manager in cli')
parser.add_argument("action")
parser.add_argument("task_description")
args = parser.parse_args()

if args.action == 'add':
    add(args.task_description)
