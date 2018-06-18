import re

def readfile():
  filename = 'mystem.xml'
  with open(filename, encoding='utf-8') as f:
    text = f.read()
  return text

def countverbs(text):
  n = 0
  x = re.findall(r'<w>.*?gr=\"V.*?сов.*?ед', text) + re.findall(r'<w>.*?gr=\"V.*?ед.*?сов', text)
  for i in x:
    n += 1
  n = str(n)
  x = 'vsego glagolov:'+' ' + n
  return x

def writefile(x):
  with open('verbs.txt','w', encoding='utf-8') as f:
    f.write(x)
    
def main():
  writefile(countverbs(readfile()))

if __name__ == '__main__':
  main()
