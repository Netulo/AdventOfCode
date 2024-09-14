def test_case_one(s):
    vovels = ['a', 'e', 'i', 'o', 'u']
    vovels_count = 0
    
    for i in s:
        if i in vovels: 
            vovels_count += 1
            if vovels_count >= 3: return 1
            
    return 0

def test_case_two(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return 1
    return 0

def test_case_three(s):
    unallowed_strings = ['ab', 'cd', 'pq', 'xy']
    
    for i in unallowed_strings:
        if i in s: return 0
        
    return 1

nice_string_counter = 0

input_string_table = open('2015/Day 5/input.txt', 'r').read().split('\n')

for s in input_string_table:
    if test_case_one(s) and test_case_two(s) and test_case_three(s):
        nice_string_counter += 1

print(nice_string_counter)