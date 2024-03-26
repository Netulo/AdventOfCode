f = open('2017/Day 8/input.txt')
text = f.read().split('\n')
registers = dict()

maxValue = 0
for reg in text:
    reg = reg.replace('inc', '+')
    reg = reg.replace('dec', '-')
    reg = reg.split(' ')
    
    execStr = "if registers.setdefault('" + reg[4] +"', 0) " + reg[5] + reg[6] + ": registers['" + reg[0] + "'] = registers.setdefault('" + reg[0] + "', 0)" + reg[1] + reg[2]
    exec(execStr)
    
    if maxValue < registers.setdefault(reg[0], 0): maxValue = registers[reg[0]]
    
print(maxValue)