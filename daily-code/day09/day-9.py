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

isfile = True
files = {}
spaces = []
ptr = 0
for i, size in enumerate(data):
    if isfile:
        files[i//2] = (ptr, size)
    else:
        spaces.append((ptr, size))
    isfile = not isfile
    ptr += size

for fid in reversed(files):
    loc, file_size = files[fid]
    space_id = 0
    while space_id < len(spaces):
        space_loc, space_size = spaces[space_id]
        if space_loc > loc:
            break
        if space_size == file_size:
            files[fid] = (space_loc, file_size)
            spaces.pop(space_id)
            break
        if space_size >file_size:
            files[fid] = (space_loc, file_size)
            spaces[space_id] = (space_loc + file_size, space_size - file_size)
            break
        space_id += 1
# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 6399153661894
print(sum(i*val for i, val in enumerate(disk)))


# ++++++++++++++++++++++++++++++++
## Part 2

# Result is 6421724645083
count2 = 0
for fid, (loc, size) in files.items():
    for i in range(loc, loc + size):
        count2 += fid * i
print(count2)