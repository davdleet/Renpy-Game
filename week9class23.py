# 지역변수와 전역변수
def house1():
    print(a)


def house2():
    global a
    a = 30
    print(a)


a = 10
house1()
house2()
print(a)
