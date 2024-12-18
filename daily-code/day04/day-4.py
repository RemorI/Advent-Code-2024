# Day 4

# Direct Link to adventofcode.com Day 4
# https://adventofcode.com/2024/day/4

import sys
from collections import defaultdict

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

char_map = defaultdict(set)
for r, row in enumerate(lines):
    for c, val in enumerate(row):
        char_map[val].add((r,c))

count1 = 0
for r, c in char_map["X"]:
    for dr, dc in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        for i, char in enumerate("MAS", 1):
            if (r + (dr * i), c + (dc * i)) not in char_map[char]:
                break
        else:
            count1 += 1

upleft = lambda r, c: (r - 1, c - 1)
upright = lambda r, c: (r - 1, c + 1)
downleft = lambda r, c: (r + 1, c - 1)
downright = lambda r, c: (r + 1, c + 1)

count2 = 0
for r, c in char_map["A"]:
    if upleft(r, c) in char_map["M"]:
        if downleft(r, c) in char_map["M"] and upright(r, c) in char_map["S"] and downright(r, c) in char_map["S"]:
            count2 += 1
        if upright(r, c) in char_map["M"] and downleft(r, c) in char_map["S"] and downright(r, c) in char_map["S"]:
            count2 += 1
    if downright(r, c) in char_map["M"]:
        if downleft(r, c) in char_map["M"] and upright(r, c) in char_map["S"] and upleft(r, c) in char_map["S"]:
            count2 += 1
        if upright(r, c) in char_map["M"] and downleft(r, c) in char_map["S"] and upleft(r, c) in char_map["S"]:
            count2 += 1

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 2578
print(count1)

# ++++++++++++++++++++++++++++++++
## Part 2

# Result is 1972
print(count2)