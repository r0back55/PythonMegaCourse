while True:
    user_action = input("Type 'add', 'edit', 'complete', 'show' or 'exit': ")

    match user_action:
        case "add":
            todo = input("Enter a TODO item: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index+1}. {item.title()}")

        case "edit":
            number = int(input("Number of the TODO to edit: "))
            number = number - 1
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter edited TODO item: ")
            todos[number] = new_todo + '\n'
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "complete":
            number = int(input("Item number to remove: "))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.remove(todos[number - 1])
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "exit":
            break

        case _:
            print("Hey, you have entered unknown command. Try again!")

print("Exiting the TODO app. Goodbye!")
