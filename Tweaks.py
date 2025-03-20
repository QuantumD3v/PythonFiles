import time as t
import random

def random_ascii():
    result = ''.join(chr(random.randint(33, 126)) for _ in range(50))
    return result

for i in range(0, 201):
    print('Hello, World! - ' + str(i) + ' - ' + random_ascii())
    t.sleep(0.02)