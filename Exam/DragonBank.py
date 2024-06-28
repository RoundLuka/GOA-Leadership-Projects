#DragonBank

#Database
name_data = ["luka15","luka0"]
pass_data = ["12345678","manager123"]
balance_data = [0,0]


#managers list and acess password customizible
manager_data = ["luka0"]
access_password = "topsecret"


def create_account():
    while True:
        name = input("Enter your name: ")
        while name in name_data:
            print("name is already taken")
            name = input("Enter your name: ")
        password = input("Enter your password: ")
        while len(password) < 8:
            print("minimal password length is 8")
            password = input("Enter your password: ")
        password_repeat = input("Renter your password: ")
        while password != password_repeat:
            password_repeat = input("Renter your password: ")
        name_data.append(name)
        pass_data.append(password)
        balance_data.append(0)
        print("Account creation finished with success. Thanks for using DragonBank")
        break

def login_account():
    while True:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        for i in range(len(name_data)):
            if name == name_data[i] and password == pass_data[i]:
                print("Authorization successful")
                key = i
                return key

def deposit(key):
    amount = input("Enter your amount to deposit: $")
    if amount.isdigit():
        if int(amount) > 0:
            balance_data[key] += int(amount)
            print(f"You added {amount}$ to your balance")
        else:
            print("Please enter valid amount")
    else:
        print("Please enter valid amount")

def withdraw(key):
    amount = input("Please enter amount to withdraw: $")
    if amount.isdigit():
        if int(amount) > 0 and int(amount) < balance_data[key]:
            balance_data[key] -= int(amount)
            print(f"withdrawn {amount}$ from account")
        else:
            print("you dont have enough balance on account to withdraw",amount)
    else:
        print("Please enter valid amount")

def transfer(key):
    recipient = input("Enter your recipient: ")
    recipient_found = False
    for i in range(len(name_data)):
        if recipient == name_data[i]:
            recipient_key = i
            recipient_found = True
    if recipient_found:
        amount = input(f"Enter amount you are transfering to {recipient}: $")
        if amount.isdigit():
            if int(amount) > 0 and int(amount) < balance_data[key]:
                balance_data[key] -= int(amount)
                balance_data[recipient_key] += int(amount)
                print(f"Transfer to {recipient} sucessful, trasnfered {amount}$")
        else:
            print("Invalid amount")
    else:
        print("There's no such recipient DragonBank")

#function to terminate account
def delete_account(key):
    while True:
        print("!!! Warning !!! Pay attention once you delete your account there is no way of recovering it")
        delete = input("Are you sure you want to permamently delete your account? (1 - Yes go on)(2 - No cancel): ")
        if delete == "1":
            process = input("Do you want to process? (type your account name): ")
            if process == name_data[key]: 
                name_data.pop(key)        #In this program account is only data in data list (data base)
                pass_data.pop(key)        #To delete account have to remove data from data base
                balance_data.pop(key)
                print("Your account has been permamently terminated")
                break
        elif delete == "2":
            print("You have cancelled termination of your account")
            break
        else:
            print("Invalid response")
            continue

#function to search for information, restricted only managers can use this function

def search_info():
    while True:
        view = input("What would you like to view (1 - user)(2 - customer list)(3 - exit): ")
        if view == "1":
            user_found = False
            name = input("Who would you like to view (username): ")
            for i in range(len(name_data) - 1):
                if name == name_data[i]:
                    user_found = True
                    current_balance = str(balance_data[i])
                    print(f"Their balance is {current_balance}$")
            if not user_found:
                print("There's no such person using our banking service")
        elif view == "2":
            for i in range(len(name_data)):
                user_name = name_data[i]
                user_balance = str(balance_data[i])
                print(f"User {user_name} has {user_balance}$")
        elif view == "3":
            break
        else:
            print("Invalid response")
            continue

def manager_options():
    while True:                     
        option = input("Would you like to view customers list, sir? (1 - approve)(2 - deny): ")
        if option == "1":
            while True:
                entry = input("Please enter password to approve your access: ")
                if entry == access_password:
                    search_info()
                    break
                else:
                    while True:
                        print("Password incorrect")
                        option = input("Would you like to (1 - try again)(2 - exit): ")
                        if option == "1":
                            continue
                        elif option == "2":
                            break
                        else:
                            print("Invalid response please try again")
        elif option == "2":
            break
        else:
            print("Invalid response")
            continue
                
#Didn't make main function options exactly as it is on image, since there are functions listed on image
#not actual order of options as if you picked transaction you would get more options and not instant result

def main():
    while True:
        print("Welcome to DragonBank, please pick your operation")
        operation = input("(1 - create account)(2 - log in account)(3 - exit): ")
        if operation == "1":
            create_account()
            continue
        elif operation == "2":
            key = login_account()           
            if name_data[key] in manager_data: #Made it so only managers can view entire database all user's data
                manager_options()
            else:
                if key != None:
                    command = input("Enter your action (1 - deposit)(2 - withdraw)(3 - transfer)(4 - delete account)(5 - main menu): ")
                    if command == "1":
                        deposit(key)
                    elif command == "2":
                        withdraw(key)
                    elif command == "3":
                        transfer(key)
                    elif command == "4":
                        delete_account(key)
                    elif command == "5":
                        break
                    else:
                        print("Invalid response")
                        continue
                else:
                    continue
        elif operation == "3":
            print("Thanks for using our service")
            quit()
        else:
            print("Invalid response")

main()
