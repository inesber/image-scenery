import random


def create(cols=10, rows=10):
    data = ["a", "b", "c", "d", "e", "f"]

    print(f"Generate a landscape which is {cols} by {rows}")

    for row in range(rows):
        row_string = ""

        for col in range(cols):
            r = random.choice(data)
            row_string += r

        print(row_string)

    print("Finished generating landscape")


def check_number(question):
    tries = 0

    while tries < 3:
        answer = input(question + "\n")

        if answer == "quit":
            quit()
        elif answer.isnumeric():
            return int(answer)
        else:
            print("Make sure to type a number")
            tries += 1

    print("Please come back when you have a number to type...")
    quit()


cols = check_number("How many columns?")
rows = check_number("How many rows?")

create(cols, rows)
