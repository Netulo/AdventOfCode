import math

def distance_3d(point1, point2):
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]
    dz = point1[2] - point2[2]
    return math.sqrt(pow(dx, 2) + pow(dy, 2) + pow(dz, 2))





def part1(data: dict):
    id_counter = 1
    circuits = []
    for i in range(10):
        min_dist = 0
        min_dist_keys = []
        is_id_changed = False
        is_merged = False

        for y in data.items():
            for x in data.items():
                if x[0] == y[0]:
                    continue
                dist = distance_3d(x[0], y[0])
                if (dist < min_dist or min_dist == 0) and \
                (data[x[0]] != data[y[0]] or (data[x[0]] == 0 or data[y[0]] == 0)):
                    min_dist = dist
                    min_dist_keys = [x[0], y[0]]


        if data[min_dist_keys[0]] != 0 and data[min_dist_keys[1]] != 0:
            tmp = circuits[data[min_dist_keys[0]] - 1] + circuits[data[min_dist_keys[1]] - 1]
            circuits.append(tmp)
            circuits[data[min_dist_keys[0]] - 1] = []
            circuits[data[min_dist_keys[1]] - 1] = []
            for j in tmp:
                data[j] = id_counter
            id_counter += 1
            is_merged = True
        elif data[min_dist_keys[0]] != 0:
            data[min_dist_keys[1]] = data[min_dist_keys[0]]
        elif data[min_dist_keys[1]] != 0:
            data[min_dist_keys[0]] = data[min_dist_keys[1]]
        else:
            data[min_dist_keys[0]] = id_counter
            data[min_dist_keys[1]] = id_counter
            is_id_changed = True
            id_counter += 1

        print(f"{min_dist_keys[0]} | {min_dist_keys[1]} | id {data[min_dist_keys[0]]}")


        if is_id_changed:
            circuits.append([min_dist_keys[0], min_dist_keys[1]])
        elif not is_merged:
            if min_dist_keys[0] not in circuits[data[min_dist_keys[0]] - 1]: circuits[data[min_dist_keys[0]] - 1].append(min_dist_keys[0])
            if min_dist_keys[1] not in circuits[data[min_dist_keys[0]] - 1]: circuits[data[min_dist_keys[0]] - 1].append(min_dist_keys[1])

    print()
    for j in circuits:
        print(j)
    return(len(circuits))











def part2(data):
    pass

def main():
    with open("2025/Day 8/test.txt", "r") as f:
        data = f.read().splitlines()
    
    parsed_data = {}
    for i in range(len(data)):
        q = tuple(map(int, data[i].split(",")))
        parsed_data[q] = 0

    print(part1(parsed_data))
    print(part2(parsed_data))



if __name__ == "__main__":
    main()