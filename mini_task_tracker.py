import json
TASKS_FILE = "tasks.json"
def load_tasks():
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)
def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
    else:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("Task added.")
def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for number, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Pending"
            print(f"{number}. {task['title']} [{status}]")
def get_task_number(tasks):
    if not tasks:
        print("No tasks available.")
        return None
    try:
        number = int(input("Task number: "))
    except ValueError:
        print("Please enter a valid task number.")
        return None
    if number < 1 or number > len(tasks):
        print("Task number is out of range.")
        return None
    return number - 1
def complete_task(tasks):
    task_index = get_task_number(tasks)
    if task_index is not None:
        tasks[task_index]["done"] = True
        save_tasks(tasks)
        print("Task completed.")
def delete_task(tasks):
    task_index = get_task_number(tasks)
    if task_index is not None:
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Deleted task: {removed_task['title']}")
def main():
    tasks = load_tasks()
    print("--- TASK TRACKER ---")
    print("1. Add 2. View 3. Complete 4. Delete 5. Exit")
    while True:
        choice = input("Choice: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 5.")
if __name__ == "__main__":
    main()
