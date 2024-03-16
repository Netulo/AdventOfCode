def EraseElementAtIndex(index, tab):
    temp = []
    for y in tab:
        temp.append(y[:index] + y[index+1:])
    return temp

def SearchForOcc(tab):
    for y in tab:
        answ = tab.index(y)
        tab.pop(answ)
        tab.insert(answ, 'null')
        if y in tab:
            return y
    return False


f = open('2018/Day 2/input.txt', 'r')
inputTab = f.read().split('\n')

for x in range(len(inputTab[0])):
    answ = SearchForOcc(EraseElementAtIndex(x, inputTab))
    if answ != False:
        print(answ)
        break