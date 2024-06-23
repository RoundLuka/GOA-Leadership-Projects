"""Create basic slot machine with 3 rows and columns"""

#add set goal
#can add customization for slot machine for customer to pick what each symbol ratio is how many rows cols and symbols will be 
#have to add spin system


import random

rows = 3
cols = 3
symbols = "$#@"

max_bet = 1000
#determines how much is paid for winning certain symbol, (filling row with same symbol) multiplication table.
symbol_ratio = {
    "$": 5,
    "#": 4,
    "@": 3
}  


#in the end what player lost (loss) or won (profit)
worth = 0


def deposit():
    while True:
        amount = input("Enter amount to deposit: $")
        if amount.isdigit():
            if int(amount) > 0:
                amount = int(amount)
                return amount
            else:
                print("Please enter valid amount")
        else:
            print("Please enter amount in numbers")


#can add setup function here to create custom multipliers for each symbol



def bet(amount):
    while True:
        bet_amount = input("Enter bet amount: $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if bet_amount > 0 and bet_amount <= amount and bet_amount <= max_bet:
                bet_amount = int(bet_amount)
                return bet_amount
            else:
                print("Please enter valid amount")
        else:
            print("Please enter amount in numbers")

def keep_playing(amount):
    while True:
        option = input("Would you like to keep playing(spin) or quit(quit)? ")
        if option == "spin":
            break
        elif option == "quit":
            print("Quitting slot machine, good day")
            total = worth + amount
            if total > 0:
                print(f"Your total win is {total}")
            else:
                print(f"Your total loss is {total}")
            quit()
        else:
            print("Invalid response please try again")


def slot_machine(rows,cols,symbols):
    result = []
    for r in range(rows):
        row = []
        for c in range(cols):
            roll = random.randint(0,2)
            symbol = symbols[roll]
            row.append(symbol)
        result.append(row)
        #Slots visualisation
        slots = ""

        for row in (result):
            slots += "".join(row) + "\n" 
    print(slots)
    #
    return result


def check_win(result,bet_amount):
    win_amount = 0
    for row in result:
        win_symbol = row[0]
        for symbol in row:
            if win_symbol != symbol:
                break
        else:
            win_amount += symbol_ratio[win_symbol] * bet_amount
    return win_amount
#if there are two rows with same ratio win aka same symbol win should be squared
#have to add this

def option_handle(amount):
    while True:
        option = input("Would you like to deposit(1) more or quit(2)? ")
        if option.isdigit():
            if int(option) == 1:
                print("Response recorded successfully.")
                return deposit()
            elif int(option) == 2:
                print("Quitting slot machine, good day")
                total = worth + amount
                if total > 0:
                    print(f"Your total win is {total}")
                else:
                    print(f"Your total loss is {total}")
                    quit()
            else:
                print("Invalid response please try again")
        else:
            print("Please enter number")

#had main code in while amount > 0: conditon but as option handle function now handles if customer wants to quit it isn't necessary
#as user can deposit again if they want to


def main():
    global worth
    print("You arrive at slot machine to start gambling, first you have to make deposit, when you place bet slot machine will spin")
    amount = deposit()
    worth -= amount
    while True:
        print(f"Current balance: ${amount}")
        keep_playing(amount)
        bet_amount = bet(amount)
        amount -= bet_amount
        result = slot_machine(rows,cols,symbols)
        win_amount = check_win(result,bet_amount)
        amount += win_amount
        if win_amount > 0:
            print(f"You won ${win_amount}!")
        else:
            print("You didn't win this time.")
        if amount <= 0:
            print("You have run out of money!")
            amount = option_handle(amount)
            worth -= amount
                            
main()
