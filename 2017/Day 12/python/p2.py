def searchForZero(pipesDict, pipesKey, visited):
    
    if pipesKey in visited:
        return visited
    visited.append(pipesKey)
    
    if '0' in pipesDict[pipesKey] or pipesKey == '0':
        return 1
    
    for x in pipesDict[pipesKey]:
        if searchForZero(pipesDict, x, visited) == 1:
            
            return 1
    return visited
    
f = open('2017/Day 12/input.txt', 'r')
text = f.read().split('\n')

pipes = dict()
for x in text:
    x = x.split(' <-> ')
    pipes[x[0]] = x[1].split(', ')

groups = [['-1']]
suma = 0
for x in list(pipes.keys()):
    otp = searchForZero(pipes, x, [])
    if type(otp) == type([]):
        for y in range(len(groups)):
            if any(i in groups[y] for i in otp):
                for j in otp:
                    if j not in groups[y]:
                        groups[y].extend(otp)
                break
        else:
            groups.append(otp)

print(len(groups))