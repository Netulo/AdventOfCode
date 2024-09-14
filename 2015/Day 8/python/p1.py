input_string_table = open("2015/Day 8/input.txt", 'r').read().split('\n')

code_base_length = 0
string_base_length = 0

temp_dict = {}
for i in input_string_table:
    code_base_length += len(i)
    exec("temp_string ="+i, globals(), temp_dict)
    string_base_length += len(temp_dict["temp_string"])

print(code_base_length)
print(code_base_length - string_base_length)