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
        self.link = self.link.replace("https://", "")
        self.link = self.link.replace("http://", "")
        self.link = self.link.replace("www.", "")
        webbrowser.open_new_tab("http://" + self.link)

        print("open...")


class Entrys:
    def __init__(self, name, nummer, main, column):
        self.main = main
        self.column = column
        self.text = StringVar()
        e = Entry(self.main, textvariable=self.text)
        e.grid(row=nummer, column=self.column, padx=20, pady=5)
        self.text.set(name)
