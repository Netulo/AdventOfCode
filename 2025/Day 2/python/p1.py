import math

with open("2025/Day 2/input.txt", "r") as f:
    data = f.read().split(',')

def check_if_overlap(num: int):
    half_len = (int(math.log10(num))+1) / 2
    right = num % pow(10, half_len)
    left = (num - right) / pow(10, half_len)

    if left == right:
        return num
    return 0

sum = 0
for elem in data:
    rng = elem.split('-')
    range_start = (int)(rng[0])
    range_end = (int)(rng[1])
    for num in range(range_start, range_end + 1):
        sum += check_if_overlap(num)


print(sum)
    