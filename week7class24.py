#메뉴를 랜덤으로 정하기
import random

food = ['햄버거', '피자', '돈까스', '덮밥']
num = random.randint(1, 4)
choice = food[num]
print('선택된 메뉴는 %s입니다' % choice)
