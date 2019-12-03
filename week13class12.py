# 파일을 읽고 단어 통계 구하기
f = open('memo2.txt', 'r', encoding='UTF-8')
book = f.read()
word_text = book.split(' ')
line_text = book.split('\n')
print('전체 단어수:', book.count(' ') + book.count('\n') + 1)
print('전체 라인 수:', book.count('\n'))
f.close()