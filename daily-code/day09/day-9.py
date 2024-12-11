# Day 9

# Direct Link to adventofcode.com Day 9
# https://adventofcode.com/2024/day/9

import sys

with open(sys.argv[1], 'r') as f:
    data = list(map(int, f.read().strip()))

disk = []
for i in range(0, len(data), 2):
    disk.extend(data[i] * [i//2])
    if i + 1 < len(data):
        disk.extend(data[i+1] * [-1])

empties = [i for i, val in enumerate(disk) if val == -1]
i=0
while True:
    while disk[-1] == -1: disk.pop()
    target = empties[i]
    if target >= len(disk):
        break
    disk[target] = disk.pop()
    i += 1

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 6399153661894
print(sum(i*val for i, val in enumerate(disk)))


# ++++++++++++++++++++++++++++++++
## Part 2

# Result is