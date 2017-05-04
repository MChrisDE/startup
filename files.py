def getdata(file_path):
    with open(file_path) as f:
        listname = (f.readlines())
    names, links = [], []
    for i in listname:
        namestemp, linkstemp = i.split("~")
        names.append(namestemp.replace("\n", ""))
        links.append(linkstemp.replace("\n", ""))
    return names, links
