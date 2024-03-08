sum = 0
for x in open("2020/Day 4/input.txt", "r").read().split("\n\n"):
    if all(y in x for y in ["byr","iyr","eyr","hgt","hcl" ,"ecl","pid"]):
        sum += 1
print(sum)