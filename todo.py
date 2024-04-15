import tkinter as tk
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firebase
cred = credentials.Certificate('serviceAccountKey.json') # enter path here
firebase_app = initialize_app(cred)
db = firestore.client()

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List')

        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack()

        self.load_tasks()

        self.add_button = tk.Button(root, text='Add Task', command=self.add_task)
        self.add_button.pack()

    def load_tasks(self):
        try:
            tasks_ref = db.collection('tasks')
            tasks = tasks_ref.stream()
            for task in tasks:
                task_data = task.to_dict()
                self.task_listbox.insert(tk.END, f"{task_data['title']} - Due: {task_data['dueTime']}")
        except Exception as e:
            print(f"Error loading tasks: {e}")

    def add_task(self):
        add_task_window = tk.Toplevel(self.root)
        add_task_window.title('Add Task')

        title_label = tk.Label(add_task_window, text='Title:')
        title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(add_task_window)
        self.title_entry.grid(row=0, column=1)

        due_time_label = tk.Label(add_task_window, text='Due Time:')
        due_time_label.grid(row=1, column=0)
        self.due_time_entry = tk.Entry(add_task_window)
        self.due_time_entry.grid(row=1, column=1)

        add_button = tk.Button(add_task_window, text='Add', command=self.save_task)
        add_button.grid(row=2, columnspan=2)

    def save_task(self):
        try:
            title = self.title_entry.get()
            due_time = self.due_time_entry.get()

            if title and due_time:
                tasks_ref = db.collection('tasks')
                tasks_ref.add({
                    'title': title,
                    'dueTime': due_time
                })

                # Update task list
                self.task_listbox.delete(0, tk.END)
                self.load_tasks()

            self.root.destroy()
        except Exception as e:
            print(f"Error saving task: {e}")

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
