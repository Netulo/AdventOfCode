f = open('2020/Day 6/input.txt', 'r')
groupTable = f.read().split('\n\n')
sum = 0
for x in groupTable:
    tempDic = dict()
    for y in x:
        if y != '\n':
            try:
                tempDic[y] += 1
            except:
                tempDic[y] = 1
    sum += list(tempDic.values()).count(x.count('\n')+1)
print(sum)