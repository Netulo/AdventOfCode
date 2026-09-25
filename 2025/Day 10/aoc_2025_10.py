def part1(data):
    pass

def part2(data):
    pass

def main():
    with open("2025/Day 10/test.txt", "r") as f:
        inpLineList = []
        inpLineList = f.readlines()

    data = []
    for i in inpLineList:
        tmp_lights_str = i[1: i.find("]")]
        tmp_lights = []
        for j in tmp_lights_str:
            if j == '.':
                tmp_lights.append(0)
            if j == '#':
                tmp_lights.append(1)

        tmp_buttons_str_list = i[i.find("(") : i.rfind(")") + 1].split(" ")
        tmp_buttons = []
        for j in tmp_buttons_str_list:
            tmp_buttons.append(list(map(int, j[1:-1].split(","))))
        

        tmp_joltage = list(map(int, i[i.find("{")+ 1 : i.rfind("}")].split(",")))

        data.append([tmp_lights, tmp_buttons, tmp_joltage])


    print(part1(data))
    # for i in data:
    #     print(i[0])


if __name__ == "__main__":
    main()