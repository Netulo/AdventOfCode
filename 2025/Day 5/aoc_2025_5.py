
def part1(ranges, ingredients):
    fresh_sum = 0

    ranges2 = []
    for i in ranges:
        tmp_ran_st, tmp_ran_en = i.split("-")
        ranges2.append([int(tmp_ran_st), int(tmp_ran_en)])

    for i in ingredients:
        ing_num = int(i)
        for item in ranges2:
            if ing_num >= item[0]:
                if ing_num <= item[1]:
                    fresh_sum += 1
                    # print(f"Item {ing_num} | range {item[0]} - {item[1]}")
                    break

    return fresh_sum


def part2_SHIT(ranges):
    fresh_sum = 0
    ranges2 = []
    for i in ranges:
        tmp_ran_st, tmp_ran_en = i.split("-")
        ranges2.append([int(tmp_ran_st), int(tmp_ran_en)])

    range_len = len(ranges2)
    i,j = 0, 0
    overlap_counter = 0

    while i < range_len:
        j = 0
        while j < range_len:
            if j != i and ranges2[i][1] >= ranges2[j][0] and ranges2[i][0] <= ranges2[j][1]:
                overlap_counter = 1
                print(f"range 1 {ranges2[i]} | range 2 {ranges2[j]} | product {[ranges2[i][0], ranges2[j][1]]}")
                tmp_st = min(ranges2[i][0], ranges2[j][0])
                tmp_en = max(ranges2[i][1], ranges2[j][1])

                tmp_remove_1 = [ranges2[i][0], ranges2[i][1]]
                tmp_remove_2 = [ranges2[j][0], ranges2[j][1]]

                ranges2.remove(tmp_remove_1)
                ranges2.remove(tmp_remove_2)
                ranges2.append([tmp_st, tmp_en])
                print(f"Modified range {ranges2}")
                range_len -= 1
                if i > 1:
                    i -= 2
                elif i > 0: i -= 1
                if j > 1:
                    j -= 2
                elif j > 0 > 0: j -= 1
                break
            j += 1
        i += 1
        if i == range_len and overlap_counter != 0:
            overlap_counter = 0
            i = 0
    
            
    for i in ranges2:
        print(f"range {i}")
        fresh_sum += i[1] - i[0] + 1


    return fresh_sum




def main():
    with open("2025/Day 5/input.txt", "r") as f:
        tmp_load = f.read().split("\n\n")
        fresh_ranges = tmp_load[0].splitlines()
        ingredients = tmp_load[1].splitlines()
    print(part1(fresh_ranges, ingredients))
    print(part2_SHIT(fresh_ranges))


if __name__ == "__main__":
    main()



    # too low 
    # 312017331335452
    # 307164622772557

    # wrong
    # 350780324308412
    # 370891773773196


    # 350780324308385
    # 