import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).with_name("assignments.json")


def load_assignments():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []


def save_assignments(assignments):
    with open(DATA_FILE, "w") as file:
        json.dump(assignments, file, indent=4)


def add_assignment(assignments):
    title = input("Enter assignment title: ")
    subject = input("Enter subject: ")

    while True:
        deadline = input("Enter deadline (YYYY-MM-DD): ")
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Try again.")

    assignment = {
        "id": len(assignments) + 1,
        "title": title,
        "subject": subject,
        "deadline": deadline,
        "completed": False
    }

    assignments.append(assignment)
    save_assignments(assignments)

    print("Assignment added successfully!")


def view_assignments(assignments):
    if not assignments:
        print("No assignments available.")
        return

    today = datetime.today().date()

    for assignment in assignments:
        status = (
            "Completed"
            if assignment["completed"]
            else "Pending"
        )

        deadline = datetime.strptime(
            assignment["deadline"], "%Y-%m-%d"
        ).date()

        if not assignment["completed"] and deadline < today:
            status = "Overdue"

        print("\n-------------------------")
        print("ID:", assignment["id"])
        print("Title:", assignment["title"])
        print("Subject:", assignment["subject"])
        print("Deadline:", assignment["deadline"])
        print("Status:", status)


def update_assignment(assignments):
    view_assignments(assignments)

    try:
        assignment_id = int(input("\nEnter assignment ID: "))
    except ValueError:
        print("Enter a valid ID.")
        return

    for assignment in assignments:
        if assignment["id"] == assignment_id:
            title = input("Enter new title: ").strip()
            subject = input("Enter new subject: ").strip()

            if not title or not subject:
                print("Title and subject cannot be empty.")
                return

            assignment["title"] = title
            assignment["subject"] = subject

            save_assignments(assignments)
            print("Assignment updated successfully!")
            return

    print("Assignment not found.")


def complete_assignment(assignments):
    view_assignments(assignments)

    try:
        assignment_id = int(input("\nEnter assignment ID: "))
    except ValueError:
        print("Enter a valid ID.")
        return

    for assignment in assignments:
        if assignment["id"] == assignment_id:
            if assignment["completed"]:
                print("This assignment is already completed.")
                return

            assignment["completed"] = True
            save_assignments(assignments)
            print("Assignment marked as completed!")
            return

    print("Assignment not found.")


def main():
    assignments = load_assignments()

    while True:
        print("\n===== STUDENT ASSIGNMENT TRACKER =====")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Update Assignment")
        print("4. Complete Assignment")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_assignment(assignments)

        elif choice == "2":
            view_assignments(assignments)

        elif choice == "3":
            update_assignment(assignments)

        elif choice == "4":
            complete_assignment(assignments)

        elif choice == "5":
            print("Thank you for using the application!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
