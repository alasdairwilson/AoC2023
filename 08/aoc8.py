import numpy as np
import parse
from math import lcm

example = "RL\n\
\n\
AAA = (BBB, CCC)\n\
BBB = (DDD, EEE)\n\
CCC = (ZZZ, GGG)\n\
DDD = (DDD, DDD)\n\
EEE = (EEE, EEE)\n\
GGG = (GGG, GGG)\n\
ZZZ = (ZZZ, ZZZ)".split('\n')

example2 = "LR\n\
\n\
11A = (11B, XXX)\n\
11B = (XXX, 11Z)\n\
11Z = (11B, XXX)\n\
22A = (22B, XXX)\n\
22B = (22C, 22C)\n\
22C = (22Z, 22Z)\n\
22Z = (22B, 22B)\n\
XXX = (XXX, XXX)".split('\n')

def read_input():
    input = open('08/input.txt').read().strip()
    return input.split('\n')

def parse_steps(input):
    steps = {}
    for line in input:
        pattern = "{step:3} = ({L}, {R})"
        match = parse.search(pattern, line)
        steps[match['step']] = { 'L':match['L'], 'R':match['R'] }
    return steps

def recursive_walk(start, sequence, steps, nsteps=0):
    loc = start
    nsteps = 0
    while loc[-1] != 'Z':
        step = np.mod(nsteps, len(sequence))
        loc = steps[loc][sequence[step]]
        nsteps += 1
    return nsteps, loc

def recursive_walk2(starts, sequence, steps, nsteps=0):
    locs = starts
    nsteps = 0
    while np.any([loc[2] != 'Z' for loc in locs]):
        step = np.mod(nsteps, len(sequence))
        locs = [steps[loc][sequence[step]] for loc in locs]
        nsteps += 1
        if np.any([loc[2] == 'Z' for loc in locs]):
            print([loc[2] for loc in locs])
    return nsteps, locs
    
input = read_input()
# input = example

sequence = input[0]
steps = parse_steps(input[2:])
print(recursive_walk('AAA', sequence, steps))

#pt2
# input = example2
# sequence = input[0]
steps = parse_steps(input[2:])
starts = []
for x in steps.keys():
    if x[2] == 'A':
        starts.append(x)
ends = []
for start in starts:
    ends.append(recursive_walk(start, sequence, steps)[0])
ends = np.array(ends, dtype=np.int32)
print(lcm(*ends), np.lcm.reduce(ends, dtype=np.int64))
