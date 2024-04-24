from itertools import permutations

f = open('2015/Day 9/input.txt', 'r')
lines = [l.strip().split() for l in f.readlines()]

d = {}
for l in lines:
    d[l[0], l[2]] = int(l[4])
    d[l[2], l[0]] = int(l[4])

places = list(set(l[0] for l in d.keys()))


shortest = float('inf')

for p in permutations(places):
    length = sum(d[p[i], p[i + 1]] for i in range(len(p) - 1))
    shortest = min(shortest, length)

print(shortest)