f = open('2022/Day 3/input.txt', 'r')
lines = f.read().split('\n')
letters = []
for line in lines:
    halfStrLen = int(len(line)/2)
    for li1 in line[:halfStrLen]:
        if line[halfStrLen:].find(li1) != -1:
            letters.append(li1)
            break
answ = 0
for char in letters:
    if char.isupper():
        answ += ord(char)-ord("A")+27
    else:
        answ += ord(char)-ord("a")+1
        
print(answ)