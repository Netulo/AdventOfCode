f = open('2021/Day 9/input.txt', 'r')
text = f.read().split('\n')
answ = 0
for i in range(len(text)):
    for j in range(len(text[i])):
        nums = []
        if i+1 != len(text):
            nums.append(int(text[i+1][j]))
        if i != 0:
            nums.append(int(text[i-1][j]))
        if j+1 != len(text[i]):
            nums.append(int(text[i][j+1]))
        if j != 0:
            nums.append(int(text[i][j-1]))
        
        temp = int(text[i][j])
        if temp < min(nums):
            answ += 1+temp
        
print(answ)
        