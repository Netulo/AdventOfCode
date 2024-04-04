f = open('2015/Day 2/input.txt')
text = f.read().split('\n')
answ = 0
for line in text:
    line = line.split('x')
    for x in range(len(line)):
        line[x] = int(line[x])
    line.sort()
    answ += 2*line[0]+2*line[1] + line[0]*line[1]*line[2]
    
print(answ)