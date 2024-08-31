while True:
    user_action = input("Type 'add', 'edit', 'complete', 'show' or 'exit': ")

    match user_action:
        case "add":
            todo = input("Enter a TODO item: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case "show":
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip("\n") for item in todos]

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index+1}. {item.title()}")

        case "edit":
            number = int(input("Number of the TODO to edit: "))
            print(todos[number-1])
            new_todo = input("Enter edited TODO item: ")
            todos[number - 1] = new_todo

        case "complete":
            r_item = int(input("Item number to remove: "))
            todos.remove(todos[r_item-1])

        case "exit":
            break

        case _:
            print("Hey, you have entered unknown command. Try again!")

print("Bye")
