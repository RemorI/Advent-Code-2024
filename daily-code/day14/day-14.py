# Day 14

# Direct Link to adventofcode.com Day 14
# https://adventofcode.com/2024/day/14

import sys
import re
import math

with open(sys.argv[1], 'r') as f:
    robots = f.read().split('\n')

height = 103
width = 101

quadrant = [0] * 4
def getting_data(robot: str) -> tuple[int]:
    px, py = tuple(map(int, re.findall(r'p\=(\d+),(\d+)', robot)[0]))
    vx, vy = tuple(map(int, re.findall(r'v\=([-]?\d+),([-]?\d+)', robot)[0]))
    pxF = (px + (vx * 100)) % width
    pyF = (py + (vy * 100)) % height

    midw, midh = width // 2, height // 2
    if pxF < midw:
        if pyF < midh:
            quadrant[0] += 1
        if pyF > midh:
            quadrant[1] += 1
    elif pxF > midw:
        if pyF < midh:
            quadrant[2] += 1
        if pyF > midh:
            quadrant[3] += 1
    return quadrant

for robot in robots:
    q = getting_data(robot)


# +x -> right
# -x -> left
# +y -> down
# -y -> up
# example_space = (7, 11)
# space = (103, 101)
# simulation_time = 100

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 209409792
print(math.prod(q))

# ++++++++++++++++++++++++++++++++
## Part 2

# Result is