from image_scenery import create
import os

os.makedirs("outputs", exist_ok=True)

noise_levels = [10, 20, 50, 100, 250, 500]

for nl in noise_levels:
    output = create(100, 100, nl)

    filename = os.path.join("outputs", f"pattern-{nl}.txt")

    with open(filename, "w") as f:
        f.write(output)
