def part1(data: list[str]):
    start_pos = data[0].find("S")
    beam_list = [0 for i in range(0, len(data[0]))]
    beam_list[start_pos] = 1

    split_counter = 0

    for i in range(1, len(data)):
        for j in range(0, len(data[0])):
            if data[i][j] == "^" and beam_list[j] == 1:
                beam_list[j] = 0
                beam_list[j-1] = 1
                beam_list[j+1] = 1
                split_counter += 1

    return split_counter

def part2(data):
    start_pos = data[0].find("S")
    beam_list = [0 for i in range(0, len(data[0]))]
    beam_list[start_pos] = 1

    for i in range(1, len(data)):
        for j in range(0, len(data[0])):
            if data[i][j] == "^" and beam_list[j] > 0:
                beam_list[j-1] += beam_list[j]
                beam_list[j+1] += beam_list[j]
                beam_list[j] = 0
                

    return sum(beam_list)

def main():
    with open("2025/Day 7/input.txt", "r") as f:
        data = f.read().splitlines()
    
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()