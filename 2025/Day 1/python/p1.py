f = open("2025/Day 1/input.txt", "r")

data = f.read().split("\n")
f.close()
dial_pos = 50

def rotate_dial(dial, instruct):
    shift = (int)(instruct[1:])

    if instruct[0] == 'L':
        dial = dial - shift
        if dial < 0:
            dial = (100 + dial) % 100
        
    if instruct[0] == 'R':
        dial = (dial + shift) % 100

    return dial

count_zeros = 0
for elem in data:
    dial_pos = rotate_dial(dial_pos, elem)
    if dial_pos == 0:
        count_zeros += 1

print(count_zeros)