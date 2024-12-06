# Day 1

# Direct Link to adventofcode.com Day 1
# https://adventofcode.com/2024/day/1


import sys

with open(sys.argv[1], 'r') as f:
    lines = [list(map(int, line.split())) for line in f.readlines()]

list1, list2 = list(zip(*lines))

#print(f'1st List: {list1}')
#print(f'2nd List: {list2}')



# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 1222801
print(sum(abs(x1 - x2) for x1, x2 in zip(sorted(list1), sorted(list2))))


# ++++++++++++++++++++++++++++++++
## Part 2

# Result is 22545250
print(sum(x * len([y for y in list2 if y == x]) for x in list1))
