# Day 6

# Direct Link to adventofcode.com Day 6
# https://adventofcode.com/2024/day/6

import sys

with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))

num_row = len(lines)
num_cols = len(lines[0])

def starter():
    for r, row in enumerate(lines):
        for c, val in enumerate(row):
            if val == "^":
                return (r, c)

r, c = starter()
dr, dc = -1, 0
visited = set()

while True:
    visited.add((r, c))
    if not (0 <= r + dr < num_row and 0 <= c + dc < num_cols):
        break
    if lines[r+dr][c+dc] == "#":
        dc, dr = -dr, dc
    else:
        r += dr
        c += dc





# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 4758
print(len(visited))

# ++++++++++++++++++++++++++++++++
## Part 2

# Result is