def cal_func(*args):
    sum = 0
    mul = 1
    for i in args:
        sum += i
        mul *= i
    return sum, mul


print(cal_func(10, 20, 34, 67, 78))
