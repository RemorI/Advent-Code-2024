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

def move_reader(movy: int, movx: int, count_y: int, count_x: int) -> list[list[str]]:
    if 0<=r+movy<num_row and 0<=c+movx<num_cols:
        if grid[r+movy][c+movx] != "#": 
            if  grid[r+movy][c+movx] != "O": 
                grid[r+movy][c+movx] = "@"
                grid[r][c] = "."
            else: 
                while grid[r+count_y][c+count_x] == "O":
                    count_y += movy
                    count_x += movx
                if grid[r+count_y][c+count_x] != "#":
                    grid[r+count_y][c+count_x] = "O"
                    grid[r+movy][c+movx] = "@"
                    grid[r][c] = "."
        return grid

def starter():
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "@":
                return (r, c)
            
for move in movement:
    r, c = starter()
    if move == "^":
        grid = move_reader(-1, 0, -2, 0)
    elif move == "v":
        grid = move_reader(1, 0, 2, 0)
    elif move == ">":
        grid = move_reader(0, 1, 0, 2)
    elif move == "<":
        grid = move_reader(0, -1, 0, -2)
    print(f"Movimiento: {move}")
    print('\n'.join(map(str, grid)))


count1 = 0   
for a, rowa in enumerate(grid):
    for b, valb in enumerate(rowa):
        if valb == "O":
            count1 += (100*a)+b




print(count1)

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 1371036

# ++++++++++++++++++++++++++++++++
## Part 2

# Result is