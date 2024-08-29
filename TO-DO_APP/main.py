todos = []

while True:
    user_action = input("Type 'add', 'show', 'edit' or 'exit': ")

    match user_action:

        case "add":
            todo = input("Enter a TODO item: ")
            todos.append(todo)

        case "show" | "display":  # it is 'or' operator
            for item in todos:
                print(item.title())

        case "edit":
            number = int(input("Number of the TODO to edit: "))
            print(todos[number-1])
            new_todo = input("Enter edited TODO item: ")
            todos[number - 1] = new_todo

        case "exit":
            break

        case _:
            print("Hey, you entered unknown command. Try again!")

print("Bye")
