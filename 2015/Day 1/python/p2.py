f = open("2015/Day 1/input.txt", "r")
text = list(f.read())

while(True):
    try:
      x = text.index('(')
      y = text[x:].index(')')
    except:
        break
    text[y+x] = text[x] = '0'
    
print(text.index(')')+1)