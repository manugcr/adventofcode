# fck recursion

print('--- Day 12: Hot Springs ---')

with open('input.txt', 'r') as file:
    lines = file.read().strip().split('\n')

def count_arrangements(cfgs, nums):
    if cfgs == '':
        return 1 if nums == () else 0
    if nums == ():
        return 0 if '#' in cfgs else 1

    result = 0

    if cfgs[0] in '.?':
        result += count_arrangements(cfgs[1:], nums)

    if cfgs[0] in '#?':
        if nums[0] <= len(cfgs) and '.' not in cfgs[:nums[0]] and (nums[0] == len(cfgs) or cfgs[nums[0]] != '#'):
            result += count_arrangements(cfgs[nums[0] + 1:], nums[1:])

    return result

cfgs = []
nums = []
answer = 0
for line in lines:
    cfgs, nums = line.split()
    nums = tuple(map(int, nums.split(',')))
    answer += count_arrangements(cfgs, nums)

print('Answer is: ', answer)