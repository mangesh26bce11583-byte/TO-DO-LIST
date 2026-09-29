To-Do List Management System

 Project Overview

The To-Do List Management System is a simple Python-based project that helps users manage their daily tasks.

The project is made using basic Python concepts such as lists, loops, conditional statements, user input, and string operations. It provides a menu-based system where users can add tasks, view them, complete them, edit them, search for them, delete them, and check their task summary.

This project is mainly created for learning and practicing Python programming.

 Purpose of the Project

The main purpose of this project is to create a simple task management system while practicing the basic concepts of Python.

It can help a user keep track of daily activities such as:

- College assignments
- Study tasks
- Personal work
- Projects
- Important reminders
- Daily activities

The program runs continuously until the user selects the Exit option.

 Features

The To-Do List contains the following features:

1. Add New Task

Users can add a new task to their To-Do List.

The program also checks whether the task is empty. If the user does not enter anything, the program asks them to enter a valid task.


2. View My Tasks

Users can view all the tasks that they have added.

Each task displays:

- Task number
- Task name
- Task status

A task can have two statuses:

- Pending
- Completed

This makes it easy to understand which tasks are finished and which tasks are still remaining.

3. Complete My Task

Users can select a task from the list and mark it as completed.

Once a task is completed, its status changes from Pending to Completed.

If the user tries to complete a task that is already completed, the program informs the user that the task has already been completed.

4. Delete The Task

Users can delete a particular task from their list.

The program displays the available tasks and asks the user to enter the task number they want to delete.

After deletion, the task is removed from the list.

5. Edit The Task

Users can change or update an existing task.

The user selects the task number and enters the new task name.

The program also checks that the new task is not empty. 

6. Search My Task

Users can search for a particular task by entering a word or part of the task name.

The search is not case-sensitive, so the user does not have to worry about uppercase or lowercase letters.

For example, searching for a word can also find tasks containing that word.

The program also displays the status of the matching task.

7. See Task Summary

The Task Summary gives a quick overview of the current To-Do List.

It shows:

- Total number of tasks
- Number of completed tasks
- Number of pending tasks

This helps the user understand their overall task progress.

8. Clear All The Tasks

Users can delete all tasks at once.

Before deleting everything, the program asks for confirmation.

The user can confirm the deletion or choose not to delete the tasks.

This helps prevent accidental deletion of all tasks.


9. Exit

The user can exit the program by selecting the Exit option.

A thank-you message is displayed before the program closes.


 Input Validation

The program includes basic input validation to make it easier to use.

It handles situations such as:

- Empty task names
- Invalid task numbers
- Non-numeric task selections
- Invalid menu choices
- Trying to complete a task that is already completed
- Trying to work with tasks when no tasks are available
- Searching for a task that does not exist
- Confirming or cancelling deletion of all tasks

If the user enters an option outside the available menu, the program displays an Invalid Choice message.


 Python Concepts Used

This project uses several important Python concepts:

- Variables
- Lists
- Nested lists
- "while" loop
- "for" loop
- "if-elif-else" statements
- User input
- String methods
- Boolean values
- List methods
- Indexing
- Searching
- Adding and deleting list elements
- Updating list elements
- Basic input validation

The project is useful for understanding how different Python concepts can be combined to create a small real-world application.

? Project Structure

The repository contains the main Python file for the To-Do List Management System.

A simple project structure can be maintained like this:

- To-Do List Python file – Contains the complete program
- README.md – Contains information about the project

---

 How to Run the Project

Step 1: Install Python

Make sure Python is installed on your computer.

You can check this from the terminal or command prompt.

Step 2: Download or Clone the Repository

Download this project from GitHub or clone the repository to your computer.

Step 3: Open the Project

Open the project folder using a Python-supported editor such as:

- Visual Studio Code
- PyCharm
- IDLE
- Any other Python editor

Step 4: Run the Program

Run the Python file.

The To-Do List menu will appear in the terminal.

You can then select the required option by entering its number.

---
 How the Program Works

When the program starts, it displays a menu containing different options.

The user selects an option by entering its corresponding number.

For example, the user can:

1. Add a task
2. View existing tasks
3. Complete a task
4. Delete a task
5. Edit a task
6. Search for a task
7. View the task summary
8. Clear all tasks
9. Exit the program

After performing an operation, the program returns to the main menu.

The program continues running until the user selects Exit.

---

Task Status

Every task has a status associated with it.

Pending

A newly added task is initially marked as Pending.

Completed

When the user finishes a task and selects the complete option, the task is marked as Completed.

This allows the user to easily track their progress.

---

What I Learned From This Project

While creating this project, I practiced how to:

- Store multiple tasks using Python lists
- Use loops to repeatedly display a menu
- Take input from users
- Use conditions to make decisions
- Update and delete list items
- Search through a list
- Track completed and pending tasks
- Handle invalid user input
- Build a simple menu-driven application
- Organize multiple features into one Python program

This project helped me understand how basic Python programming concepts can be used together to create a practical application.

---

? Future Improvements

More features can be added to this project in the future, such as:

- Setting task priorities
- Adding due dates
- Adding task categories
- Sorting tasks
- Saving tasks permanently in a file
- Loading tasks when the program starts
- Adding a graphical user interface
- Adding reminders
- Adding task deadlines
- Adding separate task lists for different users

These features can make the project more advanced and useful.

---

 Technologies Used

Programming Language: Python

Interface: Command Line / Terminal

Storage: Python list during program execution

Libraries: No external libraries are required.

---

 Project Type

This is a beginner-level Python project created for learning and practicing programming fundamentals.

It is suitable for students who are learning:

- Python basics
- Loops
- Conditional statements
- Lists
- User input
- Menu-driven programs

---

 Author

Mangesh Jedhe

This project was created as part of my Python programming practice and learning.

---

 Support

If you find this project useful for learning Python, you can  star the repository on GitHub.

Thank you for checking out my project!