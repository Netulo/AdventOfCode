f = open('2021/Day 13/input.txt', 'r')
text = f.read().split('\n\n')
cords = dict()
for cord in text[0].split('\n'):
    cords[cord] = 1

maxX = 0
maxY = 0
for fold in text[1].split('\n'):
    fold = fold[fold.find('=')-1:]
    foldNum = int(fold[2:])

    for cord in list(cords.keys()):
        
        if fold[0] == 'y':
            temp = cord[cord.find(',')+1:]
            if int(temp) > foldNum:
                del cords[cord]
                newNum = 2*foldNum - int(temp)
                if newNum > maxY: maxY = newNum
                cords[cord[:cord.find(',')+1] + str(newNum)] = 1
                
        if fold[0] == 'x':
            temp = cord[:cord.find(',')]
            if int(temp) > foldNum:
                del cords[cord]
                newNum = 2*foldNum - int(temp)
                if newNum > maxX: maxX = newNum
                cords[str(newNum) + cord[cord.find(','):]] = 1
        
print(cords)

table = []
for y in range(maxY+1):
    table.append('')
    for x in range(maxX+1):
        try:
            cords[f'{x},{y}']
            table[y] += '#'
        except:
            table[y] += '.'
    print(table[y])
            
