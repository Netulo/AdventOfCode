from collections import Counter    

f = open('2019/Day 4/input.txt', 'r')
rge = f.read().split('-')
suma = 0
doubleDigits = False
passwd = 111221
for passwd in range(int(rge[0]), int(rge[1])):
    passwd = str(passwd)
    if all(ord(passwd[i]) <= ord(passwd[i+1]) for i in range(0, 5)):
        if any(x == 2 for x in Counter(passwd).values()):
            suma += 1
print(suma)