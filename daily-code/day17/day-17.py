# Day 16

# Direct Link to adventofcode.com Day 16
# https://adventofcode.com/2024/day/16

import sys
import re

with open(sys.argv[1], 'r') as f:
    data = f.read()
a, b, c, *program = list(map(int, re.findall(r"\d+", data)))

def combo(val: int) -> int:
    assert val != 7, "Invalid combo value"
    if val <= 3: return val
    reg_map = {4: a, 5: b, 6: c}
    return reg_map[val]

output = []
ip = 0
while ip < len(program):
    opcode = program[ip]
    operand = program[ip + 1]
    match opcode:
        case 0: #adv
            a = a >> combo(operand)
        case 1: #bxl
            b = b ^ operand
        case 2: #bst
            b = combo(operand) % 8
        case 3: #jnz
            if a != 0:
                ip = operand
                continue
        case 4: #bxc
            b = b ^ c
        case 5: #out
            output.append(combo(operand) % 8)
        case 6: #bdv
            b = a >> combo(operand)
        case 7: #cdv
            c = a >> combo(operand)
    ip +=2        

print(a, b, c, program)
print(','.join(map(str, output)))

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is