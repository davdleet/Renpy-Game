import random

a = list(range(1,46))
tickets = int(input('how many tickets will you buy? '))
for i in range(tickets):
    b = random.sample(a, 6)
    print(b)