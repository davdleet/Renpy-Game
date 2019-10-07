name = input('이름을 입력하시오: ')
korean = int(input('국어점수: '))
math = int(input('수학점수: '))
english = int(input('영어 점수: '))
average = (korean + math + english)/3
print('%s 학생의 평균성적: %0.2f' % (name, average))