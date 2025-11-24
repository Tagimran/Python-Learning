import json
import os

FILE = "todo.json"

# Create file if it does not exist
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)

# Load tasks from JSON
def load_tasks():
    with open(FILE, "r") as f:
        return json.load(f)

# Save tasks to JSON
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add a new task
def add_task():
    task = input("Enter task: ")
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "Done" if t["done"] else "Pending"
        print(f"{i}. {t['task']} [{status}]")

# Mark a task as done
def mark_done():
    view_tasks()
    index = int(input("Enter task number to mark as done: "))
    tasks = load_tasks()
    tasks[index - 1]["done"] = True
    save_tasks(tasks)
    print("Task marked as done!")

# Delete a task
def delete_task():
    view_tasks()
    index = int(input("Enter task number to delete: "))
    tasks = load_tasks()
    tasks.pop(index - 1)
    save_tasks(tasks)
    print("Task deleted successfully!")

# Main menu loop
while True:
    print("\n==== TO-DO MANAGER ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid option. Please try again.")
