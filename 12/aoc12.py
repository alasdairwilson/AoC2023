import numpy as np
import re
from functools import cache

example="""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

lines = open("12/input.txt").read().strip().split('\n')
# lines = example.split('\n')
cases = []
for line in lines:
    string, nums = line.split(' ')
    string = string.strip('.')
    string = re.sub(r'\.+', '.', string)
    groups = [int(x) for x in nums.split(',')]
    cases.append((string, groups))

@cache
def rec(string, groups):
    # we have completed the recursion if no groups are left
    if not groups:
        return '#' not in string
    seq_len = len(string)
    current_group = groups[0]
    # if this is true then we do not have enough chars to fill all groups
    if seq_len - np.sum(groups) - len(groups) + 1 < 0:
        return 0
    has_gaps = any(string[x] == '.' for x in range(current_group))
    if seq_len == current_group:
        return 0 if has_gaps else 1
    # if there are gaps or if it ends in a # then it cant be possible
    possible = not has_gaps and (string[current_group] != '#')
    # if it starts with a # then it must have n consecutive #s, if it doesn't then it cant be possible
    if string[0] == '#':
        return rec(string[current_group+1:].lstrip('.'), tuple(groups[1:])) if possible else 0
    # we can strip leading . and recurse
    skip = rec(string[1:].lstrip('.'), groups)
    # exhausted possibilities
    if not possible:
        return skip
    return skip + rec(string[current_group+1:].lstrip('.'), tuple(groups[1:]))

total_arrangements = 0
for case in cases:
    string, groups = case
    arrangements= rec(string, tuple(groups))
    total_arrangements += arrangements
print(total_arrangements)

cases=[]
for line in lines:
    string, nums = line.split(' ')
    string = re.sub(r'\.+', '.', string)
    print(string)
    groups = [int(x) for x in nums.split(',')]
    string = '?'.join([string] * 5).lstrip('.')
    groups = groups*5
    cases.append((string, groups))

total_arrangements = 0
for case in cases:
    string, groups = case
    arrangements= rec(string, tuple(groups))
    total_arrangements += arrangements
print(total_arrangements)