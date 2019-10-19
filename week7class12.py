cities = ['서울', '대구', '대전', '부산', '광주']
print(cities[0:2])  # 서울,대구
print(cities[::2])  # 두개씩 건너뛰기 서울, 대전, 광주
print(cities[::-1])  # 뒤에서부터 하나씩 보기 광주, 부산, 대구, 대전
print(cities[0:3:2])  # 0:3 범위 내에서 두개씩 건너뛰기
str = 'koreauniversity'
print(str[::2])
cities = cities + ['인천']  # 추가할때
print(cities)
cities.append('전주')  # 추가할때
print(cities)
cities[5] = '김포'  # 수정할때
print(cities)
cities.extend(['인천', '울산'])  # 리스트를 통째로 추가
cities.remove('부산')  # 리스트에서 하나의 객체 지움
del cities[0:3] # 여러개 지울 때
cities.insert(1, '포항') # 중간에 추가할 때
