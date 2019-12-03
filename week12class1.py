from tkinter import *
from tkinter import messagebox

warning = 0


def ask_button():
    ans = messagebox.askyesno('질문', '당신은 고대인입니까?')
    if ans:
        messagebox.showinfo('', '저는 현대인입니다')
    else:
        messagebox.showinfo('', '저는 고대인입니다')


window = Tk()
ask = Button(window, text='질문', command=ask_button)
ask.pack()


window.mainloop()
