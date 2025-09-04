from datetime import datetime

class Task:
    def __init__(self, title, deadline=None):
        self.title = title
        self.deadline = deadline
        self.status = "pending"

    def mark_done(self):
        self.status = "done"

    def __str__(self):
        deadline_str = f" (Due: {self.deadline})" if self.deadline else ""
        return f"[{self.status.upper()}] {self.title}{deadline_str}"


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks.pop(index)
        return None

    def list_all(self):
        return self.tasks

    def list_pending(self):
        return [t for t in self.tasks if t.status == "pending"]


class User:
    def __init__(self, name):
        self.name = name
        self.tasklist = TaskList()

    def add_task(self, title, deadline=None):
        task = Task(title, deadline)
        self.tasklist.add_task(task)

    def complete_task(self, index):
        if 0 <= index < len(self.tasklist.tasks):
            self.tasklist.tasks[index].mark_done()


class App:
    def __init__(self, user):
        self.user = user

    def run(self):
        while True:
            print("\n--- To-Do List Menu ---")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Mark Task as Done")
            print("4. Remove Task")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                tasks = self.user.tasklist.list_all()
                if not tasks:
                    print("No tasks yet.")
                else:
                    for i, task in enumerate(tasks):
                        print(f"{i+1}. {task}")

            elif choice == "2":
                title = input("Enter task title: ")
                deadline = input("Enter deadline (YYYY-MM-DD) or leave empty: ")
                deadline = deadline if deadline else None
                self.user.add_task(title, deadline)
                print("Task added!")

            elif choice == "3":
                index = int(input("Enter task number to mark as done: ")) - 1
                self.user.complete_task(index)
                print("Task marked as done!")

            elif choice == "4":
                index = int(input("Enter task number to remove: ")) - 1
                removed = self.user.tasklist.remove_task(index)
                if removed:
                    print(f"Removed: {removed.title}")
                else:
                    print("Invalid task number.")

            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    name = input("Enter your name: ")
    user = User(name)
    app = App(user)
    app.run()
