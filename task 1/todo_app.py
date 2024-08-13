import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load existing tasks from the file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i + 1}. {task['description']} [{status}]")

# Add a new task
def add_task(tasks):
    description = input("Enter the task description: ")
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print("Task added.")

# Mark a task as complete
def complete_task(tasks):
    list_tasks(tasks)
    task_number = int(input("Enter the task number to mark as complete: "))
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    list_tasks(tasks)
    task_number = int(input("Enter the task number to delete: "))
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task number.")

# Main menu
def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu")
        print("1. List all tasks")
        print("2. Add a task")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
