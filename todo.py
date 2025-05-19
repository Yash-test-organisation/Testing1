import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Entry box
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Add task button
        self.add_button = tk.Button(root, text="Add Task", width=15, command=self.add_task)
        self.add_button.pack()

        # Task list
        self.task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Delete button
        self.delete_button = tk.Button(root, text="Delete Selected", width=15, command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task.strip() == "":
            messagebox.showwarning("Input Error", "Please enter a task.")
        else:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
