# Day 15

# Direct Link to adventofcode.com Day 15
# https://adventofcode.com/2024/day/15

import sys

with open(sys.argv[1], 'r') as f:
    grid, movement = f.read().split('\n\n')

movement = list(map(str, movement))
grid = list(map(str, grid.split("\n")))
num_row = len(grid)
num_cols = len(grid[0])
left, right, up, down = "<", ">", "^", "v"


print(num_row, num_cols)


print(num_row, num_cols)

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is