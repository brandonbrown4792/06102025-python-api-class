class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def complete_task(self):
        self.completed = True

    def uncomplete_task(self):
        self.completed = False