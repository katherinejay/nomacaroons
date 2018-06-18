import re

def readfile():
  filename = 'mystem.xml'
  with open(filename, encoding='utf-8') as f:
    text = f.read()
  return text

def countlines(text):
  n = 0
  x = re.findall('\n',text)
  for i in x:
    n += 1
  n = str(n-3)
  x = 'vsego strok:'+' ' + n
  return x

def writefile(x):
  with open('res.txt','w', encoding='utf-8') as f:
    f.write(x)

def main():
  writefile(countlines(readfile()))

if __name__ == '__main__':
  main()
