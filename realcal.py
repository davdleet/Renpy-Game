from tkinter import *

window = None
display_label = None
lcd = None
expression = ''


def press(num):
    global expression
    expression += num
    lcd.set(expression)


def clear():
    global expression
    global lcd
    lcd.set('0')
    expression = ''


def erase():
    global expression
    expression = expression[0:-1]
    lcd.set(expression)


def result():
    try:
        global expression

        expression = str(eval(expression))
        lcd.set(expression)
        expression = ''
    except ZeroDivisionError:
        lcd.set('Cant divide by 0')
        expression = ''
    except:
        lcd.set('Syntax error')
        expression = ''


def GUI_main():
    global window
    global display_label
    global lcd
    global expression
    window = Tk()
    window.title("Sungwon's calculator")
    window.resizable(False, False)
    lcd = StringVar()
    display_label = Label(window, textvariable=lcd, width=18, font='Arial 20', relief=SUNKEN, anchor='e')
    display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    lcd.set('0')

    btn1 = Button(window, text='1', font='arial 13', command=lambda: press('1'), width=8, height=2)
    btn2 = Button(window, text='2', font='arial 13', command=lambda: press('2'), width=8, height=2)
    btn3 = Button(window, text='3', font='arial 13', command=lambda: press('3'), width=8, height=2)
    btn4 = Button(window, text='4', font='arial 13', command=lambda: press('4'), width=8, height=2)
    btn5 = Button(window, text='5', font='arial 13', command=lambda: press('5'), width=8, height=2)
    btn6 = Button(window, text='6', font='arial 13', command=lambda: press('6'), width=8, height=2)
    btn7 = Button(window, text='7', font='arial 13', command=lambda: press('7'), width=8, height=2)
    btn8 = Button(window, text='8', font='arial 13', command=lambda: press('8'), width=8, height=2)
    btn9 = Button(window, text='9', font='arial 13', command=lambda: press('9'), width=8, height=2)
    btn0 = Button(window, text='0', font='arial 13', command=lambda: press('0'), width=8, height=2)
    clear_button = Button(window, text='C', font='arial 13', command=clear, width=8, height=2)
    add_button = Button(window, text='+', font='arial 13', command=lambda: press('+'), width=8, height=2)
    minus_button = Button(window, text='-', font='arial 13', command=lambda: press('-'), width=8, height=2)
    div_button = Button(window, text=u'÷', font='arial 13', command=lambda: press('/'), width=8, height=2)
    mul_button = Button(window, text=u'×', font='arial 13', command=lambda: press('*'), width=8, height=2)
    equal_button = Button(window, text='=', font='arial 13', command=result, width=8, height=2)
    erase_button = Button(window, text='<', font='arial 13', command=erase, width=8, height=2)
    percentage_button = Button(window, text='%', font='arial 13', command=lambda: press('*0.01'), width=8, height=2)
    dot_button = Button(window, text=u'•', font='arial 13', command=lambda: press('.'), width=8, height=2)
    squared_button = Button(window, text='X\u00b2', font='arial 13', command=lambda: press('**2'), width=8, height=2)
    btn1.grid(row=2, column=0)
    btn2.grid(row=2, column=1)
    btn3.grid(row=2, column=2)
    btn4.grid(row=3, column=0)
    btn5.grid(row=3, column=1)
    btn6.grid(row=3, column=2)
    btn7.grid(row=4, column=0)
    btn8.grid(row=4, column=1)
    btn9.grid(row=4, column=2)
    btn0.grid(row=5, column=1)
    clear_button.grid(row=1, column=0)
    add_button.grid(row=2, column=3)
    minus_button.grid(row=3, column=3)
    div_button.grid(row=4, column=3)
    mul_button.grid(row=5, column=3)
    equal_button.grid(row=5, column=2)
    erase_button.grid(row=1, column=1)
    percentage_button.grid(row=1, column=2)
    dot_button.grid(row=5, column=0)
    squared_button.grid(row=1, column=3)


GUI_main()
window.mainloop()
