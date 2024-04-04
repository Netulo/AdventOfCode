f = open('2022/Day 4/input.txt', 'r')
pairs = f.read().split('\n')

def isOverlaping(pairOne, pairTwo):
    pairOne = pairOne.split('-')
    pairTwo = pairTwo.split('-')
    if int(pairOne[0]) >= int(pairTwo[0]):
        if int(pairOne[1]) <= int(pairTwo[1]):
            return True
    return False

answ = 0
for pair in pairs:
    pair = pair.split(',')
    if isOverlaping(pair[0], pair[1]) or isOverlaping(pair[1], pair[0]):
        answ += 1
print(answ)