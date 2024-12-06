# Day 2

# Direct Link to adventofcode.com Day 2
# https://adventofcode.com/2024/day/2

import sys

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

def count_reports(line: str) -> bool:
    reports = list(map(int, line.split(' ')))
    if not all(1 <= c <= 3 for c in [abs(x1 - x2) for x1, x2 in zip(reports, reports[1:])]):
        return False
    if all(x1 < x2 for x1, x2 in zip(reports, reports[1:])):
        return True
    if all(x1 > x2 for x1, x2 in zip(reports, reports[1:])):
        return True
    return False

# ++++++++++++++++++++++++++++++++
## Part 1

# Result 407
print(len([r for r in lines if count_reports(r)]))


# ++++++++++++++++++++++++++++++++
## Part 2

