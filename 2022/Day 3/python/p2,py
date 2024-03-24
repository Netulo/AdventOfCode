f = open('2022/Day 3/input.txt', 'r')
# lines = f.read().split('\n')
letters = []

while True:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    if not line1:
        break
    
    for char in line1:
        if char in line2 and char in line3:
            letters.append(char)
            break

answ = 0
for char in letters:
    if char.isupper():
        answ += ord(char)-ord("A")+27
    else:
        answ += ord(char)-ord("a")+1
        
print(answ)