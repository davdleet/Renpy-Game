def all_add_function(para):
    result = 0
    for i in para:
        result += i
    return result


number = map(int, input('숫자를 입력하시오 ').split())
print(all_add_function(number))
