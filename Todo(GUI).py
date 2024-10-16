import tkinter as tk
from tkinter import messagebox

tasks = []
archived_tasks = []

# Add Task Function
def add_task():
    task = task_input.get()
    if task:
        tasks.append({"task": task, "completed": False, "status": "Pending"})
        task_input.delete(0, tk.END)
        refresh_task_list()
        messagebox.showinfo("Task Added", f"Task '{task}' added successfully!")
    else:
        messagebox.showwarning("Input Error", "Please enter a task description.")

# View Tasks Function
def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks, 1):
        status = task["status"]
        completed = "Done" if task["completed"] else "Not done"
        task_listbox.insert(tk.END, f"{idx}. {task['task']} - Status: {status}, Completion: {completed}")

# Approve Task Function
def approve_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        task = tasks[task_index]
        if task["status"] == "Pending":
            task["status"] = "Incomplete"
            refresh_task_list()
            messagebox.showinfo("Task Approved", f"Task '{task['task']}' approved!")
        else:
            messagebox.showwarning("Approval Error", "Task is not pending approval.")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to approve.")

# Complete Task Function
def complete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        task = tasks[task_index]
        if task["status"] == "Incomplete":
            task["status"] = "Complete"
            task["completed"] = True
            refresh_task_list()
            messagebox.showinfo("Task Completed", f"Task '{task['task']}' marked as complete!")
        else:
            messagebox.showwarning("Completion Error", "Task is not incomplete.")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to complete.")

# Remove Task Function
def remove_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        removed_task = tasks.pop(task_index)
        archived_tasks.append(removed_task)
        refresh_task_list()
        messagebox.showinfo("Task Archived", f"Task '{removed_task['task']}' archived successfully!")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# Restore Task Function
def view_archived_tasks():
    archived_listbox.delete(0, tk.END)
    for idx, task in enumerate(archived_tasks, 1):
        archived_listbox.insert(tk.END, f"{idx}. {task['task']} - Status: Archived")

def restore_task():
    selected_task = archived_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        restored_task = archived_tasks.pop(task_index)
        tasks.append(restored_task)
        refresh_task_list()
        view_archived_tasks()
        messagebox.showinfo("Task Restored", f"Task '{restored_task['task']}' restored to active list!")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to restore.")

# Main GUI Window
root = tk.Tk()
root.title("Task Management System")

# Input Field for adding a taskimport tkinter as tk
from tkinter import ttk, messagebox

tasks = []
archived_tasks = []

# Add Task Function
def add_task():
    task = task_input.get()
    if task:
        tasks.append({"task": task, "completed": False, "status": "Pending"})
        task_input.delete(0, tk.END)
        refresh_task_list()
        messagebox.showinfo("Task Added", f"Task '{task}' added successfully!")
    else:
        messagebox.showwarning("Input Error", "Please enter a task description.")

# View Tasks Function
def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks, 1):
        status = task["status"]
        completed = "Done" if task["completed"] else "Not done"
        task_listbox.insert(tk.END, f"{idx}. {task['task']} - Status: {status}, Completion: {completed}")

# Approve Task Function
def approve_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        task = tasks[task_index]
        if task["status"] == "Pending":
            task["status"] = "Incomplete"
            refresh_task_list()
            messagebox.showinfo("Task Approved", f"Task '{task['task']}' approved!")
        else:
            messagebox.showwarning("Approval Error", "Task is not pending approval.")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to approve.")

# Complete Task Function
def complete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        task = tasks[task_index]
        if task["status"] == "Incomplete":
            task["status"] = "Complete"
            task["completed"] = True
            refresh_task_list()
            messagebox.showinfo("Task Completed", f"Task '{task['task']}' marked as complete!")
        else:
            messagebox.showwarning("Completion Error", "Task is not incomplete.")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to complete.")

# Remove Task Function
def remove_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        removed_task = tasks.pop(task_index)
        archived_tasks.append(removed_task)
        refresh_task_list()
        messagebox.showinfo("Task Archived", f"Task '{removed_task['task']}' archived successfully!")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# Restore Task Function
