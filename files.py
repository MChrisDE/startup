def getdata(file_path):
    with open(file_path) as f:
        listname = (f.readlines())
    names, links = [], []
    for i in listname:
        namestemp, linkstemp = i.split("~")
        names.append(namestemp.replace("\n", ""))
        links.append(linkstemp.replace("\n", ""))
    return names, links


def getdata2(file_path):
    names, links = [], []
    with open(file_path) as f:
        for i in f.read().splitlines():
            namestemp, linkstemp = i.split("~")
            names.append(namestemp)
            links.append(linkstemp)
    return names, links


import time

i = 0
start = time.time()
while time.time() - start < 1:
    getdata('data.txt')
    i += 1
print(i)  # around 9150/s

i = 0
start = time.time()
while time.time() - start < 1:
    getdata2('data.txt')
    i += 1
print(i)  # around 9350/s
