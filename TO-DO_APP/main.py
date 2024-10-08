def get_todos():
    with open('todos.txt', 'r') as file:
        todos_local = file.readlines()
    return todos_local


while True:
    user_action = input("Type 'add...', 'edit', 'complete', 'show' or 'exit': ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + "\n")

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item.title()}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()
            new_todo = input("Enter edited TODO item: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            todos.remove(todos[number - 1])

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        except IndexError:
            print("There is no item with provided number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("You have provided incorrect command!")

print("Exiting the TODO app. Goodbye!")
