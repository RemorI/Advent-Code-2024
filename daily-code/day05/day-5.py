# Day 5

# Direct Link to adventofcode.com Day 5
# https://adventofcode.com/2024/day/5

import sys
from collections import defaultdict
from functools import cmp_to_key

with open(sys.argv[1], 'r') as f:
    data = f.read()

rules, orders = data.split("\n\n")
rules = [tuple(map(int, l.split('|'))) for l in rules.splitlines()]
orders = [tuple(map(int, l.split(','))) for l in orders.splitlines()]

wrong_map = defaultdict(bool)
for x, y in rules:
    wrong_map[(x,y)] = False
    wrong_map[(y,x)] = True

def check_order(order: list[int]) -> bool:
    for i in range(len(order)):
        for j in range(i+1, len(order)):
            if wrong_map[(order[i],order[j])]:
                return 0
    return True

def sort_order(a:int, b:int) -> int:
    if wrong_map[(a,b)]:
        return 1
    return -1

count1 = 0
count2 = 0
for order in orders:
    if check_order(order):
        count1 += order[len(order)//2]
    else:
        fixed_order = sorted(order, key=cmp_to_key(sort_order))
        count2 += fixed_order[len(fixed_order)//2]

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 4924
print(count1)

# ++++++++++++++++++++++++++++++++
## Part 2

# Result is 6085
print(count2)