from tkinter import *
from tkinter import ttk
import webbrowser


class Row:
    def __init__(self, name, link, main, nummer):
        self.name = name
        self.link = link
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 11))
        self.Button = ttk.Button(main, text=self.name, style="TButton", command=self.openlink)
        self.Button.grid(row=nummer, column=0, padx=70, pady=5)

    def openlink(self):
        webbrowser.open_new_tab(self.link)
        print("opened \"{link}\" in your default browser".format(link=self.link))


class Entrys:
    def __init__(self, name, nummer, main, column):
        self.main = main
        self.column = column
        self.text = StringVar()
        e = Entry(self.main, textvariable=self.text)
        e.grid(row=nummer, column=self.column, padx=20, pady=5)
        self.text.set(name)
