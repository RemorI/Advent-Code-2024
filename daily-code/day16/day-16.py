# Day 16

# Direct Link to adventofcode.com Day 16
# https://adventofcode.com/2024/day/16

import sys
import heapq

with open(sys.argv[1], 'r') as f:
    grid = list(map(str.strip, f.readlines()))

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "S":
            start = (r, c)
            break
    else:
        continue
    break

queue = [(0, *start, 0, 1)]
seen = {(*start, 0, 1)}

while queue:
    cost, r, c, dr, dc = heapq.heappop(queue)
    seen.add((r, c, dr, dc))
    if grid[r][c] == "E":
        count1 = cost
        break
    if grid[r + dr][c + dc] != "#" and (r + dr, c + dc, dr, dc) not in seen:
        heapq.heappush(queue, (cost + 1, r + dr, c + dc, dr, dc))
    for ndr, ndc in [(-dc, dr), (dc, -dr)]:
        if (r, c, ndr, ndc) not in seen:
            heapq.heappush(queue, (cost + 1000, r, c, ndr, ndc))


# ++++++++++++++++++++++++++++++++
## Part 1

# Result is
print(count1)

