import re

def readfile():
    text = ""
    for i in name:
        with open(i+".xhtml", "r", encoding='windows-1251') as f:
            text = f.read()
            text = text.replace("`", "")
            return text

def writetxt(text):
    for i in name:
        with open(i+".txt", "r", encoding='cp1251') as f:
            f.write("""text""")

namelist = []
name = " "
while  name != "":
    name = input("filename: ")
    if name != "":
        namelist.append(name)

writetxt((readfile()))
