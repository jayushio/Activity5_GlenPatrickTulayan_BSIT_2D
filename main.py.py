from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def run_menu():
    while True:
        print("\nSTACKS AND QUEUES")
        print("1. Array Stack")
        print("2. Linked Stack")
        print("3. Array Queue")
        print("4. Linked Queue")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "5":
            print("Program ended.")
            break

        if choice == "1":
            structure = ArrayStack(5)
            kind = "stack"
        elif choice == "2":
            structure = LinkedStack()
            kind = "stack"
        elif choice == "3":
            structure = ArrayQueue(5)
            kind = "queue"
        elif choice == "4":
            structure = LinkedQueue()
            kind = "queue"
        else:
            print("Invalid choice.")
            continue

        while True:
            print("\nCurrent structure:", structure)

            if kind == "stack":
                print("1. Push")
                print("2. Pop")
                print("3. Peek")
            else:
                print("1. Enqueue")
                print("2. Dequeue")
                print("3. Peek Front")

            print("4. Back to Main Menu")
            operation = input("Choose operation: ")

            if operation == "4":
                break

            try:
                if operation == "1":
                    value = input("Enter value: ")
                    if kind == "stack":
                        structure.push(value)
                    else:
                        structure.enqueue(value)
                    print("Value added.")

                elif operation == "2":
                    if kind == "stack":
                        print("Removed:", structure.pop())
                    else:
                        print("Removed:", structure.dequeue())

                elif operation == "3":
                    if kind == "stack":
                        print("Top:", structure.peek())
                    else:
                        print("Front:", structure.peek_front())

                else:
                    print("Invalid operation.")
                    continue

                print("Updated structure:", structure)

            except (IndexError, OverflowError) as error:
                print("Error:", error)


if __name__ == "__main__":
    run_menu()
