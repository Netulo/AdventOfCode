f = open("2015/Day 3/input.txt", "r")

text = f.read()

x = y = 0
dic = dict()
for i in text:
    if i == '^':
        y += 1
    elif i == 'v':
        y -= 1
    elif i == '>':
        x += 1
    elif i == '<':
        x -= 1
        
    try:
        dic[x,y] += 1
    except:
        dic[x,y] = 1
        
print(len(dic))
    