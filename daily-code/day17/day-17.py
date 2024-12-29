# Day 17

# Direct Link to adventofcode.com Day 17
# https://adventofcode.com/2024/day/17

import sys
import re

with open(sys.argv[1], 'r') as f:
    data = f.read()
a, b, c, *program = list(map(int, re.findall(r"\d+", data)))

def computer(a: int, b: int = 0, c: int = 0) -> list[int]:

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
    return output

candidates = [0]
for l in range(len(program)):
    next_candidates = []
    for val in candidates:
        for i in range(8):
            target = (val << 3) + i
            if computer(target) == program[-l-1:]:
                next_candidates.append(target)
    candidates = next_candidates


# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 2,1,3,0,5,2,3,7,1
print(','.join(map(str, computer(a, b, c))))

# ++++++++++++++++++++++++++++++++
## Part 2

# Result is
print(min(candidates))