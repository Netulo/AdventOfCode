input_string_table = open("2015/Day 8/input.txt", 'r').read().split('\n')

encoded_base_length = 0

for i in input_string_table:
    encoded_base_length += i.count('\\') + i.count('"') + 2

print(encoded_base_length)