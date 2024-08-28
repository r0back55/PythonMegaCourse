todos = []

while True:
    user_action = input("Type 'add' or 'show', or 'exit': ")

    match user_action:
        case "add":
            todo = input("Enter a TODO item: ")
            todos.append(todo)
        case "show" | "display":  # it is 'or' operator
            for item in todos:
                print(item.title())
        case "exit":
            break
        case _:
            print("Hey, you entered unknown command. Try again!")

print("Bye")
