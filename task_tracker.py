import csv
import os
import datetime
from task import Task

class Task_tracker:
    def __init__(self, filename='tasks.csv'):
        self.tasks = []
        self.filename = filename

        # Ensure directory exists if needed
        folder = os.path.dirname(self.filename)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)

        self.load_from_csv()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_to_csv()

    def update_task(self, id, status, updateAt):
        found = False  # To check if the ID was found

        for task in self.tasks:
            if task.id == id:  # Use dot notation for Task attributes
                task.status = status
                task.updateAt = updateAt
                found = True
                print(f"Task {id} updated successfully!")
                break
    
        if not found:
            print("ID not found")

        self.save_to_csv()


    def delete_task(self, id):
            self.tasks = [task for task in self.tasks if task.id != id]
            for i, task in enumerate(self.tasks):
                task.id = i + 1
            self.save_to_csv()

    def list_task(self, status_id):
        if status_id == 1:
            for task in self.tasks:
                print(task)
        elif status_id == 2:
            for task in self.tasks:
                if task.status == 'done':
                    print(task)
        elif status_id == 3:
            for task in self.tasks:
                if task.status == 'not done':
                    print(task)
        elif status_id == 4:
            for task in self.tasks:
                if task.status == 'in progress':
                    print(task)

    def save_to_csv(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "Description", "Status", "Created At", "Updated At"])
            for task in self.tasks:
                writer.writerow([task.id, task.description, task.status, task.createdAt, task.updateAt])
        print('tasks saved to ', self.filename)
    
    def load_from_csv(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if row:
                        task = Task(row[0], row[1], row[2], row[3], row[4])
                        self.add_task(task)
                print("task loaded from ", self.filename)
        except FileNotFoundError:
            print(f'{self.filename} not found')


def main():
    task_tracker = Task_tracker()

    print("Task tracker menu:")
    print("1.Add task")
    print("2.Update task")
    print("3.Delete task")
    print("4.List all tasks")
    print("5.List all tasks that are done")
    print("6.List all tasks that are not done")
    print("7.List all task that are in progress")
    print("8.Exit")
    
    while True:
        
        choice = input("Enter your choice:")

        if choice == "1":
            #add task
            id = len(task_tracker.tasks) + 1
            descript = input("write task description: ")
            createdAt = datetime.datetime.now()
            updateAt = createdAt

            task = Task(id=id, description=descript, status='not done', createdAt=createdAt, updateAt=updateAt)

            task_tracker.add_task(task)
        elif choice == "2":
            #update task
            id = input("enter task's id:")
            print("choose status to update: 1.Not done, 2.in-progress, 3-done")
            option = input("enter your choice: ")
            

            if option == "1":
                status = "not done"
            elif option == "2":
                status = "in progress"
            elif option == "3":
                status = "done"
            else:
                print("try again")
            
            updateAt = datetime.datetime.now()

            task_tracker.update_task(id=id, status = status, updateAt=updateAt)
        elif choice == "3":
            #delete task
            id = input("Enter task id to delete:")
            task_tracker.delete_task(id)
            print("task deleted")
        elif choice == "4":
            #list all task
            task_tracker.list_task(1)
        elif choice == "5":
            #list all task that are done
            task_tracker.list_task(2)
        elif choice == "6":
            #list all task that are not done
            task_tracker.list_task(3)
        elif choice == "7":
            task_tracker.list_task(4)
        elif choice == "8":
            print("goodbye")
            break
        else:
            print("invalid choice, try again")

if __name__ == '__main__':
    main()
