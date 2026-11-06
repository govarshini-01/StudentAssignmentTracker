
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
    name = input("Enter task name: ")
    subject = input("Enter subject: ")
    deadline = input("Enter deadline: ")

    task = {
        "id": len(tasks) + 1,
        "name": name,
        "subject": subject,
        "deadline": deadline,
        "status": "Pending"
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task created successfully!")


def view_tasks(tasks):
    print("\n--- Student Tasks ---")
    if not tasks:
        print("No tasks available.")
    for task in tasks:
        print(task)


def main():
    tasks = load_tasks()

    while True:
        print("\n===== STUDENT TASK MANAGEMENT =====")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
