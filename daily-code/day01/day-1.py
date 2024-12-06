# Day 1

# Direct Link to adventofcode.com Day 1
# https://adventofcode.com/2024/day/1


import sys

with open(sys.argv[1], 'r') as f:
    lines = [list(map(int, line.split())) for line in f.readlines()]

list1, list2 = list(zip(*lines))

first_list = list1
#print(f'1st List: {first_list}')

second_list = list2
#print(f'2nd List: {second_list}')

# Result is 1222801
#print(sum(abs(x1 - x2) for x1, x2 in zip(sorted(list1), sorted(list2))))