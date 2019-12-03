import random

products = ['물티슈', '휴대폰고리', '스타벅스 쿠폰', '문화상품권 5만원', '아이패드']
luckybox = random.choices(products, weights=[60, 30, 5, 3, 2], k = 1)
print('축하합니다. %s에 당첨되셨습니다.' % luckybox[0])
