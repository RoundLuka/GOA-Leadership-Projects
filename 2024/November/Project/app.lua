local board = {
    {" "," "," "},
    {" "," "," "},
    {" "," "," "}
}

local function displayBoard()
    for i = 1, 3 do
        local row = ""
        for j = 1, 3 do
            row = row .. board[i][j] .. (j < 3 and " | " or "") 
        end
        print(row)
        if i < 3 then 
            print("---------") 
        end
    end
end

local function checkWinner()
    -- -- checking winner logic, looking for rows, columns and diagonals for same element
    for i = 1, 3 do
        if board[i][1] ~= " " and board[i][1] == board[i][2] and board[i][2] == board[i][3] then
            return board[i][1]
        end
        if board[1][i] ~= " " and board[1][i] == board[2][i] and board[2][i] == board[3][i] then
            return board[1][i]
        end
    end
    if board[1][1] ~= " " and board[1][1] == board[2][2] and board[2][2] == board[3][3] then
        return board[1][1]
    end
    if board[1][3] ~= " " and board[1][3] == board[2][2] and board[2][2] == board[3][1] then
        return board[1][3]
    end
    return nil -- returns nil if no winner
end

-- main loop game

local function gameLoop()
    local currentMove = "X"
    for turn = 1,9 do
        displayBoard()
        print(currentMove .. "`s move, Enter row and column (1-3): ")
        local row, col = io.read("*n", "*n")
        -- checking input
        if row >= 1 and row <= 3 and col >= 1 and col <= 3 and board[row][col] == " " then
            board[row][col] = currentMove
        else
            print("Invalid move, try again")
            turn = turn - 1 -- Subtract 1 to redo this turn
        end

        local winner = checkWinner()
        if winner then
            displayBoard()
            print(winner .. "won!")
            return
        end
        -- logic to switch turns
        if currentMove == "X" then
            currentMove = "O"
        else
            currentMove = "X"
        end
    end
    print("Draw")
end

gameLoop()