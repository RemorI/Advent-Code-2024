# Day 3

# Direct Link to adventofcode.com Day 3
# https://adventofcode.com/2024/day/3

import sys
import re
from math import prod

with open(sys.argv[1], 'r') as f:
    data = f.read()

valid_mul = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)

part2= 0
enabled = True
for inst in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data):
    match inst:
        case "do()":
            enabled = True
        case "don't()":
            enabled = False
        case _:
            x, y = map(int, inst[4:-1].split(','))
            if enabled:
                part2 += x*y



# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 167650499
print(sum(prod(map(int, val)) for val in valid_mul))

# ++++++++++++++++++++++++++++++++
## Part 2

# Result is 95846796
print(part2)