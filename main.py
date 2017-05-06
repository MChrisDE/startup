from files import *
from objects import *
import os


def changeflow(main):
    main.destroy()
    global flow
    flow = "edit"


def quiteverything(main):
    main.destroy()
    global end
    end = 1


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
    flow = "main"


def showlinks():
    # creating a main window
    names, links = getdata(file_path)
    main = Tk()
    main.wm_title("startup")
    main.protocol("WM_DELETE_WINDOW", lambda: quiteverything(main))
    # creating a menubar
    menu = Menu(main)
    menu.add_command(label="Edit", command=lambda: changeflow(main))
    menu.add_command(label="Quit", command=lambda: quiteverything(main))
    main.config(menu=menu)
    # creating the buttons
    objectlist = []
    for i in range(0, len(names)):
        objectlist.append(Row(names[i], links[i], main, i))

    main.mainloop()


def add(main):
    global nameobjectlist, linkobjectlist
    nameobjectlist.append(Entrys("", len(nameobjectlist) + 1, main, 0))
    linkobjectlist.append(Entrys("", len(linkobjectlist) + 1, main, 1))


def edit():
    # creating a main window
    names, links = getdata(file_path)
    main = Tk()
    main.wm_title("startup - edit")
    main.protocol("WM_DELETE_WINDOW", lambda: quiteverything(main))
    main.grab_set()

    global nameobjectlist
    nameobjectlist = []
    for i in range(0, len(names)):
        nameobjectlist.append(Entrys(names[i], i + 1, main, 0))

    global linkobjectlist
    linkobjectlist = []
    for i in range(0, len(names)):
        linkobjectlist.append(Entrys(links[i], i + 1, main, 1))

    ttk.Style().configure("TButton", font=("Arial", 11))

    save_button = ttk.Button(main, text="Save", style="TButton", command=lambda: saveChanges(main))
    save_button.bind("<Return>", lambda event: saveChanges(main))
    save_button.grid(row=0, column=1, padx=0, pady=25)
    save_button.focus_set()

    add_button = ttk.Button(main, text="Add new entry", style="TButton", command=lambda: add(main))
    add_button.grid(row=0, column=0, padx=0, pady=25)

    main.mainloop()


# global var
flow = "main"
end = 0
file_path = os.path.realpath(__file__).replace("main.py", "data.txt")
nameobjectlist = []
linkobjectlist = []
while end == 0:
    if flow == "main":
        showlinks()
    if flow == "edit":
        edit()
