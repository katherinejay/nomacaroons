with open('quotes.txt', encoding='utf-8') as f:
    text = f.readlines()
    razum = 0
for line in text:
    a = line.find('разум')
    if a != -1:
        razum += 1
        print(line, ', ')
print(razum)
        
