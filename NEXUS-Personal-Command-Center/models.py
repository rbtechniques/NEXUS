
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
    def __init__(self, name):
        self.name = name
        self.completed_days = 0

    def complete_day(self):
        self.completed_days += 1

    def to_dict(self):
        return {
            "name": self.name,
            "completed_days": self.completed_days
        }
