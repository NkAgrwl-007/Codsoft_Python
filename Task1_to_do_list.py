import tkinter as tk

def add_task():
    
    task = entry.get()
    if task:
        listbox_tasks.insert(tk.END, f" {task}")
        entry.delete(0, tk.END)

def complete_task():
    try:
        index = listbox_tasks.curselection()
        task = listbox_tasks.get(index)
        listbox_completed.insert(tk.END, task)
        listbox_tasks.delete(index)
    except:
        pass

def undo_task():
    try:
        index = listbox_completed.curselection()
        task = listbox_completed.get(index)
        listbox_tasks.insert(tk.END, task)
        listbox_completed.delete(index)
    except:
        pass

def delete_task():
    try:
        index = listbox_tasks.curselection()
        listbox_tasks.delete(index)
    except:
        pass

def save_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    completed_tasks = listbox_completed.get(0, tk.END)
    with open("todo_list.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
        for task in completed_tasks:
            file.write(f"[X] {task}\n")

def load_tasks():
    try:
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                if task.startswith("[X] "):
                    listbox_completed.insert(tk.END, task[4:].strip())
                else:
                    listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")

label_tasks = tk.Label(root, text="Tasks")
label_tasks.pack()

listbox_tasks = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40,bg="#98F5FF")
listbox_tasks.pack(pady=10)

label_completed = tk.Label(root, text="Completed Tasks")
label_completed.pack()

listbox_completed = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40 ,bg="#98F5FF")
listbox_completed.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)
complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack(side=tk.LEFT, padx=5)
undo_button = tk.Button(root, text="Undo Task", command=undo_task)
undo_button.pack(side=tk.LEFT, padx=5)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

load_tasks()

save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack(pady=10)

root.mainloop()
