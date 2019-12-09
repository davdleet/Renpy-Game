from konlpy.tag import Okt
from collections import Counter
import pytagcloud
import random

t = Okt()
f = open('frozen2_comments.txt', 'r', encoding='utf-8')
read_lines = f.readlines()
nouns_list = []
tags_list = []
remove_list = ['편', '점', '좀', '애', '것', '더', '상미', '볼', '보고', '저']
for i in read_lines:
    for noun in t.nouns(i):
        if noun in remove_list:
            pass
        else:
            nouns_list.append(noun)
count = Counter(nouns_list)
for n, c in count.most_common(30):
    tags_list.append(
        {'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 'tag': n, 'size': 5 * c})
pytagcloud.create_tag_image(tags_list, 'wordcloud.png', fontname='my_font', size=(1280, 720))
