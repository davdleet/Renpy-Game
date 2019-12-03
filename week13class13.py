#딕셔너리
phone_no = {'이성원': '010-8966-8197', '김철수': '010-8294-1221'}
phone_no['이성원'] = '010-8966-8198'
print(phone_no)
print(phone_no.values())
print(phone_no.keys())
print(phone_no.items())
print('이성원' in phone_no)
print('010-8966-8198' in phone_no.values())