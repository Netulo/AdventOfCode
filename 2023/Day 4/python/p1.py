f = open('2023/Day 4/input.txt', 'r')
text = f.read().split('\n')
answ = 0

for line in text:
    line = line[line.find(':')+1:]
    nums = line.split('|')
    nums[0] = [i for i in nums[0].split(' ') if i != ''] 
    nums[1] = [i for i in nums[1].split(' ') if i != '']
    sum = 0
    for x in nums[0]:
        if x in nums[1]:
            if sum == 0:
                sum = 1
            else:
                sum *= 2
    answ += sum

print(answ)