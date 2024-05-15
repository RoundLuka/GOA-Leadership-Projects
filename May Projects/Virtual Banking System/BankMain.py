"""Create banking system with account creation switching money depsoit withdrawal and transactions"""
#Bank name GreenHill Bank
#might add their starting money and if they run out of it they can't deposit again
#also might import random to generate random tokens for users more safety
#have to optimize this code further more so code doesn't gets ended becasue of errors

#for optimization might think of class to simplify code for e.g BankAccount class

#this code consists of functions performing different tasks collecting neccecary information in
#database which includes 3 lists users,their passwords and balance


#might improve security by adding pin codes but i'll make code more messy

#will have to make in future so accounts with same names can't be created so that
#it doesn't casue confusion in program transfer function
#might create certain codes for failed operations

#database
name_data = ["luka"]
pass_data = ["luka1234"]
balance_data = [500]


def register():
    while True:
        check = input("Would you like to go back(1) or continue(anything else): ")
        if check == "1":
            break
        
        name = input("Enter your name: ")
        while name in name_data:
            print("Account with same name already exists")
            name = input("Enter your name: ")
        password = input("Enter your password: ")
        while len(password) < 8:
            print("Password should at least contain 8 characters")
            password = input("Enter your password: ")
        confrim = input("Confrim password: ")
        while password != confrim:
            stop = (input("enter (1) if forgot password else(anything) else: "))
            if stop == "1":
                continue
            print("Your confrimed password doesn't match with original.Try again: ")
            confrim = input("Confrim password: ")
        name_data.append(name)
        pass_data.append(password)
        balance_data.append(0)
        print("Account successfully created thanks for using GreenHill Bank")
        print("Operation successful feel free to continue using our service")
        break
def login():
    while True:
        check = (input("Would you like to go back(1) or continue(anything else): "))
        if check == "1":
            return False


        name = input("Enter your name: ")
        password = input("Enter your passowrd: ")
        for i in range(len(name_data)):
            if name == name_data[i] and password == pass_data[i]:
                print("You have successfully logged in your account")
                print("Operation successful thanks for using GreenHill Bank service")
                key = i #key to access balance, to know which balance belongs to account
                login_successful = True
                return key 
            else:
                print("Operation failed:")                              #if login wasn't successful user gets redirected to main menu
                print("Authorization failed inccoret name or password please try again redirecting you to main menu") 
                

def deposit(key):
    print("Dear user you are now in your account of GH Bank (deposit)")
    deposit_amount = input("Enter how much $ you would like to deposit: ")
    if deposit_amount.isdigit():
        if int(deposit_amount) > 0: #could have created manual isdigit might as well in future using it as i know how to write it
            balance_data[key] = balance_data[key] + int(deposit_amount)
            print(f"Operation successful deposited {deposit_amount} $ to your account")
        else:
            print("Operation failed: invalid amount. you'll get redirected to main menu")
    else:
         print("Operation failed: invalid amount. you'll get redirected to main menu")
    

def withdraw(key):
    print("Dear user you are now in your account of GH Bank (withdraw)")
    print("Your balance is",balance_data[key])
    withdraw_amount = input("Enter how much $ you would like to withdraw: ")
    if withdraw_amount.isdigit():
        if int(withdraw_amount) > 0 and int(withdraw_amount) <= balance_data[key]: 
            balance_data[key] -= int(withdraw_amount)
            print(f"You have successfully withdrawn {withdraw_amount}$  from your bank account")
        else:
            print("Operation failed: invalid amount. you'll get redirected to main menu")
    else:
         print("Operation failed: invalid amount. you'll get redirected to main menu")
def transfer(key):
    print("Dear user you are now in your account of GH Bank (transfer)")
    print("Your balance is",str(balance_data[key]),"$")
    recipient = input("Enter your recipient(to whom you're transfering $): ")
    recipient_found = False
    for i in range(len(name_data)):
        if recipient == name_data[i]:
            recipient_key = i
            recipient_found = True
            break
    if recipient_found:
        print("Recipient found keep in mind you can't trasnfer $ that is over your balance")
        print("Your balance is",balance_data[key],"$")
        print("Warning: make sure you enter positive number as well or your operation will fail")
        transfer_amount = input("Enter how much $ you would like to transfer: ")
        if transfer_amount.isdigit():
            if int(transfer_amount) > 0 and int(transfer_amount) <= balance_data[key]:
                balance_data[key] -= int(transfer_amount)
                balance_data[recipient_key] += int(transfer_amount)
                print(f"{transfer_amount}$ was charged from your account and sent to {recipient}")
                print(f"Operation successful: {transfer_amount}$ was successfully transfered to {recipient}")
            else:
                print("Operation failed: invalid amount. you'll get redirected to main menu")
    else:
        print("Operation failed: recipient not found you'll get redirected back")


    
def main():
    while True:
        print("Welcome to GreenHill Bank paybox what would you like to do? ")
        action = (input("Pick Operation (1-create account)(2-log in account)(3-exit): ")) #main menu
        if action == "1":
            register()
            continue
        elif action == "2":
            while True:
                key = login()       #this key will be equal to what is key in login which will be found by checking data with for loop index for user
                if key is not None: #if key wasn't found then login was not successful and and while loop will rerun
                    operation = (input("Enter operation (1-Deposit)(2-Withdraw)(3-Transfer)(4-Exit Go back to main menu): ")) #inner menu for operations
                    if operation == "1":
                        deposit(key)
                    elif operation == "2":
                        withdraw(key)
                    elif operation == "3":
                        transfer(key)
                    elif operation == "4":
                        break #Exiting inner loop going back to main menu added this option if they wanted to pick any of these operations again
            else:
                continue


        elif action == "3":
            quit() #quit and break does same in this case if i were to close this loop program would have stopped running since its just this while loop
        else:
            print("Operation failed:")
            print("Invalid input please try again")


main()
