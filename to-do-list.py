from os import system, name
from time import sleep
def show_menu():
    print("\n1)Show tasks")
    print("2)Add a task")
    print("3)Delete a task")
    print("4)Swap two task's place")
    print("5)Exit\n")

def show_tasks(todo):
    print("\nYour tasks:")
    for index, item in enumerate(todo, start=1):
        print(f"{index}.{item}")

print("========= Welcome To ToDoList Program =========")
todo = []

while True:
    show_menu()
    choice = int(input("Your Option: "))
    if choice == 1:
        if not todo:
            print("\tYou don't have any tasks")
        else:
            show_tasks(todo)
    elif choice == 2:
        new_task = input("Enter your new task: ")
        if new_task.strip():
            todo.append(new_task)
            show_tasks(todo)
        else:
            print("Enter a valid input")
    elif choice == 3:
        if not todo:
            print("You don't have any tasks to delete")
        else:
            try:
                show_tasks(todo)
                task_index = int(input("Enter your task index for deleting: "))
                if 1 <= task_index <= len(todo):
                    removed_task = todo.pop(task_index - 1)
                    print(f"item '{removed_task}' deleted.")
                    show_tasks(todo)
                else:
                    print(f"your input is invalid; Enter an index between 1 and {len(todo)}")
            except ValueError:
                print("Invaild input")
    elif choice == 4:
        if len(todo) < 2:
                    print("\nYou don't have enough item to swap")
                    continue
        try:
                show_tasks(todo)
                first_task_index = int(input("Enter your first task index that you want to move: "))
                second_task_index = int(input("Enter your first task index that you want to move: "))
                if 1 <= first_task_index <= len(todo) and 1 <= second_task_index <= len(todo):
                    todo[first_task_index - 1], todo[second_task_index - 1] = todo[second_task_index - 1], todo[first_task_index - 1]
                    print("Your tasks just swaped.")
                    show_tasks(todo)
                else:
                    print(f"Your input is invalid; Enter an index between 1 and {len(todo)}")
        except ValueError:
                print("Invaild input")

    elif choice == 5:
        print("Program closed.")
        break
    else:
        print("\nInvalid input! Try again.")
        print("\n" + "=" * 47)
