from models import Task, Note, Habit
from storage import save_data, load_data


class Nexus:

    def __init__(self):
        self.tasks = load_data("tasks.json")
        self.notes = load_data("notes.json")
        self.habits = load_data("habits.json")

    def show_banner(self):
        print("\n" + "=" * 45)
        print("          N E X U S")
        print("     PERSONAL COMMAND CENTER")
        print("=" * 45)

    def show_dashboard(self):
        completed = sum(1 for task in self.tasks if task["completed"])
        total = len(self.tasks)

        print("\n========== DASHBOARD ==========")
        print(f"Total Tasks      : {total}")
        print(f"Completed Tasks  : {completed}")
        print(f"Pending Tasks    : {total - completed}")
        print(f"Total Notes      : {len(self.notes)}")
        print(f"Tracked Habits   : {len(self.habits)}")
        print("===============================")

    def show_menu(self):
        print("\n[1] Dashboard")
        print("[2] View Tasks")
        print("[3] Add Task")
        print("[4] View Notes")
        print("[5] Exit")

    def run(self):
        self.show_banner()

        while True:
            self.show_dashboard()
            self.show_menu()

            choice = input("\nNEXUS >> ")

            if choice == "1":
                self.show_dashboard()

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                self.add_task()

            elif choice == "4":
                self.view_notes()

            elif choice == "5":
                print("\nShutting down NEXUS...")
                break

            else:
                print("\nInvalid option! Try again.")

    def view_tasks(self):
        print("\n========== YOUR TASKS ==========")

        if not self.tasks:
            print("No tasks found.")
            return

        for index, task in enumerate(self.tasks, start=1):
            status = "DONE" if task["completed"] else "PENDING"
            print(f"{index}. {task['title']} [{status}]")

    def add_task(self):
        title = input("\nEnter task title: ").strip()

        if not title:
            print("Task title cannot be empty.")
            return

        task = Task(title)
        self.tasks.append(task.to_dict())

        save_data("tasks.json", self.tasks)

        print("Task added successfully!")

    def view_notes(self):
        print("\n========== YOUR NOTES ==========")

        if not self.notes:
            print("No notes found.")
            return

        for index, note in enumerate(self.notes, start=1):
            print(f"{index}. {note['title']}")
            print(f"   {note['content']}")


class Nexus:

    def __init__(self):
        self.running = True

    def show_dashboard(self):
        print("\n" + "=" * 45)
        print("              N E X U S")
        print("       PERSONAL COMMAND CENTER")
        print("=" * 45)

        print("\nWelcome to NEXUS!")
        print("\nWhat would you like to do today?\n")

        print("1. Task Manager")
        print("2. Notes Manager")
        print("3. Habit Tracker")
        print("4. Focus Timer")
        print("5. Dashboard")
        print("0. Exit")

        print("\n" + "-" * 45)

    def run(self):

        while self.running:

            self.show_dashboard()

            choice = input("Enter your choice: ")

            if choice == "1":
                print("\nTask Manager is coming soon!")

            elif choice == "2":
                print("\nNotes Manager is coming soon!")

            elif choice == "3":
                print("\nHabit Tracker is coming soon!")

            elif choice == "4":
                print("\nFocus Timer is coming soon!")

            elif choice == "5":
                print("\nYou are already on the dashboard!")

            elif choice == "0":
                print("\nThank you for using NEXUS!")
                self.running = False

            else:
                print("\nInvalid choice. Please try again.")
