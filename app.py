import json

assignments = []

def load_assignments():
    global assignments
    try:
        with open("assignments.json", "r") as file:
            assignments = json.load(file)
    except FileNotFoundError:
        assignments = []

def save_assignments():
    with open("assignments.json", "w") as file:
        json.dump(assignments, file, indent=4)

def add_assignment():
    title = input("Enter assignment title: ")
    course = input("Enter course name: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    assignment = {
        "title": title,
        "course": course,
        "due_date": due_date,
        "completed": False
    }

    assignments.append(assignment)
    save_assignments()
    print("Assignment added!\n")

def view_assignments():
    if not assignments:
        print("No assignments yet.\n")
        return

    sorted_assignments = sorted(assignments, key=lambda a: a["due_date"])

    for i, a in enumerate(sorted_assignments):
        status = "Done" if a["completed"] else "Pending"
        print(f"{i+1}. {a['title']} ({a['course']}) - Due: {a['due_date']} [{status}]")
    print()

def mark_completed():
    view_assignments()

    if not assignments:
        return

    try:
        choice = int(input("Enter assignment number to mark as completed: "))
        sorted_assignments = sorted(assignments, key=lambda a: a["due_date"])
        selected_assignment = sorted_assignments[choice - 1]
        selected_assignment["completed"] = True
        save_assignments()
        print("Marked as completed!\n")
    except:
        print("Invalid choice.\n")

def delete_assignment():
    view_assignments()

    if not assignments:
        return

    try:
        choice = int(input("Enter assignment number to delete: "))
        sorted_assignments = sorted(assignments, key=lambda a: a["due_date"])
        selected_assignment = sorted_assignments[choice - 1]
        assignments.remove(selected_assignment)
        save_assignments()
        print("Assignment deleted!\n")
    except:
        print("Invalid choice.\n")

def menu():
    load_assignments()

    while True:
        print("=== Assignment Tracker ===")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Mark as Completed")
        print("4. Delete Assignment")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_assignment()
        elif choice == "2":
            view_assignments()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_assignment()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")

menu()