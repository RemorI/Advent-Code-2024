# Day 8

# Direct Link to adventofcode.com Day 8
# https://adventofcode.com/2024/day/8

import sys
from collections import defaultdict
from itertools import combinations

with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))

antenna = defaultdict(set)
num_rows = len(lines)
num_cols = len(lines[0])

for r, line in enumerate(lines):
    for c, val in enumerate(line):
        if val != '.':
            antenna[val].add((r, c))

antinodes = set()
antinodes2 = set()
for freq in antenna:
    for (r1, c1), (r2, c2) in combinations(antenna[freq], 2):
        antinodes.add((2*r1 - r2, 2*c1 - c2))
        antinodes.add((2*r2 - r1, 2*c2 - c1))
        dr = r2 - r1
        dc = c2 - c1
        r, c = r1, c1
        while 0 <= r < num_rows and 0 <= c < num_cols:
            antinodes2.add((r, c))
            r += dr
            c += dc
        r, c = r1, c1
        while 0 <= r < num_rows and 0 <= c < num_cols:
            antinodes2.add((r, c))
            r -= dr
            c -= dc

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 327
print(sum(1 for r, c in antinodes if 0 <= r < num_rows and 0 <= c < num_cols))

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 1233
print(len(antinodes2))