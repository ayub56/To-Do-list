FILENAME = "index.json"

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        with open(FILENAME, "a") as file:
            file.write(f'{{"task": "{task}"}}\n')
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")

def view_tasks():
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No tasks found.")
                return
            print("\nTo-Do List:")
            for i, line in enumerate(lines, 1):
                task = line.strip()
                if task.startswith('{') and task.endswith('}'):
                    task_text = task[task.find('"task":') + 8 : -2]
                    print(f"{i}. {task_text}")
    except FileNotFoundError:
        print("No tasks found. Start by adding a task.")

def delete_task():
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
        if not tasks:
            print("No tasks to delete.")
            return
        view_tasks()
        number = int(input("Enter the task number to delete: "))
        if 1 <= number <= len(tasks):
            del tasks[number - 1]
            with open(FILENAME, "w") as file:
                file.writelines(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks to delete.")
    except ValueError:
        print("Please enter a valid number.")

def update_task():
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
        if not tasks:
            print("No tasks to update.")
            return
        view_tasks()
        number = int(input("Enter the task number to update: "))
        if 1 <= number <= len(tasks):
            new_task = input("Enter the new task description: ").strip()
            if new_task:
                tasks[number - 1] = f'{{"task": "{new_task}"}}\n'
                with open(FILENAME, "w") as file:
                    file.writelines(tasks)
                print("Task updated successfully.")
            else:
                print("New task cannot be empty.")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks to update.")
    except ValueError:
        print("Please enter a valid number.")

# Main Menu
while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        update_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
