from konlpy.tag import Okt
from collections import Counter
okt = Okt()
f = open('frozen2_comments.txt', 'r', encoding='utf-8')
comments_list = []
nouns_list = []
analyzed = []
nouns = []
read_lines = f.readlines()
for i in read_lines:
    comments_list.append(i[0:-1])
f.close()
for i in comments_list:
    analyzed.append(okt.pos(i))
for i in analyzed:
    for word, tag in i:
        if tag in ['Noun']:
            nouns.append(word)
counted = Counter(nouns)
common = counted.most_common(30)
print(common)