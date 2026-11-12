
import time


class FocusTimer:

    def countdown(self, minutes, session_name):
        total_seconds = minutes * 60

        print(f"\nStarting {session_name}...")
        print("Press Ctrl + C to stop the timer.\n")

        try:
            while total_seconds > 0:
                mins, secs = divmod(total_seconds, 60)

                timer = f"{mins:02d}:{secs:02d}"

                print(f"\r{session_name}: {timer}", end="", flush=True)

                time.sleep(1)
                total_seconds -= 1

            print(f"\n\n{session_name} completed!")

        except KeyboardInterrupt:
            print("\n\nTimer stopped.")

    def start_focus(self):
        print("\n========== FOCUS TIMER ==========")
        print("[1] Focus Session (25 minutes)")
        print("[2] Short Break (5 minutes)")
        print("[3] Long Break (15 minutes)")
        print("[4] Custom Timer")
        print("[5] Back")

        choice = input("\nFOCUS >> ")

        if choice == "1":
            self.countdown(25, "Focus Session")

        elif choice == "2":
            self.countdown(5, "Short Break")

        elif choice == "3":
            self.countdown(15, "Long Break")

        elif choice == "4":
            try:
                minutes = int(input("Enter duration in minutes: "))

                if minutes <= 0:
                    print("Duration must be positive!")
                elif minutes > 180:
                    print("Maximum duration is 180 minutes!")
                else:
                    self.countdown(minutes, "Custom Session")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            return

        else:
            print("Invalid choice!")
