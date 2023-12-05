import re
import parse
from pprint import pprint
import numpy as np

example="\seeds: 79 14 55 13\n\
\n\
seed-to-soil map:\n\
50 98 2\n\
52 50 48\n\
\n\
soil-to-fertilizer map:\n\
0 15 37\n\
37 52 2\n\
39 0 15\n\
\n\
fertilizer-to-water map:\n\
49 53 8\n\
0 11 42\n\
42 0 7\n\
57 7 4\n\
\n\
water-to-light map:\n\
88 18 7\n\
18 25 70\n\
\n\
light-to-temperature map:\n\
45 77 23\n\
81 45 19\n\
68 64 13\n\
\n\
temperature-to-humidity map:\n\
0 69 1\n\
1 0 69\n\
\n\
humidity-to-location map:\n\
60 56 37\n\
56 93 4"

def parse_map(m):
    mappings = []
    for i in range(m.shape[0]):
        try:
            mappings.append([m[i][0], m[i][1], m[i][2]])
        except:
            pass
    return mappings

def stupid_map(m):
    map2 = []
    rows = [x.split('\n') for x in m]
    for row in rows:
        x = [y.split() for y in row]
        try:
            z = [int(p) for p in x[0]]
        except:
            print("error",x,row)
        
        map2.append(z)
    return np.array(map2)

seeds, *maps = open('05/input.txt').read().split('\n\n') 
# seeds, *maps = example.split('\n\n')
maps = [(map.split('\n')[1:]) for map in maps]
seeds = [int(seed) for seed in seeds.split()[1:]]

maps2=[]
mappings=[]
for m in maps:
    maps2.append(stupid_map(m))

for i,m in enumerate(maps2):
    mappings.append(parse_map(m))

locations = []
iseeds=seeds.copy()
def propagate(seed):
    for mapping in mappings:
        for j in range(len(mapping)):
            if seed >= mapping[j][1] and seed < mapping[j][1] + mapping[j][2]:
                seed = seed - mapping[j][1] + mapping[j][0]
                break
    return(seed)

for seed in seeds:
    locations.append(propagate(seed))
                     
print(min(locations))
seedrange=[]
for i in np.arange(10):
    seedrange.append([iseeds[2*i], iseeds[2*i+1]])

for seedpair in seedrange:
    print(seedpair)

winner = np.inf
winning_seed=0
winning_seedpair=0
for i, seedpair in enumerate(seedrange):
    n = np.floor(np.sqrt(seedpair[1]))
    seed_no = seedpair[0]
    while seed_no < seedpair[0]+seedpair[1]:
        trial = propagate(seed_no)
        if trial < winner:
            winner = trial
            winning_seed = seed_no
            winning_seedpair = i
        seed_no += n

new_seeds = np.arange(winning_seed-np.floor(np.sqrt(seedrange[winning_seedpair][1])),winning_seed+np.floor(np.sqrt(seedrange[winning_seedpair][1])))
minim = np.inf
winner=0
for seed in new_seeds:
    trial = propagate(seed)
    if trial < minim:
        minim = trial
        winner = seed

print(minimr)
