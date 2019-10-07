number = input('숫자를 입력하시오 > ')
lastdigit = number[-1]
if lastdigit == '2' or lastdigit == '3' or lastdigit == '5' or lastdigit == '7':
    print('%s의 끝자리 "%s"는 소수(prime number)입니다' % (number, lastdigit))
else:
    print('입력된 값은 %s입니다' % number)
