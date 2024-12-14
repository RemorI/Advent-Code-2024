# Day 11

# Direct Link to adventofcode.com Day 11
# https://adventofcode.com/2024/day/11

import sys
from functools import cache

with open(sys.argv[1], 'r') as f:
    stones = list(map(int, f.read().strip().split(" ")))

# for _ in range(75):
#     new_stones = []
#     for stone in stones:
#         if stone == 0:
#             new_stones.append(1)
#         elif len(str(stone)) % 2 == 0:
#             new_stones.append(int(str(stone)[len(str(stone))//2:]))
#             new_stones.append(int(str(stone)[:len(str(stone))//2]))
#         else:
#             new_stones.append(stone * 2024)
#     stones = new_stones

@cache
def count_stones(val: int, blinks: int) -> int:
    if blinks == 0:
        return 1
    if val == 0:
        return count_stones(1, blinks-1)
    str_val = str(val)
    len_str_val = len(str_val)
    if len_str_val % 2 == 0:
        return count_stones(int(str_val[:len_str_val//2]), blinks-1) + count_stones(int(str_val[len_str_val//2:]), blinks-1)
    return count_stones(val * 2024, blinks-1)



# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 211306
print(sum(count_stones(s, 25) for s in stones))

# ++++++++++++++++++++++++++++++++
## Part 2

# Result is 250783680217283
print(sum(count_stones(s, 25) for s in stones))