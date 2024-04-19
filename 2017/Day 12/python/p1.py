def searchForZero(pipesDict, pipesKey, visited):
    
    if pipesKey in visited:
        return 0
    visited.append(pipesKey)
    
    if '0' in pipesDict[pipesKey] or pipesKey == '0':
        return 1
    
    for x in pipesDict[pipesKey]:
        if searchForZero(pipesDict, x, visited) == 1:
            return 1
    return 0
    
f = open('2017/Day 12/input.txt', 'r')
text = f.read().split('\n')

pipes = dict()
for x in text:
    x = x.split(' <-> ')
    pipes[x[0]] = x[1].split(', ')
    
suma = 0
for x in list(pipes.keys()):
    suma += searchForZero(pipes, x, [])

print(suma)