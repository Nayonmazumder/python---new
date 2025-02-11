tasks = []


def add_task():
    task = input("Please Enter the Task: >>> ")
    tasks.append(task)
    print("Task has been successfully Loaded! ")


def delete_task():
    list_task()
    task_to_delete = int(
        input("Please Enter the Task Number to Delete : >>> "))
    if 0 >= task_to_delete < len(tasks):
        tasks.pop(task_to_delete)
    else:
        print(f"#{task_to_delete} is Not found")


def list_task():
    if len(tasks) == 0:
        print("There is no Task to show!!")
    else:
        for index, task in enumerate(tasks):
            print(f"{index}. {task}", end="\n")


while True:
    print("Welcome To the TODO App !!!")
    print("\n")
    print("...............................")
    print("Please Select from the Options:")
    print("> 1.Add Task")
    print("> 2.List Task")
    print("> 3.Delete Task")
    print("> 4.Exit()")
    print("...............................")
    user_input = input(":>>")
    if user_input == "1":
        add_task()
    elif user_input == "2":
        list_task()
    elif user_input == "3":
        delete_task()
    elif user_input == "4":
        break
    else:
        print("Invaild Input! Try Again.")
print("Have a nice Day !")
