f = open('2015/Day 7/input.txt', 'r')
instructions = f.read().split('\n')
values = dict()
while(True):
    tempInst = []
    for iter in range(len(instructions)):
        temp = instructions[iter].split(" -> ")
        try:
            values[temp[1]] = int(temp[0])
        except:
            try:
                
                if 'NOT' in temp[0]:
                    procVals = temp[0].split('NOT ')
                    tempStr = '{0:016b}'.format(values[procVals[1]])
                    tempStr = tempStr.replace('0', '2')
                    tempStr = tempStr.replace('1', '0')
                    tempStr = tempStr.replace('2', '1')
                    values[temp[1]] = int(tempStr, 2)
                elif "AND" in temp[0]:
                    procVals = temp[0].split(' AND ')
                    if procVals[0].isdigit(): values[temp[1]] = int(procVals[0]) & values[procVals[1]]
                    else: values[temp[1]] = values[procVals[0]] & values[procVals[1]]
                elif "OR" in temp[0]:
                    procVals = temp[0].split(' OR ')
                    values[temp[1]] = values[procVals[0]] | values[procVals[1]]
                elif "LSHIFT" in temp[0]:
                    procVals = temp[0].split(' LSHIFT ')
                    values[temp[1]] = values[procVals[0]] << int(procVals[1])
                elif "RSHIFT" in temp[0]:
                    procVals = temp[0].split(' RSHIFT ')
                    values[temp[1]] = values[procVals[0]] >> int(procVals[1])
                else:
                    values[temp[1]] = values[temp[0]]
            except:
                tempInst.append(instructions[iter])
                continue
    instructions = tempInst
    if len(tempInst) <= 0:
        break
           
print(values['a'])