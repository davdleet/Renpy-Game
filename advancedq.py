import time
import random

start = time.time()
range = 10
x = 1
while x:
    now = time.time()
    a = random.randint(1, range)
    b = random.randint(1, range)
    if (now - start) >= 10:
        range = 100
    c = int(input('%d + %d = ' % (a, b)))
    if c == (a + b):
        print('good job')
    elif c == 0:
        break
    else:
        print('try another question')
