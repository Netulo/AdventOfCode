f = open('2015/Day 2/input.txt')
text = f.read().split('\n')
answ = 0
for line in text:
    line = line.split('x')
    line[0] = int(line[0])
    line[1] = int(line[1])
    line[2] = int(line[2])

    temp = [0,0,0]
    temp[0] = 2*line[0]*line[1]
    temp[1] = 2*line[1]*line[2]
    temp[2] = 2*line[0]*line[2]
    
    answ += sum(temp) + min(temp)/2
    
print(answ)