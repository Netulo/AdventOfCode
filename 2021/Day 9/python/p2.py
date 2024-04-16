def BasinsCount(x, y, table):
    dic = dict()

    if y+1 != len(table) and int(table[y+1][x]) > int(table[y][x]) and int(table[y+1][x]) != 9:
        dic = dic | BasinsCount(x, y+1, table) | {(x,y+1) : 1}

    if y != 0 and int(table[y-1][x]) > int(table[y][x]) and int(table[y-1][x]) != 9:
        dic = dic | BasinsCount(x, y-1, table) | {(x,y-1) : 1}

    if x+1 != len(table[y]) and int(table[y][x+1]) > int(table[y][x]) and int(table[y][x+1]) != 9:
        dic = dic | BasinsCount(x+1, y, table) | {(x+1,y) : 1}

    if x != 0 and int(table[y][x-1]) > int(table[y][x]) and int(table[y][x-1]) != 9:
        dic = dic | BasinsCount(x-1, y, table) | {(x-1,y) : 1}
        
    return dic

f = open('2021/Day 9/input.txt', 'r')
text = f.read().split('\n')

basins = []
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
        