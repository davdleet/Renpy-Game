a = 0
import random
import time
start = time.time()
while a != 3:
    a = random.randint(1,10000000)
end = time.time()
print(end - start)