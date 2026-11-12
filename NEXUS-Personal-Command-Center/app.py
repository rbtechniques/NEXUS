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
        print("[4] Notes Manager")
        print("[5] Complete a Task")
        print("[6] Exit")

    
    def complete_task(self):
        self.view_tasks()

        if not self.tasks:
            return

        try:
            task_number = int(input("\nEnter task number to complete: "))

            if task_number < 1 or task_number > len(self.tasks):
                print("Invalid task number!")
                return

            task = self.tasks[task_number - 1]

            if task["completed"]:
                print("This task is already completed!")
            else:
                task["completed"] = True
                save_data("tasks.json", self.tasks)
                print("Task completed successfully!")

        except ValueError:
            print("Please enter a valid number.")

    
    def add_note(self):
        title = input("\nEnter note title: ").strip()

        if not title:
            print("Note title cannot be empty.")
            return

        content = input("Enter note content: ").strip()

        if not content:
            print("Note content cannot be empty.")
            return

        note = Note(title, content)
        self.notes.append(note.to_dict())

        save_data("notes.json", self.notes)

        print("Note saved successfully!")


    def delete_note(self):
        self.view_notes()

        if not self.notes:
            return

        try:
            note_number = int(input("\nEnter note number to delete: "))

            if note_number < 1 or note_number > len(self.notes):
                print("Invalid note number!")
                return

            removed_note = self.notes.pop(note_number - 1)

            save_data("notes.json", self.notes)

            print(f"Note '{removed_note['title']}' deleted successfully!")

        except ValueError:
            print("Please enter a valid number.")

    
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
                self.notes_menu()

            elif choice == "5":
                self.complete_task()

            elif choice == "6":
                print("\nShutting down NEXUS...")
                break

            else:
                print("\nInvalid option! Try again.")

    def notes_menu(self):
        while True:
            print("\n========== NOTES MANAGER ==========")
            print("[1] Add Note")
            print("[2] View Notes")
            print("[3] Delete Note")
            print("[4] Back to Main Menu")

            choice = input("\nNOTES >> ")

            if choice == "1":
                self.add_note()

            elif choice == "2":
                self.view_notes()

            elif choice == "3":
                self.delete_note()

            elif choice == "4":
                break

            else:
                print("Invalid choice!")

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
            print(f"\n{index}. {note['title']}")
            print(f"   {note['content']}")
