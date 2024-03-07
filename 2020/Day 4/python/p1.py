f = open("2020/Day 4/input.txt", "r")

count = 0

fields = ["byr","iyr","eyr","hgt","hcl" ,"ecl","pid"]
fields.sort()
table = []
for x in f.read().split("\n\n"):
    dic = dict()
    for y in x.replace('\n', ' ').split(' '):
        temp = y.split(':')
        dic[temp[0]] = temp[1]
        
    table.append(dic)
    
for x in table:
    tab = list(x.keys())
    tab.sort()
    try:
        tab.remove("cid")
    except:
        pass
    if tab == fields:
        count+=1
        
print(count)