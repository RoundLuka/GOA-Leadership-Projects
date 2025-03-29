-- To-Do List Program - Using a txt file for data storage

-- Function to return all task lines from the tasks file
function load_tasks(file_name)
    local file = io.open(file_name, "r") -- Open file in read mode
    if not file then
        return {} -- Return empty table if file doesn't exist
    end
    
    local tasks = {}
    for line in file:lines() do
        table.insert(tasks, line) -- Insert each line into the tasks table
    end
    file:close()
    return tasks
end

-- Function to save given tasks in a file
function save_tasks(file_name, tasks)
    local file = io.open(file_name, "w") -- Open file in write mode
    for _, task in ipairs(tasks) do
        file:write(task .. "\n") -- Write each task on a new line
    end
    file:close()
end

function main()
    local file_name = "tasks.txt" -- File to store tasks
    local tasks = load_tasks(file_name) -- Load tasks previously stored in file

    while true do
        -- Displaying to-do list with current tasks
        print("\nTo-Do List:")
        for i, task in ipairs(tasks) do
            print(i .. ". " .. task)
        end

        -- Menu options
        print("\nOptions:")
        print("1 - Add new task")
        print("2 - Remove task")
        print("3 - Exit")
        
        -- User choice
        io.write("Choose option: ")
        local choice = io.read()

        if choice == "1" then -- Add new task
            io.write("Enter new task: ")
            local new_task = io.read()
            table.insert(tasks, new_task)
        
        elseif choice == "2" then -- Remove task
            io.write("Enter task number to delete: ")
            local index = tonumber(io.read())
            if index and index > 0 and index <= #tasks then
                table.remove(tasks, index)
            else
                print("Invalid task number")
            end
        
        elseif choice == "3" then -- Exit the program
            save_tasks(file_name, tasks) -- Save all tasks before exiting
            print("Saved tasks, Good luck!")
            break
        else
            print("Invalid option, please try again")
        end
    end
end

-- Running the program
main()
