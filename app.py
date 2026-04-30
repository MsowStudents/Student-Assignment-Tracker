assignments = []

def add_assignment():
    course = input("Enter course name: ")
    title = input("Enter assignment title: ")
    due_date = input("Enter due date: ")

    assignment = {
        "course": course,
        "title": title,
        "due_date": due_date,
        "completed": False
    }

    assignments.append(assignment)
    print("Assignment added successfully!\n")

def view_assignments():
    if len(assignments) == 0:
        print("No assignments yet.\n")
    else:
        for i, assignment in enumerate(assignments, start=1):
            status = "Done" if assignment["completed"] else "Not Done"
            print(f"{i}. {assignment['course']} - {assignment['title']} - Due: {assignment['due_date']} - {status}")
        print()

def main():
    while True:
        print("Student Assignment Tracker")
        print("1. Add assignment")
        print("2. View assignments")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_assignment()
        elif choice == "2":
            view_assignments()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

main()