def view_archived_tasks():
    archived_listbox.delete(0, tk.END)
    for idx, task in enumerate(archived_tasks, 1):
        archived_listbox.insert(tk.END, f"{idx}. {task['task']} - Status: Archived")

def restore_task():
    selected_task = archived_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        restored_task = archived_tasks.pop(task_index)
        tasks.append(restored_task)
        refresh_task_list()
        view_archived_tasks()
        messagebox.showinfo("Task Restored", f"Task '{restored_task['task']}' restored to active list!")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to restore.")

# Main GUI Window
root = tk.Tk()
root.title("Task Management System")
root.geometry("500x600")
root.config(bg="#f0f0f0")  # Light gray background

# Define Fonts
title_font = ("Helvetica", 16, "bold")
button_font = ("Arial", 12)
listbox_font = ("Courier", 12)

# Title Label
title_label = tk.Label(root, text="Task Management System", font=title_font, bg="#4CAF50", fg="white")
title_label.pack(pady=10, fill=tk.X)

# Input Field for adding a task
task_input = tk.Entry(root, width=50, font=listbox_font, bd=3, relief="sunken")
task_input.pack(pady=10)

# Button to add a task
add_task_button = tk.Button(root, text="Add Task", command=add_task, font=button_font, bg="#4CAF50", fg="white", bd=0)
add_task_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=10, font=listbox_font, bg="#e6f7ff", bd=3, relief="sunken")
task_listbox.pack(pady=10)

# Button to approve a task
approve_task_button = tk.Button(root, text="Approve Task", command=approve_task, font=button_font, bg="#FFC107", fg="black", bd=0)
approve_task_button.pack(pady=5)

# Button to mark a task as complete
complete_task_button = tk.Button(root, text="Complete Task", command=complete_task, font=button_font, bg="#2196F3", fg="white", bd=0)
complete_task_button.pack(pady=5)

# Button to remove (archive) a task
remove_task_button = tk.Button(root, text="Archive Task", command=remove_task, font=button_font, bg="#f44336", fg="white", bd=0)
remove_task_button.pack(pady=5)

# Label for archived tasks
archived_label = tk.Label(root, text="Archived Tasks", font=title_font, bg="#607D8B", fg="white")
archived_label.pack(pady=10, fill=tk.X)

# Listbox for archived tasks
archived_listbox = tk.Listbox(root, width=50, height=5, font=listbox_font, bg="#f0f0f0", bd=3, relief="sunken")
archived_listbox.pack(pady=10)

# Button to view archived tasks
view_archived_button = tk.Button(root, text="View Archived Tasks", command=view_archived_tasks, font=button_font, bg="#8BC34A", fg="white", bd=0)
view_archived_button.pack(pady=5)

# Button to restore a task from the archive
restore_task_button = tk.Button(root, text="Restore Archived Task", command=restore_task, font=button_font, bg="#009688", fg="white", bd=0)
restore_task_button.pack(pady=5)

# Run the Tkinter main loop
root.mainloop()

task_input = tk.Entry(root, width=50)
task_input.pack(pady=10)

# Button to add a task
add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack()

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Button to approve a task
approve_task_button = tk.Button(root, text="Approve Task", command=approve_task)
approve_task_button.pack()

# Button to mark a task as complete
complete_task_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_task_button.pack()

# Button to remove (archive) a task
remove_task_button = tk.Button(root, text="Archive Task", command=remove_task)
remove_task_button.pack()

# Label for archived tasks
archived_label = tk.Label(root, text="Archived Tasks")
archived_label.pack()

# Listbox for archived tasks
archived_listbox = tk.Listbox(root, width=50, height=5)
archived_listbox.pack(pady=10)

# Button to view archived tasks
view_archived_button = tk.Button(root, text="View Archived Tasks", command=view_archived_tasks)
view_archived_button.pack()

# Button to restore a task from the archive
restore_task_button = tk.Button(root, text="Restore Archived Task", command=restore_task)
restore_task_button.pack()

# Run the Tkinter main loop
root.mainloop()
