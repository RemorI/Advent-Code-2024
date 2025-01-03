# Day 21

# Direct Link to adventofcode.com Day 21
# https://adventofcode.com/2024/day/21

import sys
from collections import deque
from itertools import product

with open(sys.argv[1], "r") as f:
    lines = list(map(str.strip, f.readlines()))


def find_best_x_to_y(keypad, x, y):
    if x == y:
        return ["A"]
    # state = r, c, path
    queue = deque([(*x, "")])
    best_length = 100
    optimal_paths = []
    while queue:
        r, c, path = queue.popleft()
        for nr, nc, move in [
            (r + 1, c, "v"),
            (r - 1, c, "^"),
            (r, c + 1, ">"),
            (r, c - 1, "<"),
        ]:
            if (nr, nc) not in keypad:
                continue
            if len(path) + 1 > best_length:
                return optimal_paths
            if (nr, nc) == y:
                optimal_paths.append(path + move + "A")
                best_length = min(len(path) + 2, best_length)
            else:
                queue.append((nr, nc, path + move))
    return optimal_paths


def keys_to_paths(keypad_paths, code):
    paths = [keypad_paths[(b1, b2)] for b1, b2 in zip("A" + code, code)]
    return ["".join(segment) for segment in product(*paths)]


num_pad = {
    (0, 0): "7",
    (0, 1): "8",
    (0, 2): "9",
    (1, 0): "4",
    (1, 1): "5",
    (1, 2): "6",
    (2, 0): "1",
    (2, 1): "2",
    (2, 2): "3",
    (3, 1): "0",
    (3, 2): "A",
}
dir_pad = {
    (0, 1): "^",
    (0, 2): "A",
    (1, 0): "<",
    (1, 1): "v",
    (1, 2): ">",
}

num_pad_paths = {
    (num_pad[p1], num_pad[p2]): find_best_x_to_y(num_pad, p1, p2)
    for p1 in num_pad
    for p2 in num_pad
}
dir_pad_paths = {
    (dir_pad[p1], dir_pad[p2]): find_best_x_to_y(dir_pad, p1, p2)
    for p1 in dir_pad
    for p2 in dir_pad
}

count1 = 0
for code in lines:
    best_length = float("inf")
    for path1 in keys_to_paths(num_pad_paths, code):
        for path2 in keys_to_paths(dir_pad_paths, path1):
            for path3 in keys_to_paths(dir_pad_paths, path2):
                best_length = min(len(path3), best_length)
    count1 += int(code[:-1]) * best_length


# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 184716
print(count1)