
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
