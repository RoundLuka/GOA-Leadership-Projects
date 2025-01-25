# To do list program - using txt file for data store

# function to return all task lines from tasks file
def load_tasks(file_name):
    try:
        # opening file in reading mode, as we dont need any extra accces
        with open(file_name, "r") as file:
            # file.read() function reads entire content of txt file, and split line removes new lines and puts each item as element in list
            return file.read().splitlines()
    except: # excepted error: FileNotFoundError, if file isn't yet created can't read from it
        return []

# function to save given tasks in file, tasks that have to be saved is given as parameter as well as file
def save_tasks(file_name, tasks):
    # opening file in write mode
    with open(file_name, "w") as file:
        # putting new line as serparator in between each task and writing it in file
        file.write("\n".join(tasks))

def main():
    file_name = "tasks.txt" # file to store tasks
    tasks = load_tasks(file_name) # load tasks that have been previosuly stored in file

    while True:
        # Displaying to-do list with current tasks
        print("\nTo-Do List:")
        # using enumeration to get every task by their index
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}") # printing task after their place 1 - n
        
        # Menu Options
        print("\nOptions")
        print("1 - Add new task")
        print("2 - Remove task")
        print("3 - exit")

        # user choice
        choice = input("Choose option: ")

        if choice == "1": # Add new task
            new_task = input("Enter new task: ")
            tasks.append(new_task)
        
        elif choice == "2": # Remove task
            try:
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    tasks.pop(index)
                else:
                    print("Invalid task number")
            except ValueError: # if user didn't enter number 
                print("Please enter a valid number")
        
        elif choice == "3": # Exit the program
            save_tasks(file_name, tasks) # finally save all tasks at once before exiting
            print("Saved  tasks, Good luck!")
            break
        else: # if user didn't enter any of 3 options
            print("Invalid option, please try again")

# Running the program
main()

