file = open('2023/Day 8/test-p2.txt', 'r')
text = file.read().split('\n\n')

count = 0
currentKey = 'AAA'
keys = dict()
turn = 0
for x in text[1].split('\n'):
    keys[x[:3]] = x[7:-1]
    
print(keys)
while currentKey != 'ZZZ':
    if text[0][turn] == 'L':
        currentKey = keys[currentKey][:3]
    else:
        currentKey = keys[currentKey][-3:]
    count += 1
    
    
    if turn == len(text[0])-1:
        turn = 0
    else:
        turn += 1
        
print(count)