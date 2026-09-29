tasks = []

while True:
    print("\n========== TO DO LIST ==========")
    print("1. Add new Task")
    print("2. View My Tasks")
    print("3. Complete My Task")
    print("4. Delete The Task")
    print("5. Edit The Task")
    print("6. Search My Task")
    print("7. See Task Summary")
    print("8. Clear All The Tasks")
    print("9. Exit")
    print("")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter your task: ")
        if task.strip() == "":
            print("Task cannot be empty.")
        else:
            tasks.append([task, False])
            print("Task added successfully.")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYOUR TASKS")
            for i in range(len(tasks)):
                if tasks[i][1] == True:
                    status = "Completed"
                else:
                    status = "Pending"
                print(str(i + 1) + ". " + tasks[i][0] + " - " + status)
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i][0])
            number = input("Enter task number to complete: ")
            if number.isdigit():
                number = int(number)
                if number >= 1 and number <= len(tasks):
                    if tasks[number - 1][1] == True:
                        print("This task is already completed.")
                    else:
                        tasks[number - 1][1] = True
                        print("Task completed:", tasks[number - 1][0])
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a number.")
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i][0])
            number = input("Enter task number to delete: ")
            if number.isdigit():
                number = int(number)
                if number >= 1 and number <= len(tasks):
                    deleted = tasks.pop(number - 1)
                    print("Task deleted:", deleted[0])
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a number.")
    elif choice == "5":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i][0])
            number = input("Enter task number to edit: ")
            if number.isdigit():
                number = int(number)
                if number >= 1 and number <= len(tasks):
                    new_task = input("Enter new task: ")
                    if new_task.strip() == "":
                        print("Task cannot be empty.")
                    else:
                        tasks[number - 1][0] = new_task
                        print("Task updated successfully.")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a number.")

    elif choice == "6":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            search = input("Enter task name to search: ")
            found = False
            for i in range(len(tasks)):
                if search.lower() in tasks[i][0].lower():
                    if tasks[i][1] == True:
                        status = "Completed"
                    else:
                        status = "Pending"
                    print(i + 1, ".", tasks[i][0], "-", status)
                    found = True
            if found == False:
                print("Task not found.")
    elif choice == "7":
        completed = 0
        pending = 0
        for task in tasks:
            if task[1] == True:
                completed = completed + 1
            else:
                pending = pending + 1
        print("\n--------- TASK SUMMARY ---------")
        print("Total tasks     :", len(tasks))
        print("Completed tasks :", completed)
        print("Pending tasks   :", pending)
    elif choice == "8":
        if len(tasks) == 0:
            print("There are no tasks.")
        else:
            confirm = input("Delete all tasks? (yes/no): ")
            if confirm.lower() == "yes":
                tasks.clear()
                print("All tasks deleted.")
            else:
                print("Tasks were not deleted.")
    elif choice == "9":
        print("Thank you for using To-Do List!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 9.")