num = int(input("분자를 입력하시오: "))
den = int(input("분모를 입력하시오: "))
print('=' * 30)
result = num / den
left = num % den
print('나눗셈의 몫:', result)
print('나눗셈의 나머지:', left)
