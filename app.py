try:
    with open("tasks.json", "r") as file:
        tasks = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    tasks = []

# Save tasks to file
def save_tasks():
    with open("tasks.json", "w") as file:
        for task in tasks:
            file.write(task + "\n")
tasks = []
def task():
    print("------Welcome to TO-DO App-------")
while True:
    operation = int(input("Enter the option: \n1-Add Task \n2-View Task \n3-Update Task \n4-Delete Task \n5-Exit "))
    if operation == 1:
        add = input("Enter Task to add :")
        tasks.append(add)
        save_tasks()
        print(f"Task {add} Successfully added in tasks list.")
    elif operation == 2:
        print(f"Total tasks = {tasks}")
    elif operation == 3:
        updated_value = input ("Enter the task you want to update :")
        if updated_value in tasks:
            new_task = input("Enter new task :")
            old_replace = tasks.index(updated_value)
            tasks[old_replace] = new_task
            save_tasks()
            print(f"Updated task is {new_task}")
    elif operation == 4:
        del_task = input("Enter the task you want to delete :")
        if del_task in tasks:
            del_val= tasks.index(del_task)
            del tasks[del_val]
            deleted = del_task
            save_tasks()
            print(f"{deleted} Successfully deleted.")
    elif operation ==5:
        print("Closing the program......")
        break
    else:
        print("This is invalid option.")
        
