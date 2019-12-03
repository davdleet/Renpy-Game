import requests
import pandas
def get_everycoding_stock():
    url = 'https://everycoding.net/static/upload/tutor/image/value_investment/sample_site.html'
    site = requests.get(url)
    html_text = site.text

    tables = pandas.read_html(html_text)

    everycoding_stock = tables[1].values
    eps = (everycoding_stock[2][1])
    per = (everycoding_stock[3][1])
    price = float(eps) * float(per)
    return price
get_everycoding_stock()