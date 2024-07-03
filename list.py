import json

# A simple class to represent each task
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def __repr__(self):
        return f"Task(title={self.title}, completed={self.completed})"

# The main to-do list application class
class ToDoList:
    def __init__(self, storage_file='tasks.json'):
        self.storage_file = storage_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.storage_file, 'r') as file:
                tasks = json.load(file)
                return [Task(**task) for task in tasks]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.storage_file, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def add_task(self, title):
        self.tasks.append(Task(title))
        self.save_tasks()

    def edit_task(self, index, new_title):
        if 0 <= index < len(self.tasks):
            self.tasks[index].title = new_title
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def mark_task(self, index, completed=True):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = completed
            self.save_tasks()

    def show_tasks(self):
        for index, task in enumerate(self.tasks):
            status = '✓' if task.completed else '✗'
            print(f"{index}. [{status}] {task.title}")

# Main program logic
if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List:")
        todo_list.show_tasks()

        print("\nOptions:")
        print("1. Add a task")
        print("2. Edit a task")
        print("3. Delete a task")
        print("4. Mark task as completed")
        print("5. Unmark task as completed")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter the task title: ")
            todo_list.add_task(title)
        elif choice == '2':
            index = int(input("Enter the task number to edit: "))
            new_title = input("Enter the new task title: ")
            todo_list.edit_task(index, new_title)
        elif choice == '3':
            index = int(input("Enter the task number to delete: "))
            todo_list.delete_task(index)
        elif choice == '4':
            index = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_task(index, completed=True)
        elif choice == '5':
            index = int(input("Enter the task number to unmark as completed: "))
            todo_list.mark_task(index, completed=False)
        elif choice == '6':
            break
        else:
            print("Invalid option, please try again.")
