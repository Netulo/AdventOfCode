f = open('2017/Day 8/input.txt')
text = f.read().split('\n')
registers = dict()

for reg in text:
    reg = reg.replace('inc', '+')
    reg = reg.replace('dec', '-')
    reg = reg.split(' ')
    
    execStr = "if registers.setdefault('" + reg[4] +"', 0) " + reg[5] + reg[6] + ": registers['" + reg[0] + "'] = registers.setdefault('" + reg[0] + "', 0)" + reg[1] + reg[2]
    exec(execStr)
    
print(max(list(registers.values())))
