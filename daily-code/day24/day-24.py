# Day 24

# Direct Link to adventofcode.com Day 24
# https://adventofcode.com/2024/day/24

import sys
import re

with open(sys.argv[1], "r") as f:
    bits, connections = f.read().split("\n\n")
init_pairs = re.findall(r'(.{3}): ([01])', bits)
init = {k: int(v) for k, v in init_pairs}
map_str = connections.splitlines()

wire_map = {}
for wire in map_str:
    in1, op, in2, _, out = wire.strip().split(" ")
    wire_map[out]

print(init, map_str)


operations = {
    "OR": lambda x1, x2: x1 | x2,
    "AND": lambda x1, x2: x1 & x2,
    "XOR": lambda x1, x2: x1 ^ x2
}

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is