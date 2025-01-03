# Day 22

# Direct Link to adventofcode.com Day 22
# https://adventofcode.com/2024/day/22

import sys
from collections import defaultdict

with open(sys.argv[1], "r") as f:
    numbers = list(map(int, f.readlines()))


def next_num(x: int) -> int:
    x ^= (x * 64) % 16777216
    x ^= (x // 32) % 16777216
    x ^= (x * 2048) % 16777216
    return x

count1 = 0
seq_totals = defaultdict(int)
for num in numbers:
    seen = set()
    outputs = [(num := next_num(num)) % 10 for _ in range(2000)]
    count1 += num
    diffs = [y - x for x, y in zip(outputs, outputs[1:])]
    for n, *seq in zip(outputs[4:], diffs, diffs[1:], diffs[2:], diffs[3:]):
        seq = tuple(seq)
        if seq in seen: continue
        seen.add(seq)
        seq_totals[seq] += n


# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 15613157363
print(count1)

# ++++++++++++++++++++++++++++++++
## Part 2

# Result is 1784
print(seq_totals[max(seq_totals, key=seq_totals.get)])