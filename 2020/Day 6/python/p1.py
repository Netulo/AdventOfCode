f = open('2020/Day 6/input.txt', 'r')
groupTable = f.read().split('\n\n')
sum = 0
for x in groupTable:
    tempDic = dict()
    for y in x:
        if y != '\n':
            tempDic[y] = True
    sum += len(tempDic)
print(sum)