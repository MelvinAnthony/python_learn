import uuid
import json
import os

# File to store tasks
task_file = "tasks.json"
tasks = {}

# ================= File Handling =================
def load_task():
    """Load tasks from JSON file"""
    global tasks
    if os.path.exists(task_file):
        with open(task_file, "r") as f:
            try:
                tasks = json.load(f)
            except json.JSONDecodeError:
                tasks = {}   # if file is empty or invalid
    else:
        tasks = {}

def save_tasks():
    """Save tasks into JSON file"""
    with open(task_file, "w") as f:
        json.dump(tasks, f, indent=4)


# ================= Task Functions =================
def add_task(description, status="pending"):
    """Add new task"""
    task_id = str(uuid.uuid4())
    tasks[task_id] = {"description": description, "status": status.capitalize()}
    save_tasks()
    print(f"✅ Task added! ID: {task_id}")


def view_all_tasks():
    """View all tasks"""
    if tasks:
        for task_id, task_info in tasks.items():
            print(f"\nID: {task_id}")
            print(f"Description: {task_info['description']}")
            print(f"Status: {task_info['status']}")
    else:
        print("⚠ No tasks found")


def view_task_by_status(status):
    """View tasks filtered by status"""
    found = False
    for t_id, t_info in tasks.items():
        if t_info['status'].lower() == status.lower():
            found = True
            print(f"\nID: {t_id}")
            print(f"Description: {t_info['description']}")
            print(f"Status: {t_info['status']}")
    if not found:
        print(f"⚠ No tasks found with status '{status}'")


def update_task(t_u_id, new_desc=None, new_status=None):
    """Update task description or status"""
    if t_u_id in tasks:
        if new_status and new_status.lower() in ["pending", "done"]:
            tasks[t_u_id]['status'] = new_status.capitalize()
        if new_desc:
            tasks[t_u_id]['description'] = new_desc
        save_tasks()
        print("✅ Task updated successfully")
    else:
        print("⚠ Task ID not found")


def delete_task(en_d_id):
    """Delete a task by ID"""
    if en_d_id in tasks:
        tasks.pop(en_d_id)
        save_tasks()
        print(f"🗑 Task {en_d_id} deleted successfully")
    else:
        print("⚠ Invalid Task ID")


# ================= Menu =================
def menu():
    load_task()  # load tasks when program starts
    while True:
        print("\n====== To-Do List Application ======")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Tasks by Status")
        print("4. Delete Task")
        print("5. Update Task")
        print("6. Exit")

        try:
            choice = int(input("\nChoose an option: "))
        except ValueError:
            print("⚠ Invalid input! Enter a number 1–6.")
            continue

        if choice == 1:
            en_desc = input("Enter task description: ")
            add_task(en_desc)

        elif choice == 2:
            view_all_tasks()

        elif choice == 3:
            en_s = input("Enter the status (Pending/Done): ")
            view_task_by_status(en_s)

        elif choice == 4:
            en_d_id = input("Enter the task ID to delete: ")
            delete_task(en_d_id)

        elif choice == 5:
            en_d_id = input("Enter the task ID: ")
            en_new_desc = input("Enter new description (leave blank to keep same): ")
            en_new_status = input("Enter new status (Pending/Done, leave blank to keep same): ")
            update_task(en_d_id, en_new_desc if en_new_desc else None,
                        en_new_status if en_new_status else None)

        elif choice == 6:
            print("👋 Exiting... Tasks saved to file.")
            break

        else:
            print("⚠ Invalid choice! Please enter between 1–6.")


# ================= Run Program =================
if __name__ == "__main__":
    menu()
