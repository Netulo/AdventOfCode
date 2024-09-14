def test_case_one(s):
    for i in range(len(s)-2):
        if s[i] + s[i+1] in s[i+2:]: return 1
            
    return 0

def test_case_two(s):
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            return 1
    return 0

nice_string_counter = 0

input_string_table = open('2015/Day 5/input.txt', 'r').read().split('\n')

for s in input_string_table:
    if test_case_one(s) and test_case_two(s):
        nice_string_counter += 1

print(nice_string_counter)
