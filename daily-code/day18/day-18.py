# Day 18

# Direct Link to adventofcode.com Day 18
# https://adventofcode.com/2024/day/18

import sys
from collections import deque

if sys.argv[1] == "input.txt":
    num_rows = 71
    num_cols = 71
    part1_num = 1024
else:
    num_rows = 7
    num_cols = 7
    part1_num = 12

with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))

blocks = [tuple(map(int, line.split(',')))[::-1] for line in lines]

def count_steps(num_blocks: int) -> int:
    queue = deque([(0, 0, 0)])
    seen = set((0, 0))
    while queue:
        r, c, d = queue.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        if r == num_rows -1 and c == num_cols -1:
            return d
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = r + dr, c+ dc
            if 0 <=nr < num_rows and 0 <= nc < num_cols and (nr, nc) not in blocks[:num_blocks]:
                queue.append((nr, nc, d + 1))
    return -1

lo, hi = 0, len(blocks) - 1
while lo < hi:
    mid = (lo + hi) // 2
    if count_steps(mid + 1) != -1:
        lo = mid + 1
    else:
        hi = mid

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 282
print(count_steps(part1_num))

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 64,29
print(",".join(str(x) for x in blocks[lo][::-1]))