# Day 22

# Direct Link to adventofcode.com Day 22
# https://adventofcode.com/2024/day/22

import sys
from collections import defaultdict

with open(sys.argv[1], "r") as f:
    pairs = [l.strip().split('-') for l in f.readlines()]

passwords = set()
def build_set(conn: str, group: set[str]) -> None:
    password = ','.join(sorted(group))
    if password in passwords: return
    passwords.add(password)
    for neighbor in conns[conn]:
        if neighbor in group: continue
        if any(neighbor not in conns[node] for node in group): continue
        build_set(neighbor, {*group, neighbor})


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

for conn in conns:
    build_set(conn, {conn})

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is
print(len([t for t in triples if any(x.startswith("t") for x in t)]))

# ++++++++++++++++++++++++++++++++
## Part 2

# Result is
print(max(passwords, key=len))