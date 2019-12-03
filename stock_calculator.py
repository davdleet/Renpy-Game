import pandas
import requests
from tkinter import *

link = None
window = None
price = None
answer = None
answer_number = None


def get_url():
    address = link.get()
    return address


def GUI_main():
    global window
    global link
    global price
    global answer_number
    global answer
    window = Tk()
    window.title('stock calculator')
    text = Label(window, text='please enter the url and press confirm')
    link = Entry(window, width=50)
    confirm_button = Button(window, text='Confirm', command=lambda: get_price())
    answer_number = StringVar()
    answer = Label(window, textvariable=answer_number)
    answer_number.set('Appropriate price: Nothing')
    text.grid(row=0, column=0)
    link.grid(row=1, column=0)
    confirm_button.grid(row=2, column=0)
    answer.grid(row=3, column=0)


def get_price():
    global price
    global answer
    global answer_number
    site = requests.get(get_url())
    html_text = site.text
    tables = pandas.read_html(html_text)
    every_coding = tables[1].values
    print(every_coding)
    price = float(every_coding[2][1]) * float(every_coding[3][1])
    answer_number.set('Appropriate price: %s' % price)


GUI_main()
window.mainloop()
