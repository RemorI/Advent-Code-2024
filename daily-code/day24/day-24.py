# Day 24

# Direct Link to adventofcode.com Day 24
# https://adventofcode.com/2024/day/24

import sys
import re
from dataclasses import dataclass

@dataclass
class Connection:
    in1: str
    in2: str
    op: str
    out: str

operations = {
    "OR": lambda x1, x2: x1 | x2,
    "AND": lambda x1, x2: x1 & x2,
    "XOR": lambda x1, x2: x1 ^ x2
}

with open(sys.argv[1], "r") as f:
    bits, connections = f.read().split("\n\n")
init_pairs = re.findall(r'(.{3}): ([01])', bits)
init = {k: int(v) for k, v in init_pairs}
map_str = connections.splitlines()

wire_map = {}
for wire in map_str:
    in1, op, in2, _, out = wire.strip().split(" ")
    wire_map[out] = Connection(in1, in2, op, out)

def run_wire(w:str):
    if w in init:
        return init[w]
    conn = wire_map[w]
    return operations[conn.op](run_wire(conn.in1), run_wire(conn.in2))

result = [
    run_wire(w)
    for w in sorted([w for w in wire_map if w.startswith("z")], reverse=True)
]

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 56620966442854
print(int("".join(map(str, result)), 2))