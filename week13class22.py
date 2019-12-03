#1차원 데이터는 series, 그 이상은 dataframe
import pandas as pd

data = {'name': ['홍길동', '이몽룡', '김철수', 'James', 'John'],
        'ID': [2017123, 2016312, 2014321, 2016332, 2019654],
        'Score': [77, 88, 99, 76, 78]}
data_frame = pd.DataFrame(data)
print(data_frame)
