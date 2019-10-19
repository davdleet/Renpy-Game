# num 리스트에서 100보다 작은 수 더하기
num = [123, 7, 2933, 22, 55, 37]
sum = 0
for i in num:
    if i < 100:
        sum += i
print(sum)