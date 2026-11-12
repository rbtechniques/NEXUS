
from datetime import date

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed
        }


class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content
        }


class Habit:
    def __init__(self, name, completion_dates=None):
        self.name = name
        self.completion_dates = completion_dates or []

    def complete_day(self):
        today = date.today().isoformat()

        if today not in self.completion_dates:
            self.completion_dates.append(today)
            return True

        return False

    def to_dict(self):
        return {
            "name": self.name,
            "completion_dates": self.completion_dates,
            "completed_days": len(self.completion_dates)
        }
