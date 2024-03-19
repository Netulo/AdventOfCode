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
    for num in numberSet:
        for board in range(len(boards)):
            for row in range(len(boards[board])):
                if num in boards[board][row]:
                    while 1:
                        try:
                            answ = boards[board][row].index(num)
                            boards[board][row][answ] = '*' + boards[board][row][answ]
                        except:
                            break
                
                if all('*' in i for i in boards[board][row]):
                    boards[board].pop(row)
                    return int(num) * SumOfTable(boards[board])
         #sprawdzanie kolumn - brak
            if all(e)
    return 0


f = open('2021/Day 4/input.txt', 'r')
numberSet = f.readline().split(',')
f.readline()
boards = f.read().split('\n\n')

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
        