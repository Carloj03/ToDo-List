import json
import os

FILE_NAME = "todo_data.json"
CATEGORIES = ["URGENT", "Prioritize", "Do", "Maybe"]

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {category: [] for category in CATEGORIES}

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def show_tasks(data):
    for category in CATEGORIES:
        print(f"\n{category}:")
        if data[category]:
            for i, task in enumerate(data[category], 1):
                print(f"  {i}. {task}")
        else:
            print("  (No tasks)")

def add_task(data):
    print("\nChoose a category:")
    for i, category in enumerate(CATEGORIES, 1):
        print(f"{i}. {category}")

    try:
        choice = int(input("Category number: "))
        category = CATEGORIES[choice - 1]
        task = input("Enter task description: ").strip()
        if task:
            data[category].append(task)
            save_data(data)
            print("Task added.")
    except (ValueError, IndexError):
        print("Invalid selection.")

def remove_task(data):
    show_tasks(data)
    category = input("\nEnter category name: ").strip().title()

    if category not in CATEGORIES or not data[category]:
        print("Invalid category or no tasks.")
        return

    try:
        task_num = int(input("Task number to remove: "))
        removed = data[category].pop(task_num - 1)
        save_data(data)
        print(f"Removed: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    data = load_data()

    while True:
        print("\nTo-Do List Menu")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(data)
        elif choice == "2":
            add_task(data)
        elif choice == "3":
            remove_task(data)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
