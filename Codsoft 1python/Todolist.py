import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        # Frame for listbox and scrollbar
        self.frame = tk.Frame(self.root, bg="#ffffff")
        self.frame.pack(pady=10)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Listbox
        self.listbox = tk.Listbox(self.frame, width=50, height=15, yscrollcommand=self.scrollbar.set, selectmode=tk.SINGLE, bg="#e6e6e6")
        self.listbox.pack(padx=10, pady=10)
        self.scrollbar.config(command=self.listbox.yview)

        # Entry widget for task input
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="#4CAF50", fg="#ffffff")
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task, bg="#2196F3", fg="#ffffff")
        self.complete_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task, bg="#f44336", fg="#ffffff")
        self.remove_button.pack(pady=5)

        self.clear_button = tk.Button(self.root, text="Clear All Tasks", command=self.clear_tasks, bg="#9E9E9E", fg="#ffffff")
        self.clear_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def complete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            task = self.listbox.get(selected_index)
            self.listbox.delete(selected_index)
            self.listbox.insert(tk.END, f"[Completed] {task}")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to complete.")

    def remove_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")

    def clear_tasks(self):
        self.listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
