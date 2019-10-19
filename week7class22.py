number = int(input('출력할 단을 입력하시오: '))
for i in range(9, 0, -1):  #구구단 거꾸로 하기
    print('%d * %d = %d' % (number, i, number * i))
dan = int(input('출력할 단을 입력 하세요: ')) + 1
for i in range(2, dan):
    for j in range(1,10):
        print('%d * %d = %d' % (i, j, i*j))
    print('*' * 10)