f = open('2022/Day 8/test.txt','r')
text = f.read().split('\n')

for x in range(len(text)):
    text[x] = [*text[x]]

suma = len(text)*4-4
for y in range(1, len(text)-1):
    for x in range(1, len(text[y])-1):
        if any(ord(text[y][x]) > ord(text[i][x]) for i in range(y-1, y+2)) and any(ord(text[y][x]) > ord(text[y][i]) for i in range(x-1, x+2)):
            suma += 1
print(suma)