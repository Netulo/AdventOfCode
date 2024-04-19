f = open('2019/Day 2/input.txt', 'r')
line = f.read().split(',')
for i in range(len(line)): line[i] = int(line[i])

for x in range(100):
    for y in range(100):
        tempLine = line.copy()
        line[1] = x
        line[2] = y
        iter = 0
        while(iter < len(line)-4):
            if line[iter] == 99:
                break
            
            if line[iter] == 1:
                try:
                    line[line[iter+3]] = line[line[iter+1]] + line[line[iter+2]]
                except: 
                    for i in range(line[iter+3] - len(line)+1):
                        line.append(0)
                    line[line[iter+3]] = line[line[iter+1]] + line[line[iter+2]]
            else:
                try:
                    line[line[iter+3]] = line[line[iter+1]] * line[line[iter+2]]
                except: 
                    for i in range(line[iter+3] - len(line)+1):
                        line.append(0)
                    line[line[iter+3]] = line[line[iter+1]] * line[line[iter+2]]
            iter += 4
        # print(line)
        if line[0] == 19690720:
            print(100 * x + y)
            exit(0)
        line = tempLine.copy()
        
