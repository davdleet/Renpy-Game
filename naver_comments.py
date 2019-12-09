from bs4 import BeautifulSoup
from urllib.request import urlopen
comment_list = []
for i in range(1,20):
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=136873&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page='+str(i)
    url_open = urlopen(url)
    html = BeautifulSoup(url_open, 'html.parser')
    for i in range(1,10):
        comment = html.find('span', id='_filtered_ment_'+str(i)).text
        comment_list.append(comment.strip())
f = open('frozen2_comments.txt', 'w', encoding= 'utf-8')
for i in comment_list:
    f.write(i+'\n')
f.close()