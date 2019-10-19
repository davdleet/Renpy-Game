list1 = [1, 3, '홍길동', '유관순', '이도령', '홍길동']
list = [1, 2, 3, 4, 5]
str = 'korea'
sum = 0
for i in str:
    print(i)
for i in list:
    sum = sum + i
print(sum)
for i in ['홍길동', '유관순']:  # list1에서 '홍길동', '유관순' 찾기
    if i in list1:
        print(i)
