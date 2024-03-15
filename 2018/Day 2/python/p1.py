f = open("2018/Day 2/input.txt", "r")
text = f.read()
inputTab = text.split('\n')
tripple = dobble = 0
for x in inputTab:
    dic = dict()
    for y in x:
        try:
            dic[y] += 1
        except:
            dic[y] = 1
    if 3 in dic.values():
        tripple += 1
    if 2 in dic.values():
        dobble += 1

print(tripple*dobble)
