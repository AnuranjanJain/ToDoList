import tkinter as tk
from firebase_admin import credentials, firestore, initialize_app
from tkinter import messagebox

# Initialize Firebase
cred = credentials.Certificate('serviceAccountKey.json') #enter your service json path
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

        self.delete_button = tk.Button(root, text='Delete Task', command=self.delete_task)
        self.delete_button.pack()

        self.update_button = tk.Button(root, text='Update Task', command=self.update_task)
        self.update_button.pack()

    def load_tasks(self):
        try:
            self.task_listbox.delete(0, tk.END)  # Clear the listbox before loading tasks
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
                self.load_tasks()

            # Destroy add task window
                #add_task_window.destroy()

        except Exception as e:
            print(f"Error saving task: {e}")


    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task_item = self.task_listbox.get(selected_index)
            task_title = task_item.split(' - ')[0]  # Extract title from listbox item
            tasks_ref = db.collection('tasks')
            query = tasks_ref.where('title', '==', task_title)
            tasks = query.stream()
            for task in tasks:
                task.reference.delete()
            self.load_tasks()  # Refresh task list after deletion
        except Exception as e:
            print(f"Error deleting task: {e}")

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task_item = self.task_listbox.get(selected_index)
            old_title = task_item.split(' - ')[0]  # Extract title from listbox item
        
            update_task_window = tk.Toplevel(self.root)
            update_task_window.title('Update Task')

            title_label = tk.Label(update_task_window, text='New Title:')
            title_label.grid(row=0, column=0)
            self.new_title_entry = tk.Entry(update_task_window)
            self.new_title_entry.grid(row=0, column=1)

            due_time_label = tk.Label(update_task_window, text='New Due Time:')
            due_time_label.grid(row=1, column=0)
            self.new_due_time_entry = tk.Entry(update_task_window)
            self.new_due_time_entry.grid(row=1, column=1)

            update_button = tk.Button(update_task_window, text='Update', command=lambda: self.save_updated_task(old_title))
            update_button.grid(row=2, columnspan=2)
        
        except Exception as e:
            print(f"Error updating task: {e}")

    def save_updated_task(self, old_title):
        try:
            new_title = self.new_title_entry.get()
            new_due_time = self.new_due_time_entry.get()
        
            tasks_ref = db.collection('tasks')
            query = tasks_ref.where('title', '==', old_title)
            tasks = query.stream()
            for task in tasks:
                task.reference.update({'title': new_title, 'dueTime': new_due_time})
            self.load_tasks()  # Refresh task list after update

        except Exception as e:
            print(f"Error saving updated task: {e}")
        # Destroy add task window)


def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
