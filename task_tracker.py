def displaymenu():
    print("Menu: ")
    print("1. Add task")
    print("2. Update task")
    print("3. Delete task")
    print("4. List all tasks")
    print("5. List all tasks that are done")
    print("6. List all tasks that are not done")
    print("7. List all task that are in progress")
    print("8. Exit")

def get_user_input():
    displaymenu()
    while True:
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            #add task
            add_task()
        elif choice == "2":
            #update task
            update_task()
        elif choice == "3":
            #delete task:
            delete_task()
        elif choice == "4":
            #List all tasks
            list_tasks()
        elif choice == "5":
            #list all tasks that are done
            list_tasks()
        elif choice == "6":
            #list all tasks that are not done
            list_tasks()
        elif choice == "7":
            #list all tasks that are in progress
            list_tasks()
        elif choice == "8":
            print("Exiting..")
            break
        else:
            print("invalid choice")
            print("Please try again")

def add_task():
    pass

def update_task():
    pass

def delete_task():
    pass

def list_tasks():
    pass

def main():
    #get user input
    get_user_input()
    #write file

if __name__ == '__main__':
    main()