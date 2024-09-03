while True:
    user_action = input("Type 'add...', 'edit', 'complete', 'show' or 'exit': ")
    user_action = user_action.strip()

    if "add" in user_action:
        # todo = input("Enter a TODO item: ") + "\n"
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1}. {item.title()}")

    elif "edit" in user_action:
        number = int(user_action[5:])
        number = number - 1
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter edited TODO item: ")
        todos[number] = new_todo + '\n'
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif "complete" in user_action:
        number = int(user_action[9:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.remove(todos[number - 1])
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif "exit" in user_action:
        break

    else:
        print("You have provided incorrect command!")

print("Exiting the TODO app. Goodbye!")
