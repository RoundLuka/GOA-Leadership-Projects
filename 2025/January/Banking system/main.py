def load_accounts(file_name):
    # Function to load accounts from file
    accounts = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 3:
                    name, password, balance = parts
                    accounts.append((name, password, int(balance)))
    except FileNotFoundError:
        pass # if file wasn't found return empty list
    return accounts


def save_accounts(file_name, accounts):
    # save given accounts to given file
    with open(file_name, "w") as file:
        for name, password, balance in accounts:
            file.write(f"{name} {password} {balance}\n") # each account gets 1 line

def register(accounts):
    # creating new account
    while True:
        name = input("Enter your name: ")
        
        for account in accounts:
            if account[0] == name:
                print("Account already exists")
                continue
        
        password = input("Enter your password: ")
        while len(password) < 8:
            print("Password must be at least 8 characters long")
            password = input("Enter your password: ")
        
        balance = 0 # starting balance 
        accounts.append((name, password, balance)) # adding account

        print("Account created successfuly")
        break

def login(accounts):
    # Function to handle log in
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    for index, (acc_name, acc_pass, _) in enumerate(accounts):
        if name == acc_name and password == acc_pass:
            print("Login successful")
            return index  # returning index as key of account, to know which account is being accessed
    
    print("Invalid name or password")
    return None

def deposit(accounts, key):
    # Deposit money to account
    amount = input("Enter deposit amount: ")
    if amount.isdigit() and int(amount) > 0:
        accounts[key] = (
            accounts[key][0],
            accounts[key][1],
            accounts[key][2] + int(amount)
        )
        print(f"Deposited {amount} to your balance")
    else:
        print("Invalid amount")

         
def withdraw(accounts, key):
    # Function to handle money withdrawal
    amount = input("Enter withdraw amount: ")
    if amount.isdigit() and 0 < int(amount) <= accounts[key][2]: # checking if account has enough to withdraw
        accounts[key] = (
            accounts[key][0],
            accounts[key][1],
            accounts[key][2] - int(amount)
        )
        print(f"Withdrew {amount} from your balance")
    else:
        print("Invalid amount or not enough balance")

def transfer(accounts, key):
    # Function to transfer balance to other account
    recipient_name = input("Enter recipient name: ")
    recipient = False
    for index, account in enumerate(accounts):
        if account[0] == recipient_name:
            recipient = index

    if recipient is None:
        print("Recipient not found")
        return 

    amount = input("Enter transfer amount: ")
    if amount.isdigit() and 0 < int(amount) <= accounts[key][2]:
        accounts[key] = (
            accounts[key][0],
            accounts[key][1],
            accounts[key][2] - int(amount),
        )
        accounts[recipient] = (
            accounts[recipient][0],
            accounts[recipient][1],
            accounts[recipient][2] + int(amount),
        )

        print(f"Transfered {amount} to {recipient_name}")
    else:
        print("Invalid amount or insufficient balance")
    

def main():
    file_name = "accounts.txt"
    accounts = load_accounts(file_name) 

    while True:
        print("\nWelcome to GreenHill Bank!")
        print("1 - Register")
        print("2 - Login")
        print("3 - Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            register(accounts)
        elif choice == "2":
            key = login(accounts)
            if key is not None:
                while True:
                    print("\n1 - Deposit")
                    print("2 - Withdraw")
                    print("3 - Transfer")
                    print("4 - Logout")

                    action = input("Choose an action: ")
                    if action == "1":
                        deposit(accounts, key)
                    elif action == "2":
                        withdraw(accounts, key)
                    elif action == "3":
                        transfer(accounts, key)
                    elif action == "4":
                        break
                    else:
                        print("Invalid action")
        elif choice == "3":
            save_accounts(file_name, accounts)
            print("Goodbye!")  
            break
        else:
            print("Invalid option")          

main()