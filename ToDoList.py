
tasks = []

def add_task(task_description):
    """Add a new task to the list."""
    task = {
        'task': task_description,
        'completed': False
    }
    tasks.append(task)
    print(f"Task added: {task_description}")

def delete_task(task_index):
    """Delete a task from the list by its index."""
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task removed: {removed_task['task']}")
    else:
        print("Invalid task index.")

def display_tasks():
    """Display the list of tasks."""
    if not tasks:
        print("No tasks to display.")
    for index, task in enumerate(tasks):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{index + 1}: {task['task']} [{status}]")

def mark_task_complete(task_index):
    """Mark a task as completed."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Task marked as completed: {tasks[task_index]['task']}")
    else:
        print("Invalid task index.")

def main():
    """Main function to run the to-do list application."""
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Display tasks")
        print("4. Mark a task as complete")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task_description = input("Enter the task description: ")
            add_task(task_description)
        elif choice == '2':
            display_tasks()
            try:
                task_index = int(input("Enter the task number to delete: ")) - 1
                delete_task(task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            display_tasks()
            try:
                task_index = int(input("Enter the task number to mark as complete: ")) - 1
                mark_task_complete(task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()