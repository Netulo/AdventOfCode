import time

def part1(data: list[str]):
    rollsTab = []
    rolls_sum = 0
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            sum_adj = 0
            if data[i][j] == "@":
                if j > 0: 
                    if data[i][j-1] == "@": sum_adj += 1
                    if i < len(data) - 1 and data[i+1][j-1] == "@": sum_adj += 1
                    if i > 0 and data[i-1][j-1] == "@": sum_adj += 1
                if j < len(data[i]) - 1: 
                    if data[i][j+1] == "@": sum_adj += 1
                    if i < len(data) - 1 and data[i+1][j+1] == "@": sum_adj += 1
                    if i > 0 and data[i-1][j+1] == "@": sum_adj += 1

                if i > 0 and data[i-1][j] == "@": sum_adj += 1
                if i < len(data) - 1 and data[i+1][j] == "@": sum_adj += 1
            
                if sum_adj < 4: rolls_sum += 1
    
    return rolls_sum


def part2(data_in: list[str]):
    rollsTab = []
    rolls_sum = 0
    data = []
    for i in range(0, len(data_in)):
        data.append(list(data_in[i]))

    while True:
        tmp_data = data
        roll_removed = False
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                sum_adj = 0
                if data[i][j] == "@":
                    if j > 0: 
                        if data[i][j-1] == "@": sum_adj += 1
                        if i < len(data) - 1 and data[i+1][j-1] == "@": sum_adj += 1
                        if i > 0 and data[i-1][j-1] == "@": sum_adj += 1
                    if j < len(data[i]) - 1: 
                        if data[i][j+1] == "@": sum_adj += 1
                        if i < len(data) - 1 and data[i+1][j+1] == "@": sum_adj += 1
                        if i > 0 and data[i-1][j+1] == "@": sum_adj += 1

                    if i > 0 and data[i-1][j] == "@": sum_adj += 1
                    if i < len(data) - 1 and data[i+1][j] == "@": sum_adj += 1
                
                    if sum_adj < 4: 
                        tmp_data[i][j] = '.'
                        roll_removed = True
                        rolls_sum += 1
        data = tmp_data
        
        if not roll_removed: break

    
    return rolls_sum




def main():
    with open("2025/Day 4/input.txt") as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()