f = open("2015/Day 3/input.txt", "r")

text = f.read()
#text = "^v^v^v^v^v"

x = y = 0
santa1 = [0,0]
santa2 = [0,0]
tempIter = 1
dic = {}
for i in text:
    if tempIter%2 == 0:
        y = santa1[1]
        x = santa1[0]
    else:
        y = santa2[1]
        x = santa2[0]
        
    if i == '^':
        y += 1
    elif i == 'v':
        y -= 1
    elif i == '>':
        x += 1
    elif i == '<':
        x -= 1
        
    if tempIter%2 == 0:
        santa1[1] = y
        santa1[0] = x
    else:
        santa2[1] = y
        santa2[0] = x
    tempIter += 1
        
    try:
        dic[x,y] += 1
    except:
        dic[x,y] = 1
        
        
print(len(dic))
    