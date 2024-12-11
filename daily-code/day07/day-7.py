# Day 6

# Direct Link to adventofcode.com Day 6
# https://adventofcode.com/2024/day/6

import sys

with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))

def check_result(target: int, nums:list[int]) -> bool:
    if len(nums) == 1:
        return target == nums[0]
    num = nums.pop()
    if target / num == target // num:
        if check_result(target // num, nums[:]):
            return True
    if target - num >= 0:
        if check_result(target - num, nums[:]):
            return True
    return False

count1 = 0
for line in lines:
    target = int(line.split(':')[0])
    nums = list(map(int, line.split(': ')[1].split(' ')))
    print(target, nums)
    if check_result(target, nums):
        count1 += target

# ++++++++++++++++++++++++++++++++
## Part 1

# Result is 465126289353
print(count1)

# ++++++++++++++++++++++++++++++++
## Part 2

# Result is