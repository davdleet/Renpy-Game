age = int(input("나이가 어떻게 되시나요? "))
future = age - (age % 10) + 10
print("흠.. %d을 바라 보시는군요" % future)
