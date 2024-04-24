f = open('2022/Day 8/input.txt','r')
text = f.read().split('\n')

for x in range(len(text)):
    text[x] = [*text[x]]

suma = len(text)*4-4
for y in range(1, len(text)-1):
    for x in range(1, len(text[y])-1):
        if all(ord(text[y][x]) > ord(text[i][x]) for i in range(0, y)) or all(ord(text[y][x]) > ord(text[i][x]) for i in range(y+1, len(text))) or all(ord(text[y][x]) > ord(text[y][i]) for i in range(0, x)) or all(ord(text[y][x]) > ord(text[y][i]) for i in range(x+1, len(text[y]))):
            suma += 1
            print(x+1)
            print(y+1)
            print()
print(suma)