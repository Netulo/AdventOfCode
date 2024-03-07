f = open("2017/Day 2/input.txt", "r")

text = f.read()

table = text.split('\n')
sum = 0
for x in table:
    temp = x.split('\t')
    temp = [int(y) for y in temp]
    
    for i in temp:
        for j in temp:
            if i%j == 0 and i !=j:
                #print(i, j, sep='\t')
                sum += int(i / j)
    
    
print(sum)