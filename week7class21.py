str = '*'
sum = 0
sum1 = 0
for i in range(1, 101):   #단순히 몇번 반복하고 싶을때는 range 활용
    sum += i
print('%d까지의 합은 %d' % (i, sum))
for i in range(0, 11, 2):   #2개씩 스킵하면서 더하기 거꾸로 할때는 마이너스
    sum1 += i
print(sum1)