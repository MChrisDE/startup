from files import *
from objects import *
import os


def handle_url(url) -> str:
    """
    Prevents Windows from defaulting to open some URLs in IE 
    by adding a default url scheme to the input string
    if URL doesn't contain a scheme
    :param url: url from link text input
    :return: 'url' prefixed with default protocol or unchanged parameter 'url'
    """
    if "https://" not in url[:8] and "http://" not in url[:7]:
        url = "http://" + url
    return url


def saveChanges(main):
    text = ""
    global file_path, flow, nameobjectlist, linkobjectlist
    for i in range(0, len(nameobjectlist)):
        if nameobjectlist[i].text.get() != '' and linkobjectlist[i].text.get() != '':
            text += nameobjectlist[i].text.get() + "~" + handle_url(linkobjectlist[i].text.get()) + "\n"

    f = open(file_path, "w")
    f.write(text)
    f.close()

    main.destroy()


def add(main):
    global nameobjectlist, linkobjectlist
    nameobjectlist.append(Entrys("", len(nameobjectlist) + 1, main, 0))
    linkobjectlist.append(Entrys("", len(linkobjectlist) + 1, main, 1))


# Thanks to: http://stackoverflow.com/a/15306785
class MainWindow(Frame):
    counter = 0

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        names, links = getdata(file_path)
        # creating the buttons
        objectlist = []
        for i in range(0, len(names)):
            objectlist.append(Row(names[i], links[i], self, i))

    def edit(self):
        # creating a main window
        names, links = getdata(file_path)
        t = Toplevel(self)
        t.wm_title("startup - edit")
        t.protocol("WM_DELETE_WINDOW", lambda: quit())
        t.grab_set()

        global nameobjectlist
        nameobjectlist = []
        for i in range(0, len(names)):
            nameobjectlist.append(Entrys(names[i], i + 1, t, 0))

        global linkobjectlist
        linkobjectlist = []
        for i in range(0, len(names)):
            linkobjectlist.append(Entrys(links[i], i + 1, t, 1))

        ttk.Style().configure("TButton", font=("Arial", 11))

        save_button = ttk.Button(t, text="Save", style="TButton", command=lambda: saveChanges(t))
        save_button.bind("<Return>", lambda event: saveChanges(t))
        save_button.grid(row=0, column=1, padx=0, pady=25)
        save_button.focus_set()

        add_button = ttk.Button(t, text="Add new entry", style="TButton", command=lambda: add(t))
        add_button.grid(row=0, column=0, padx=0, pady=25)


file_path = os.path.realpath(__file__).replace("main.py", "data.txt")
nameobjectlist = []
linkobjectlist = []

# creating a main window
root = Tk()
main = MainWindow(root)
main.pack(side="top", fill="both", expand=True)
root.wm_title("startup")
root.protocol("WM_DELETE_WINDOW", lambda: quit())

# creating a menubar
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Quit", command=lambda: quit())
menu.add_command(label="Edit", command=lambda: main.edit())

root.mainloop()
