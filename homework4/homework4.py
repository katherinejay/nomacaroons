with open("text.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff", "")
lines = text.splitlines()
words = text.split()

vsego = 0
stroki = 0
