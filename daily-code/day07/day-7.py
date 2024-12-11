# Day 7

# Direct Link to adventofcode.com Day 7
# https://adventofcode.com/2024/day/7

import sys

with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))

def check_result(target: int, nums:list[int], count2 = False) -> bool:
    if len(nums) == 1:
        return target == nums[0]
    num = nums.pop()
    if target / num == target // num:
        if check_result(target // num, nums[:], count2 = count2):
            return True
    if target - num >= 0:
        if check_result(target - num, nums[:], count2 = count2):
            return True
    if not count2:
        return False
    target_str = str(target)
    num_str = str(num)
    if target_str.endswith(num_str) and len(target_str) > len(num_str):
        new_target = int(target_str[:-len(num_str)])
        if check_result(new_target, nums[:], count2=count2):
            return True
    return False

count1 = 0
count2 = 0
for line in lines:
    target = int(line.split(':')[0])
    nums = list(map(int, line.split(': ')[1].split(' ')))
    if check_result(target, nums[:]):
        count1 += target
    if check_result(target, nums[:], count2=True):
        count2 += target

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 465126289353
print(count1)

# ++++++++++++++++++++++++++++++++
## Part 2

# Result is
print(count2)