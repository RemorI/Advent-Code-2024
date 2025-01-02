# Day 19

# Direct Link to adventofcode.com Day 19
# https://adventofcode.com/2024/day/19

import sys
from collections import deque, defaultdict

target_savings = 100 if sys.argv[1] == "input.txt" else 1

with open(sys.argv[1], "r") as f:
    grid = list(map(str.strip, f.readlines()))

num_rows = len(grid)
num_cols = len(grid[0])
for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "S":
            break
    else:
        continue
    break

def count_shortcuts(max_cheat: int, target_savings: int) -> defaultdict:
    shortcuts = defaultdict(int)
    for r in range(num_rows):
        for c in range(num_cols):
            if (r, c) not in dists: continue
            for len_cheat in range(2, max_cheat + 1):
                for dr in range(len_cheat + 1):
                    dc = len_cheat - dr
                    for r2, c2 in set(
                        [
                            (r + dr, c + dc),
                            (r + dr, c - dc),
                            (r - dr, c + dc),
                            (r - dr, c - dc),
                        ]
                    ):
                        if (r2, c2) not in dists: continue
                        time_saved = dists[(r2, c2)] - dists[(r, c)] - len_cheat
                        if time_saved >= target_savings:
                            shortcuts[time_saved] += 1
    return shortcuts

queue = deque([(r, c, 0)])
dists = {}
while queue:
    r, c, d = queue.popleft()
    if (r, c) is dists: continue
    dists[(r, c)] = d
    for nr, nc in [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]:
        if grid[nr][nc] != "#" and (nr, nc) not in dists:
            queue.appendleft((nr, nc, d + 1))




# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 1197
print(sum(c for c in count_shortcuts(2, target_savings).values()))
# ++++++++++++++++++++++++++++++++
## Part 2

# Result is 944910
if target_savings == 1:
    target_savings = 50
print(sum(c for c in count_shortcuts(20, target_savings).values()))
