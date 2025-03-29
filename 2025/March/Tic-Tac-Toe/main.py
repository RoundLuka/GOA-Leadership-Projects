board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def displayBoard():
    for i in range(3):
        row = ""
        for j in range(3):
            if j < 2:
                row += board[i][j] + " | "
            else:
                row += board[i][j]
        print(row)
        if i < 2:
            print("---------")

def checkWinner():
    # -- checking winner logic, looking for rows, columns and diagonals for same element
    for i in range(3):
        if board[i][0] != " " and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] != " " and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] != " " and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != " " and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    return None  # returns None if no winner

# main loop game
def gameLoop():
    currentMove = "X"
    for turn in range(9):
        displayBoard()
        
        print(currentMove + "`s move, Enter row (1-3): ")
        row = int(input())  
        
        print(currentMove + "`s move, Enter column (1-3): ")
        col = int(input())  
        
        # checking input
        if row >= 1 and row <= 3 and col >= 1 and col <= 3 and board[row-1][col-1] == " ":
            board[row-1][col-1] = currentMove
        else:
            print("Invalid move, try again")
            turn -= 1  # Subtract 1 to redo this turn

        winner = checkWinner()
        if winner:
            displayBoard()
            print(winner + " won!")
            return
        # logic to switch turns
        if currentMove == "X":
            currentMove = "O"
        else:
            currentMove = "X"
    print("Draw")

gameLoop()
