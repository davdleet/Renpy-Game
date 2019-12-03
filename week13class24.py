import requests
import pandas
def find_price(companyCode):
    url = 'https://media.kisline.com/highlight/mainHighlight.nice?paper_stock='+str(companyCode)+'&nav=1'
    html = requests.get(url)
    tables = pandas.read_html(html.text)
    financialSummary=tables[6].values
    # 5. PER 값을 가져옵니다.
    per = float(financialSummary[10][4])
    # 6. EPS 값을 가져옵니다.
    eps = float(financialSummary[13][4])
    fair_price = per * eps
    print(fair_price)
input_code = input('회사코드를 입력하세요:')
find_price(input_code)