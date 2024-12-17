# Day 13

# Direct Link to adventofcode.com Day 13
# https://adventofcode.com/2024/day/13

import sys
import re

with open(sys.argv[1], 'r') as f:
    puzzles = f.read().split('\n\n')

def solve_puzzle(puzzle: str, offset: int = 0) -> tuple[int]:
    a1, a2 = tuple(map(int, re.findall(r'Button A: X\+(\d+), Y\+(\d+)', puzzle)[0]))
    b1, b2 = tuple(map(int, re.findall(r'Button B: X\+(\d+), Y\+(\d+)', puzzle)[0]))
    c1, c2 = tuple(map(int, re.findall(r'Prize: X=(\d+), Y=(\d+)', puzzle)[0]))
    c1 += offset
    c2 += offset

    x = ((c1*b2) - (b1*c2)) / ((a1*b2) - (b1*a2))
    y = ((a1*c2) - (c1*a2)) / ((a1*b2) - (b1*a2))

    if int(x) == x and int(y) == y:
        return tuple(map(int, (x, y)))
    return (0, 0)

count1 = 0
count2 = 0
for puzzle in puzzles:
    a, b = solve_puzzle(puzzle)
    count1 += a*3+b
    a2, b2 = solve_puzzle(puzzle, offset=10000000000000)
    count2 += a2*3+b2


# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 38839
print(count1)

# ++++++++++++++++++++++++++++++++
## Part 2

# Result is 75200131617108
print(count2)