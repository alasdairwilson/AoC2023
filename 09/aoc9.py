import numpy as np

example="0 3 6 9 12 15\n\
1 3 6 10 15 21\n\
10 13 16 21 30 45"
example = example.split('\n')
example = [[int(x) for x in y.split()] for y in example]


def read_input():
    input = open('09/input.txt').read().strip().split('\n')
    input = [[int(x) for x in y.split()] for y in input]
    return input

def rec_diffs(input):
    current = input[-1]
    if np.sum(current) != 0:
        input.append(np.diff(current))
        rec_diffs(input)
    return input
   
input = read_input()
# input = example

print(input)
x = rec_diffs([np.array(input[:][0])])
diffs=[]
for line in input:
    x = rec_diffs([np.array(line)])
    diffs.append(x)

# pt1
next_val = []
for diff in diffs:
    next_val.append(np.sum([x[-1] for x in diff]))
print(np.sum(next_val))

# pt2
prev_val=[]
for diff in diffs:
    pv = diff[0][0]
    for i in range(len(diff)-1):
        if i%2 == 0:
            pv = pv - diff[i+1][0]
        else:
            pv = pv + diff[i+1][0]
    prev_val.append(pv)

print(np.sum(prev_val))