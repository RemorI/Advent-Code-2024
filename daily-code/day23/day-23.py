# Day 22

# Direct Link to adventofcode.com Day 22
# https://adventofcode.com/2024/day/22

import sys
from collections import defaultdict

with open(sys.argv[1], "r") as f:
    pairs = [l.strip().split('-') for l in f.readlines()]

conns = defaultdict(set)
for a, b in pairs:
    conns[a].add(b)
    conns[b].add(a)

triples = set()
for conn in conns:
    for neighbor in conns[conn]:
        for nn in conns[neighbor]:
            if conn in conns[nn]:
                triples.add(tuple(sorted([conn, neighbor, nn])))



# ++++++++++++++++++++++++++++++++
## Part 1

# Result is
print(len([t for t in triples if any(x.startswith("t") for x in t)]))