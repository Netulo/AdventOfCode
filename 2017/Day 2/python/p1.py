f = open("2017/Day 2/input.txt", "r")

text = f.read()

table = text.split('\n')
sum = 0
for x in table:
    temp = x.split('\t')
    temp = [int(y) for y in temp]
    sum += max(temp) - min(temp)
    
print(sum)