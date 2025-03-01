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

queue = [(0, *start, 0, 1, [start])]
seen = {(*start, 0, 1)}
count1 = None
best_cost = float("inf")
points = set()

while queue:
    cost, r, c, dr, dc, path = heapq.heappop(queue)
    seen.add((r, c, dr, dc))
    if grid[r][c] == "E":
        if not count1:
            count1 = cost
        if cost <= best_cost:
            best_cost = cost
            for point in path:
                points.add(point)
        else:
            break
    if grid[r + dr][c + dc] != "#" and (r + dr, c + dc, dr, dc) not in seen:
        heapq.heappush(queue, (cost + 1, r + dr, c + dc, dr, dc, path + [(r + dr, c + dc)]))
    for ndr, ndc in [(-dc, dr), (dc, -dr)]:
        if (r, c, ndr, ndc) not in seen and grid[r + ndr][c + ndc] != "#":
            heapq.heappush(queue, (cost + 1000, r, c, ndr, ndc, list(path)))


# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 88416
print(count1)

# ++++++++++++++++++++++++++++++++
## Part 2

# Result is 442
print(len(points))