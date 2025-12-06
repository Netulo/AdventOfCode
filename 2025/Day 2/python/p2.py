import math
import time
start_time = time.time()

with open("2025/Day 2/input.txt", "r") as f:
    data = f.read().split(',')



def check_if_overlap(num: str):
    str_len = len(num)
    # half_len = str_len // 2
    # if str_len % 2 != 0: 
    #     half_len += 1
    

    for i in range(1, str_len):
        # print(f"i = {i} | slice = {num[0:i]} | num = {num} | test = {num[0:i]*(str_len // i)}")
        if num[0:i]*(str_len // i) == num:
            return (int)(num)
    # for i in range(1, half_len + 1):
    #     tmp_str = num
    #     tmp_str = tmp_str.replace(num[0:i], "")
    #     if len(tmp_str) == 0:
    #         return (int)(num)
    
    return 0


sum = 0
for elem in data:
    rng = elem.split('-')
    range_start = (int)(rng[0])
    range_end = (int)(rng[1])
    for num in range(range_start, range_end + 1):
        sum += check_if_overlap((str)(num))


print(sum)

print(f"--- {(round(time.time() - start_time, 4))} seconds ---" )
    