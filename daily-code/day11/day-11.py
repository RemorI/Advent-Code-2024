# Day 11

# Direct Link to adventofcode.com Day 11
# https://adventofcode.com/2024/day/11

import sys

with open(sys.argv[1], 'r') as f:
    stones = list(map(int, f.read().strip().split(" ")))

for _ in range(25):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            new_stones.append(int(str(stone)[len(str(stone))//2:]))
            new_stones.append(int(str(stone)[:len(str(stone))//2]))
        else:
            new_stones.append(stone * 2024)
    stones = new_stones

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 211306
print(len(stones))