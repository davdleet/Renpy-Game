fee = 1000
rate1 = 0.25
rate2 = 0.5
rate3 = 1
age = int(input('나이를 입력하시오: '))
if age <= 3 or age >= 65:
    fee = fee - (fee * rate3)
elif 4 <= age <= 13:
    fee = fee - (fee * rate2)
elif 14 <= age <= 19:
    fee = fee - (fee * rate1)
print('버스 요금은: %d원 입니다.' % fee)