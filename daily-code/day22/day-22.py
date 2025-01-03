# Day 22

# Direct Link to adventofcode.com Day 22
# https://adventofcode.com/2024/day/22

import sys

with open(sys.argv[1], "r") as f:
    numbers = list(map(int, f.readlines()))


def next_num(x: int) -> int:
    x ^= (x * 64) % 16777216
    x ^= (x // 32) % 16777216
    x ^= (x * 2048) % 16777216
    return x

count1 = 0
for num in numbers:
    for _ in range(2000):
        num = next_num(num)
    count1 += num

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 15613157363
print(count1)