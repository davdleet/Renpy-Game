import time
from math import factorial
number = int(input('find the factorial of: '))
start = time.time()
print(factorial(number))
end = time.time()
print('Calculation took %d seconds' % (end - start))