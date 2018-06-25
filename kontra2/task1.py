with open('quotes.txt', encoding='utf-8') as f:
    text = f.read()
    text = text.split("\n")
    for line in text:
        line = line.split("|, -")
        if len(line) < 10:
            print(line)
            
