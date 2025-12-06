import time
from utils.utils_py import *


def slow(data: list):
    start_time = time.time()

    num_list = [f"{i}" for i in range(9, 0, -1)]
    joltage_sum = 0
    for line in data:
        for i in num_list:

            occ = [j for j, x in enumerate(line) if x == i]
            max_vals = []

            for j in occ:
                if j != len(line) - 1:
                    max_vals.append(i + max(line[j+1:]))
            max_len = len(max_vals)
            if max_len == 0:
                continue
            if len(max_vals) == 1:
                joltage_sum += int(max_vals[0])
            else:
                joltage_sum += max([int(x) for x in max_vals])

            # print(f"Line {line} | max_vals {max_vals} | char {i}")
            break
    
    print("\n*-----------PART 1-------------")
    print("|")
    print(f"| - Joltage sum is {joltage_sum}")
    print(f"| - Took {(round((time.time() - start_time) * 1000, 3))} miliseconds" )
    print("|")
    print("*------------------------------\n")
    print_solution(
        1, 
        "First approach", 
        "Joltage sum is {joltage_sum}", 
        "Took {(round((time.time() - start_time) * 1000, 3))} miliseconds"
        )



def fast(data: list[str]):
    start_time = time.time()
    joltage_sum = 0
    right_barrier = 12
    for line in data:
        idx = 0
        str_num = ""
        prev_idx = -1
        for i in range(right_barrier - 1, 0, -1):
            # print(f"Line {line} | substr {line[idx:-i]} | char {max(line[idx:-i])}")

            tmp = max(line[idx:-i])
            tmp_idx = idx
            idx = line.find(tmp, idx)
            str_num += line[idx]
            idx += 1


        if len(str_num) < right_barrier:
            str_num += max(line[idx:])
        # print(f"---- joltage: {str_num} ----")
        joltage_sum += int(str_num)

    print("\n*-----------PART 2-------------")
    print("|")
    print(f"| - Joltage sum is {joltage_sum}")
    print(f"| - Took {(round((time.time() - start_time) * 1000, 3))} miliseconds")
    print("|")
    print("*------------------------------\n")


def main():
    with open("2025/Day 3/input.txt", "r") as f:
        data = f.read().split("\n")
    
    print("\n")
    slow(data)
    fast(data)

if __name__ == "__main__":
    main()
