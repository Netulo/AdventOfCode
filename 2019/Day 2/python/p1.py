f = open('2019/Day 2/input.txt', 'r')
line = f.read().split(',')
for i in range(len(line)): line[i] = int(line[i])
line[1] = 12
line[2] = 2
iter = 0
while(iter < len(line)-4):
    if line[iter] == 99:
        break
    
    if line[iter] == 1:
        line[line[iter+3]] = line[line[iter+1]] + line[line[iter+2]]
    else:
        line[line[iter+3]] = line[line[iter+1]] * line[line[iter+2]]
    iter += 4
    
print(line[0])