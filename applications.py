from linked_queue import LinkedQueue


def is_balanced(expression):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for character in expression:
        if character in "([{":
            stack.append(character)
        elif character in ")]}":
            if not stack or stack[-1] != pairs[character]:
                return False
            stack.pop()

    return len(stack) == 0


def print_queue_demo():
    queue = LinkedQueue()

    queue.enqueue(("JOB101", 3))
    queue.enqueue(("JOB102", 5))
    queue.enqueue(("JOB103", 2))

    print("Waiting order:", queue)

    while not queue.is_empty():
        job_id, pages = queue.dequeue()
        print("Printing:", job_id, "-", pages, "pages")
        print("Remaining jobs:", queue)


if __name__ == "__main__":
    print("Balanced Parentheses Checker")
    print(is_balanced("({[]})"))
    print(is_balanced("([)]"))

    print("\nPrint Queue Simulation")
    print_queue_demo()
