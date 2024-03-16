import re

f = open('2021/Day 4/input.txt', 'r')
numberSet = f.readline().split(',')
f.readline()
boards = f.read().split('\n\n')

def SumOfTable(table):
    sum = 0
    for x in table:
        for y in x:
            if '*' in y:
                continue
            else:
                sum += int(y)
    return sum

def checkIfBingo(numberSet, boards):
    for x in numberSet:
        for y in range(len(boards)):
            for z in range(len(boards[y])):
                if x in boards[y][z]:
                    while 1:
                        try:
                            answ = boards[y][z].index(x)
                            boards[y][z][answ] = '*' + boards[y][z][answ]
                        except:
                            break
                
                if all('*' in i for i in boards[y][z]):
                    boards[y].pop(z)
                    return int(x) * SumOfTable(boards[y])
         #sprawdzanie kolumn - brak
    return 0

for x in range(len(boards)):
    temp = boards[x].split('\n')
    for y in range(len(temp)):
        temp2 = temp[y].split(' ')
        while 1: 
            try:
                temp2.remove('')
            except:
                break
        temp[y] = temp2
    boards[x] = temp

    

print(checkIfBingo(numberSet, boards))
        