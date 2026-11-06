
import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def create_task(tasks):
    task = {
        "id": max([t["id"] for t in tasks], default=0) + 1,
        "name": input("Enter task name: "),
        "subject": input("Enter subject: "),
        "deadline": input("Enter deadline: "),
        "status": "Pending"
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task created successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    for task in tasks:
        print(task)


def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    task_id = int(input("Enter Task ID to update: "))

    for task in tasks:
        if task["id"] == task_id:
            task["name"] = input("Enter new task name: ")
            task["subject"] = input("Enter new subject: ")
            task["deadline"] = input("Enter new deadline: ")
            save_tasks(tasks)
            print("Task updated successfully!")
            return

    print("Task ID not found!")


def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    task_id = int(input("Enter Task ID to complete: "))

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_tasks(tasks)
            print("Task completed successfully!")
            return

    print("Task ID not found!")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== STUDENT TASK MANAGEMENT =====")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
