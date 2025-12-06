f = open("2025/Day 1/input.txt", "r")
data = f.read().split("\n")

dial_pos = 50
count_zeros = 0

def get_zone_r(n):
    return n // 100

def get_zone_l(n):
    return (n - 1) // 100

for elem in data:    
    direction = elem[0]
    shift = int(elem[1:])
    
    if direction == 'R':
        prev_pos = dial_pos
        dial_pos += shift
        
        passes = get_zone_r(dial_pos) - get_zone_r(prev_pos)
        count_zeros += passes

    elif direction == 'L':
        prev_pos = dial_pos
        dial_pos -= shift
        
        passes = get_zone_l(prev_pos) - get_zone_l(dial_pos)
        count_zeros += passes

print(count_zeros)












# f = open("2025/Day 1/input.txt", "r")

# data = f.read().split("\n")

# dial_pos = 50

# def rotate_dial(init_dial, shift, direction):
#     zero_pass = 0

#     if direction[0] == 'L':
#         dial = init_dial - shift
#         zero_pass = -((dial - 1) // 100)
#         dial = -dial % 100

        
#     if direction[0] == 'R':
#         dial = init_dial + shift
#         zero_pass = dial // 100
#         dial = dial % 100

#     return dial, zero_pass

# count_zeros = 0
# for elem in data:
#     shift = (int)(elem[1:])
#     dial_pos, tmp_zero_pass = rotate_dial(dial_pos, shift, elem[0])

#     count_zeros += tmp_zero_pass
#     # if dial_pos == 0:
#     #     count_zeros += 1

# print(count_zeros)


#between 6176 and 7111
#correct 6860