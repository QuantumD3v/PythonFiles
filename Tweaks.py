import time as t
import random
import os

def random_ascii():
    return ''.join(chr(random.randint(33, 126)) for _ in range(50))

filename = "random_output.txt"

for i in range(201):
    line = f"Hello, World! - {i} - {random_ascii()}\n"
    print(line, end="")

    with open(filename, "a") as file:
        file.write(line)

    t.sleep(0.02)
