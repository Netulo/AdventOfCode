f = open('2021/Day 4/test.txt', 'r')
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
    
def SumOfTable(table, numberSet):
    sum = 0
    for x in table:
        for y in x:
            if y not in numberSet:
                sum += int(y)
    return sum
    
def BingoRow(boards, board, tempNumberSet):
    for row in boards[board]:    
        if all(e in tempNumberSet for e in row):
            if len(boards) == 1:
                return int(tempNumberSet[-1]) * SumOfTable(boards[board], tempNumberSet)
            else:
                boards.pop(board)
                break
    return boards
                
def BingoCol(boards, board, tempNumberSet):
    for row in range(len(boards[board])):  
        for col in range(len(boards[board][row])):
            if all(e[col] in tempNumberSet for e in boards[board]):
                if len(boards) == 1:
                    return int(tempNumberSet[-1]) * SumOfTable(boards[board], tempNumberSet)
                else:
                    boards.pop(board)
                    break
    return boards
    
def checkIfBingo(numberSet, boards):
    for num in range(len(numberSet)):
        tempNumberSet = numberSet[:num+1]
        for board in range(len(boards)): 
            answ = BingoRow(boards, board, tempNumberSet)
            if type(answ) == type(1):
                return answ
            else:
                boards = answ
            answ = BingoCol(boards, board, tempNumberSet)
            if type(answ) == type(1):
                return answ
            else:
                boards = answ
                            
                
print(checkIfBingo(numberSet, boards))                  