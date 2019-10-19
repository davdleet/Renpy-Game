fee = 1000
rate1 = 0
rate2 = 0.25
rate3 = 0.5
rate4 = 1
age = int(input('나이를 입력해 주세요: '))
if age >= 65 or age <= 3:
    fee = fee - (fee * rate4)
elif 4 <= age <= 13:
    fee = fee - fee * rate3
elif 14 <= age <= 19:
    fee = fee - fee *rate2
print('요금은 %d원 입니다' % fee)
