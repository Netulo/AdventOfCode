def part1(input_data: list[str]):
    out_sum = 0
    data = input_data.copy()
    data_len = len(data)

    while True:
        if len(data[-1]) == 0:
            break
        data[-1] = data[-1].strip()
        operation = data[-1][0]
        data[-1] = data[-1][1:]
        tmp_output = 0

        counter = 1
        for i in range(data_len - 2, -1, -1):
            data[i] = data[i].strip()
            tmp_space_idx = data[i].find(" ")
            if tmp_space_idx == -1:
                num = data[i]
            else:
                num = data[i][: tmp_space_idx]

            if operation == "+":
                tmp_output += int(num)
            if operation == "*":
                tmp_output = (1 if tmp_output == 0 else tmp_output) * int(num)
            data[i] = data[i][tmp_space_idx:]
            counter += 1
        out_sum += tmp_output
    
    return out_sum



def part2(data: list[str]):
    out_sum = 0
    tmp_output = 0
    counter = 0
    print(f"{len(data[-1])}")
    for i in range(0, len(data[-1])):
        if data[-1][i] == "*" or data[-1][i] == "+":
            operation = data[-1][i]
            out_sum += tmp_output
            print(f"Partial sum {tmp_output}")

            tmp_output = 0
            counter += 1
        elif i < len(data[-1]) - 1 and (data[-1][i + 1] == "+" or data[-1][i + 1] == "*"):
            continue
    
        tmp_str_num = ""
        for j in range(0, len(data) - 1):
            if data[j][i] != " ":
                tmp_str_num += data[j][i]
        
        print(f"Column {counter} | Current num {tmp_str_num} | operation {operation}")
        if operation == "*":
            tmp_output = (1 if tmp_output == 0 else tmp_output) * int(tmp_str_num)
        else:
            tmp_output += int(tmp_str_num)

        if i == len(data[-1]) - 1:
            out_sum += tmp_output


        
    return out_sum

        

def main():
    with open("2025/Day 6/input.txt", "r") as f:
        data = f.read().split("\n")

    # print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()