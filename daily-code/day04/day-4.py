# Day 4

# Direct Link to adventofcode.com Day 4
# https://adventofcode.com/2024/day/4

import sys
import numpy as np
from collections import defaultdict
import pandas as pd

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

prueba = np.array(lines)

result = []
char_map = defaultdict(set)
for i in range(len(prueba)):
    result.append(list(prueba[i]))

df = pd.DataFrame(result)
fila, columna = df.shape

coordenadas = [(x, y) for x, resu in enumerate(result) for y, char in enumerate(resu) if char == 'X']
compro = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

part1=0
for x,y in coordenadas:
    for cr, cp in compro:
        xM,yM=x+cr, y+cp
        if result[xM][yM] == 'M':
            coor_M = (xM,yM)
            xA, yA= xM+cr, yM+cp
            if result[xA][yA] == 'A':
                coor_A = (xA,yA)
                xS, yS = xA+cr, yA+cp
                if result[xS][yS] == 'S':
                    part1 +=1

print(part1)
# ++++++++++++++++++++++++++++++++
## Part 1

# Result is