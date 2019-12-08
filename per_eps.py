import requests
import pandas as pd
from tkinter import *

enter_code = None
good_price = None
price_label = None


def calculate_stock():
    global enter_code
    global good_price
    try:
        company_code = enter_code.get()
        url = 'https://media.kisline.com/highlight/mainHighlight.nice?paper_stock=' + '%s' % (company_code) + '&nav=1l'
        site = requests.get(url)
        html_text = site.text
        tables = pd.read_html(html_text)
        values1 = tables[6].values
        per = values1[10][-1]
        eps = values1[13][-1]
        good_price = float(per) * float(eps)
        rounded = '%0.3f' % good_price
        price_label['text'] = '%s won' % rounded
    except:
        price_label['text'] = 'Error try another code'


def calculating(i):
    price_label['text'] = 'Calculating... please wait'


def GUI_main():
    global enter_code
    global price_label
    window = Tk()
    window.title('kisline calculator')
    window.geometry('200x100')
    window.resizable(False, False)
    enter_code = Entry(window, width=30)
    cal_button = Button(window, text='calculate', command=calculate_stock)
    guide_label = Label(window, text='Appropriate price: ')
    price_label = Label(window, text='')
    cal_button.bind('<Button-1>', calculating)
    cal_button.grid(row=1)
    enter_code.grid(row=0)
    guide_label.grid(row=2)
    price_label.grid(row=3)
    window.mainloop()


GUI_main()
