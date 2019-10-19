number = input("Please input any number: ")
print(number[-1])
if number[-1] == '0':
    print('%c은 짝수입니다' % number)
else:
    print('%c은 홀수입니다.' % number)