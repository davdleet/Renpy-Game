from pytube import *
from tkinter import *

window =None
download_button = None
quit_button = None
url_entry = None
help_label = None


def download():
    yt = YouTube(url())
    video = yt.streams.first()
    video.download()
    help_label['text'] = 'Download Completed'


def quit_window():
    window.destroy()


def url():
    link = url_entry.get()
    return link


def quit_message(i):
    global help_label
    help_label['text'] = 'Close the program'

def quit_message2(i):
    global help_label
    help_label['text'] = 'Enter the url of the Youtube video and press download'

def GUI_main():
    global window
    global help_label
    window = Tk()
    window.title('YT downloader')
    window.geometry('400x100')
    download_button = Button(window, command=download, text='Download')
    download_button.grid(row=1, column=0, padx=3, pady=3)
    quit_button = Button(window, command=quit_window, text='Quit')
    quit_button.grid(row=1, column=1)
    quit_button.bind('<Enter>', quit_message)
    quit_button.bind('<Leave>', quit_message2)
    url_entry = Entry(window, font='Arial 15', justify=LEFT, width=30)
    url_entry.grid(row=0, column=0, padx=5, pady=5)
    help_label = Label(window, text='Enter the url of the Youtube video and press download')
    help_label.grid(row=2, column=0)

GUI_main()
window.mainloop()
