import random

a = random.randint(1, 10)
b = random.randint(1, 10)
c = int(input('%d + %d = ' % (a, b)))
if c == (a + b):
    print('good job')
else:
    print('wrong answer')
