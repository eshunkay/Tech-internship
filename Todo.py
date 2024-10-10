# Initialize empty lists to store tasks and archived tasks
tasks = []
archived_tasks = []

# Function to add a task (starts as 'Pending')
def add_task(task):
    """Add a new task to the list (starts as pending)"""
    tasks.append({"task": task, "completed": False, "status": "Pending"})
    print(f"Task '{task}' added to your to-do list (Pending approval)!")

# Function to approve a task (move from Pending to Incomplete)
def approve_task(task_number):
    """Approve a task to move it from 'Pending' to 'Incomplete'"""
    pending_tasks = [task for task in tasks if task["status"] == "Pending"]
    
    if 0 < task_number <= len(pending_tasks):
        # Get the task from the filtered pending list
        task_to_approve = pending_tasks[task_number - 1]
        task_to_approve["status"] = "Incomplete"
        print(f"Task '{task_to_approve['task']}' is now marked as 'Incomplete' and can be worked on!")
    else:
        print("Invalid task number!")

# Function to view all tasks
def view_tasks():
    """View all tasks with their completion status and categories"""
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nHere are your current tasks:")
        for idx, task in enumerate(tasks, 1):
            status = task["status"]
            completed = "Done" if task["completed"] else "Not done"
            print(f"{idx}. {task['task']} - Status: {status}, Completion: {completed}")
        print()

# Function to view pending tasks
def view_pending_tasks():
    """View only pending tasks (those waiting for approval)"""
    pending_tasks = [task for task in tasks if task["status"] == "Pending"]

    if not pending_tasks:
        print("There are no pending tasks.")
    else:
        print("\nPending tasks:")
        for idx, task in enumerate(pending_tasks, 1):
            print(f"{idx}. {task['task']} - Status: Pending")
        print()

# Function to mark a task as complete
def complete_task(task_number):
    """Mark a task as complete by its number"""
    if 0 < task_number <= len(tasks):
        if tasks[task_number - 1]["status"] == "Incomplete":
            tasks[task_number - 1]["completed"] = True
            tasks[task_number - 1]["status"] = "Complete"
            print(f"Task {task_number} marked as complete!")
        else:
            print("You can only complete tasks that are 'Incomplete'.")
    else:
        print("Invalid task number!")

# Function to remove a task (moves it to archived tasks)
def remove_task(task_number):
    """Remove a task and archive it"""
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        archived_tasks.append(removed_task)
        print(f"Task '{removed_task['task']}' archived and removed from the active list!")
    else:
        print("Invalid task number!")

# Function to view archived tasks
def view_archived_tasks():
    """View all archived tasks"""
    if not archived_tasks:
        print("No tasks in the archive.")
    else:
        print("\nArchived tasks:")
        for idx, task in enumerate(archived_tasks, 1):
            print(f"{idx}. {task['task']} - Status: Archived")
        print()

# Function to restore a task from the archive
def restore_task(task_number):
    """Restore a task from the archive back to the active task list"""
    if 0 < task_number <= len(archived_tasks):
        restored_task = archived_tasks.pop(task_number - 1)
        tasks.append(restored_task)
        print(f"Task '{restored_task['task']}' restored to your to-do list!")
    else:
        print("Invalid task number!")

# Main program loop for user interaction
while True:
    print("\nWhat would you like to do?")
    print("1. Add a task")
    print("2. View pending tasks")
    print("3. Approve a pending task")
    print("4. View all tasks")
    print("5. Complete a task")
    print("6. Remove (archive) a task")
    print("7. View archived tasks")
    print("8. Restore a task from the archive")
    print("9. Exit")

    choice = input("Choose an option (1-9): ")

    if choice == "1":
        task_description = input("Enter the task description: ")
        add_task(task_description)

    elif choice == "2":
        view_pending_tasks()

    elif choice == "3":
        view_pending_tasks()  # Show pending tasks before approving
        task_number = int(input("Enter the pending task number to approve: "))
        approve_task(task_number)

    elif choice == "4":
        view_tasks()

    elif choice == "5":
        task_number = int(input("Enter the task number to complete: "))
        complete_task(task_number)

    elif choice == "6":
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)

    elif choice == "7":
        view_archived_tasks()

    elif choice == "8":
        task_number = int(input("Enter the archived task number to restore: "))
        restore_task(task_number)

    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please choose a number between 1 and 9.")
