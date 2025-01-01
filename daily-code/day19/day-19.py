# Day 19

# Direct Link to adventofcode.com Day 19
# https://adventofcode.com/2024/day/19


import sys
from functools import cache

with open(sys.argv[1], "r") as f:
    options = f.readline().strip().split(", ")
    f.readline()
    targets = f.read().strip().split("\n")

@cache
def count_combinations(target: str) -> int:
    if target == "":
        return 1
    count = 0
    for option in options:
        if target.startswith(option):
            count += count_combinations(target[len(option) :])
    return count

combinations = [count_combinations(t) for t in targets]
count1 = len([c for c in combinations if c != 0])


# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 317
print(count1)

# ++++++++++++++++++++++++++++++++
## Part 2

# Result is 883443544805484
print(sum(combinations))