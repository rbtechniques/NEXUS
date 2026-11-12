
import csv
import os


def export_data(tasks, notes, habits):
    os.makedirs("exports", exist_ok=True)

    # Export tasks
    with open("exports/tasks.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["title", "completed"]
        )

        writer.writeheader()
        writer.writerows(tasks)

    # Export notes
    with open("exports/notes.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["title", "content"]
        )

        writer.writeheader()
        writer.writerows(notes)

    # Export habits
    with open("exports/habits.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "completed_days"]
        )

        writer.writeheader()

        for habit in habits:
            writer.writerow({
                "name": habit["name"],
                "completed_days": len(
                    habit.get("completion_dates", [])
                )
            })

    print("\nAll data exported successfully!")
    print("Location: exports/")
