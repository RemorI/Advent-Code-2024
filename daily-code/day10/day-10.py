# Day 10

# Direct Link to adventofcode.com Day 10
# https://adventofcode.com/2024/day/10

import sys
from collections import deque

with open(sys.argv[1], 'r') as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

zeros = [(r, c) for r, row in enumerate(grid) for c, val in enumerate(row) if val == 0]
rows = len(grid)
cols = len(grid[0])

def count_trails(r: int, c: int) -> tuple[int]:
    queue = deque([(r, c)])
    summits = set()
    count = 0
    while queue:
        r, c = queue.popleft()
        if grid[r][c] == 9:
            summits.add((r, c))
            count +=1
            continue
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[r][c] +1 == grid[nr][nc]:
                queue.append((nr, nc))
    return count



# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 744
print(sum(count_trails(*zero) for zero in zeros))


# ++++++++++++++++++++++++++++++++
## Part 2

# Result is
print(sum(count_trails(*zero) for zero in zeros))