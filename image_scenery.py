import random

from termcolor import colored
from noise import pnoise2


def create(cols=10, rows=10):
    data = ["!", ".", "#", "&", "-", "$", "-", "&", "#", ".", "!"]
    seed = random.randint(0, 100)
    field = ""

    print(f"Generate a landscape which is {cols} by {rows}")

    for row in range(rows):
        for col in range(cols):
            n = pnoise2(row / rows, col / cols, base=seed)
            n *= 100
            n = round(n)
            n = n % len(data)

            field += data[n]
        field += "\n"

    print("Finished generating landscape")
    return field


def check_number(question):
    tries = 0

    while tries < 3:
        answer = input(colored(question + "\n", "blue"))

        if answer == "quit":
            quit()
        elif answer.isnumeric():
            return int(answer)
        else:
            print(colored("Make sure to type a number", "yellow"))
            tries += 1

    print(colored("Please come back when you have a number to type...", "red"))
    quit()


cols = check_number("How many columns?")
rows = check_number("How many rows?")

output = create(cols, rows)

print(output)
