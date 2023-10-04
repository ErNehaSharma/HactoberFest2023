import datetime
import time

# Define a dictionary to store tasks and their due dates
tasks = {}

def add_task():
    task_name = input("Enter the task name: ")
    due_date_str = input("Enter the due date (YYYY-MM-DD HH:MM): ")

    try:
        due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
        tasks[task_name] = due_date
        print(f"Task '{task_name}' added with due date {due_date}.")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD HH:MM format.")

def list_tasks():
    if tasks:
        print("Tasks:")
        for task, due_date in tasks.items():
            print(f"{task} - Due on {due_date}")
    else:
        print("No tasks scheduled.")

def remind_tasks():
    current_time = datetime.datetime.now()
    for task, due_date in tasks.items():
        if current_time >= due_date:
            print(f"Reminder: Task '{task}' was due at {due_date}.")
            del tasks[task]

while True:
    print("\nTask Reminder Menu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remind Tasks")
    print("4. Quit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        remind_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

# Optional: Save tasks to a file or database for persistence
# Example: You can pickle the 'tasks' dictionary and save it to a file
# for later retrieval.
