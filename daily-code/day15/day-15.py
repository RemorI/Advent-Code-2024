# Day 15

# Direct Link to adventofcode.com Day 15
# https://adventofcode.com/2024/day/15

import sys

with open(sys.argv[1], 'r') as f:
    grid, movement = f.read().split('\n\n')

movement = list(map(str, movement))
grid = [list(map(str, line)) for line in grid.splitlines()]
num_row = len(grid)
num_cols = len(grid[0])
#up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)



for r, row in enumerate(grid):
    for c, col in enumerate(grid[0]):
        if grid[r][c] == "@":
            rro, cro = r, c
        for move in movement:
            if "^":
                if grid[r-1][c] == "#": #
                    continue
                if not grid[r-1][c] == "O" and not grid[r-1][c] == "#": #
                    rro, cro = (r-1, c)
                    grid[rro][cro] = "@"
                    grid[r][c] = "."
                if  grid[r-1][c] == "O": #
                    if grid[r-2][c] == "#": #
                        continue
                    else:
                        grid[rro][cro] = "@"
                        grid[r][c] = "."
                        count = -2#
                        while grid[r+count][c] == "O" and not grid[r+count-1][c] == "#":
                            grid[r+count-1][c] = "O"
                            count += 1#

# O O @ .

print(grid)
print(len(movement))

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is