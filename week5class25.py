fee = 1000
discount = 0.75
age = int(input('나이를 입력해 수세요: '))
if age < 20:
    fee *= discount
    print('요금은 %d원 입니다' % fee)
else:
    print('요금은 %d원 입니다' % fee)