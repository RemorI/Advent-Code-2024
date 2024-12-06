# Day 3

# Direct Link to adventofcode.com Day 3
# https://adventofcode.com/2024/day/3

import sys
import re
from math import prod

with open(sys.argv[1], 'r') as f:
    data = f.read()

valid_mul = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)


# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 167650499
print(sum(prod(map(int, val)) for val in valid_mul))

# ++++++++++++++++++++++++++++++++
## Part 2

# Result is