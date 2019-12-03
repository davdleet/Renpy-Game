#한글을 쓸때는 UTF-8 인코딩이라는 것을 알려줘야 함
#읽을때는 'r', 쓸때는 'w', 추가할때 'a'
text = input('메모에 저장할 내용을 입력하세요: ') + '\n'
f = open('memo2.txt', 'a', encoding ='UTF-8')
f.write(text)
f.close()
#book = f.read()
#print(book)
#f.close()