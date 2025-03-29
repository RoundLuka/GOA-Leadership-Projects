local function load_accounts(file_name)
    local accounts = {}
    local file = io.open(file_name, "r")
    if file then
        for line in file:lines() do
            local name, password, balance = line:match("(%S+) (%S+) (%d+)")
            if name and password and balance then
                table.insert(accounts, {name = name, password = password, balance = tonumber(balance)})
            end
        end
        file:close()
    end
    return accounts
end

local function save_accounts(file_name, accounts)
    local file = io.open(file_name, "w")
    for _, acc in ipairs(accounts) do
        file:write(acc.name .. " " .. acc.password .. " " .. acc.balance .. "\n")
    end
    file:close()
end

local function register(accounts)
    while true do
        io.write("Enter your name: ")
        local name = io.read()
        for _, acc in ipairs(accounts) do
            if acc.name == name then
                print("Account already exists")
                goto continue
            end
        end
        
        io.write("Enter your password: ")
        local password = io.read()
        while #password < 8 do
            print("Password must be at least 8 characters long")
            io.write("Enter your password: ")
            password = io.read()
        end
        
        table.insert(accounts, {name = name, password = password, balance = 0})
        print("Account created successfully")
        break
        ::continue::
    end
end

local function login(accounts)
    io.write("Enter your name: ")
    local name = io.read()
    io.write("Enter your password: ")
    local password = io.read()

    for index, acc in ipairs(accounts) do
        if acc.name == name and acc.password == password then
            print("Login successful")
            return index
        end
    end
    print("Invalid name or password")
    return nil
end

local function deposit(accounts, key)
    io.write("Enter deposit amount: ")
    local amount = tonumber(io.read())
    if amount and amount > 0 then
        accounts[key].balance = accounts[key].balance + amount
        print("Deposited " .. amount .. " to your balance")
    else
        print("Invalid amount")
    end
end

local function withdraw(accounts, key)
    io.write("Enter withdraw amount: ")
    local amount = tonumber(io.read())
    if amount and amount > 0 and amount <= accounts[key].balance then
        accounts[key].balance = accounts[key].balance - amount
        print("Withdrew " .. amount .. " from your balance")
    else
        print("Invalid amount or not enough balance")
    end
end

local function transfer(accounts, key)
    io.write("Enter recipient name: ")
    local recipient_name = io.read()
    local recipient = nil
    
    for index, acc in ipairs(accounts) do
        if acc.name == recipient_name then
            recipient = index
            break
        end
    end
    
    if not recipient then
        print("Recipient not found")
        return
    end
    
    io.write("Enter transfer amount: ")
    local amount = tonumber(io.read())
    if amount and amount > 0 and amount <= accounts[key].balance then
        accounts[key].balance = accounts[key].balance - amount
        accounts[recipient].balance = accounts[recipient].balance + amount
        print("Transferred " .. amount .. " to " .. recipient_name)
    else
        print("Invalid amount or insufficient balance")
    end
end

local function main()
    local file_name = "accounts.txt"
    local accounts = load_accounts(file_name)
    
    while true do
        print("\nWelcome to GreenHill Bank!")
        print("1 - Register")
        print("2 - Login")
        print("3 - Exit")
        io.write("Choose an option: ")
        local choice = io.read()
        
        if choice == "1" then
            register(accounts)
        elseif choice == "2" then
            local key = login(accounts)
            if key then
                while true do
                    print("\n1 - Deposit")
                    print("2 - Withdraw")
                    print("3 - Transfer")
                    print("4 - Logout")
                    io.write("Choose an action: ")
                    local action = io.read()
                    
                    if action == "1" then
                        deposit(accounts, key)
                    elseif action == "2" then
                        withdraw(accounts, key)
                    elseif action == "3" then
                        transfer(accounts, key)
                    elseif action == "4" then
                        break
                    else
                        print("Invalid action")
                    end
                end
            end
        elseif choice == "3" then
            save_accounts(file_name, accounts)
            print("Goodbye!")
            break
        else
            print("Invalid option")
        end
    end
end

main()
