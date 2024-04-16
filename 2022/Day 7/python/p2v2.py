file = open("2022/Day 7/inputv2.txt").read().split("\n")

folders = dict()
current_dir = [""]

for row in file:
    if row.startswith('$'):
        if row == '$ cd ..':
            current_dir.pop()
        elif row.startswith('$ cd '):
            current_dir.append(row[5:])
    else:
        if not row.startswith('dir '):
            size = int(row.split(' ')[0])
            path = ""
            for dir in current_dir:
                path += "/" + dir
                if not path in folders:
                    folders[path] = 0
                folders[path] += size

min_free_up_space = folders["/"] - 70000000 + 30000000

print(min([s for f, s in folders.items() if s > min_free_up_space]))