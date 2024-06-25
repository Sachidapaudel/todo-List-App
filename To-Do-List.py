import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

# Function to add a task to the list
def add_task():
    task = entry_task.get()
    if task != "" and task != "Enter your task here...":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        entry_task.config(fg='grey')
        entry_task.insert(0, "Enter your task here...")
    else:
        tk.messagebox.showwarning(title="Warning!", message="You must enter a task.")

# Function to delete a task from the list
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tk.messagebox.showwarning(title="Warning!", message="You must select a task.")

# Function to update a selected task in the list
def update_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        new_task = entry_task.get()
        if new_task != "" and new_task != "Enter your task here...":
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, new_task)
            entry_task.delete(0, tk.END)
            entry_task.config(fg='grey')
            entry_task.insert(0, "Enter your task here...")
        else:
            tk.messagebox.showwarning(title="Warning!", message="You must enter a task in the placeholder.")
    except:
        tk.messagebox.showwarning(title="Warning!", message="You must enter a task to be updated in the placeholder.")

# Function to clear the placeholder text when the user clicks on the entry field
def on_entry_click(event):
    if entry_task.get() == "Enter your task here...":
        entry_task.delete(0, tk.END)
        entry_task.config(fg='black')

# Function to restore the placeholder text if the entry field is empty
def on_focusout(event):
    if entry_task.get() == "":
        entry_task.config(fg='grey')
        entry_task.insert(0, "Enter your task here...")

# Create main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x400")
root.config(bg="#E5E3BC")  # Set background color to white

# Create a frame for the listbox and scrollbar
frame_tasks = tk.Frame(root, bg="#ffffff")
frame_tasks.pack(pady=10)

# Create a listbox for tasks
listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, font=("Helvetica", 12), bg="#f0f0f0", bd=0, fg="#333")
listbox_tasks.pack(side=tk.LEFT, padx=(10, 0))

# Create a scrollbar for the listbox
scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Create an entry widget for task input with placeholder
entry_task = tk.Entry(root, width=50, font=("Helvetica", 12), fg='grey')
entry_task.insert(0, "Enter your task here...")
entry_task.bind('<FocusIn>', on_entry_click)
entry_task.bind('<FocusOut>', on_focusout)
entry_task.pack(pady=10)

# Create a frame for buttons
frame_buttons = tk.Frame(root, bg="#ffffff")
frame_buttons.pack(pady=10)

# Define button styles
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))
style.configure("Add.TButton", background="#4CAF50", foreground="green")
style.configure("Delete.TButton", background="#f44336", foreground="red")
style.configure("Update.TButton", background="#FFC107", foreground="black")

# Create buttons for adding, deleting, and updating tasks
button_add_task = ttk.Button(frame_buttons, text="Add Task", width=20, command=add_task, style="Add.TButton")
button_add_task.grid(row=0, column=0, padx=5, pady=5)

button_delete_task = ttk.Button(frame_buttons, text="Delete Task", width=20, command=delete_task, style="Delete.TButton")
button_delete_task.grid(row=0, column=1, padx=5, pady=5)

button_update_task = ttk.Button(frame_buttons, text="Update Task", width=20, command=update_task, style="Update.TButton")
button_update_task.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
