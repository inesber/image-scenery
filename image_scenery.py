import random


def create(cols, rows):
    data = ["a", "b", "c", "d", "e", "f"]

    print(f"Generate a landscape which is {cols} by {rows}")

    for row in range(rows):
        row_string = ""

        for col in range(cols):
            r = random.choice(data)
            row_string += r

        print(row_string)

    print("Finished generating landscape")


create(5, 5)
