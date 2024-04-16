from collections import Counter
f = open('2022/Day 7/test.txt', 'r')
lines = f.read().split('\n')

answ = 0
currentDirectory = []
dirTree = {'/':dict()}
for line in lines:
    if line[0] == '$':
        if 'cd' in line:
            if '/' in line: currentDirectory = ['/']
            elif '..' in line: currentDirectory = currentDirectory[:-1]
            else: currentDirectory.append(line[line.rfind(' ')+1:])
    else:
        temp = dirTree
        for i in currentDirectory: temp = temp[i]
        if 'dir' in line: temp[line[line.find(' ')+1:]] = dict()
        # else: temp[line[line.find(' ')+1:]] = int(line[:line.find(' ')])
        else: temp[line[:line.find(' ')]] = int(line[:line.find(' ')])
 
 
for x in dirTree['/']:
    print(x)
# print(dirTree)