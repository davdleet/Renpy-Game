a = int(input('1번째 값: '))
b = int(input('2번째 값: '))
c = int(input('3번째 값: '))
maxValue = a if a > b else b
if c > maxValue:
    maxValue = c
print('최대 값은 %s 입니다' % maxValue)
