def myprint():
    print('''
    -------------------------------
            Korea University
    -------------------------------''')


def cal_func(v1, v2):
    sum = v1 + v2
    mul = v1 * v2
    sub = v1 - v2
    return sum, mul, sub


a = int(input('첫번째 수를 입력하시오: '))
b = int(input('두번째 수를 입력하시오: '))
result_sum, result_mul, result_sub = cal_func(a, b)
result = result_sum, result_mul, result_sub
print(result)
