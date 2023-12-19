import numpy as np
from pprint import pprint

example ="""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

def read_input():
    input = open('11/input.txt').read().strip().split('\n')
    return input

def expand_input(input):
    penalty_indices=[]
    output=[]
    for i, line in enumerate(input):
        output.append(line)
        if not '#' in line:
            penalty_indices.append(i)
    return np.array(output), penalty_indices

def transpose_map(map):
    map_out=np.empty([len(map[0]),len(map)], dtype=str)
    for i in range(len(map)):
        for j in range(len(map[0])):
            map_out[j][i] = map[i][j]
    return map_out

def index_gals(map):
    gal_dict={}
    gal=0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '#':
                gal_dict[gal] = [i,j]
                gal += 1
    return gal_dict

input = read_input()
# input = example.split('\n')

map, penalty_rows = expand_input(input)
m_t = transpose_map(map)
m_2, penalty_cols = expand_input(m_t)
m = transpose_map(m_2)

penalty_rows = np.array(penalty_rows)
penalty_cols = np.array(penalty_cols)
gals = index_gals(m)


def gal_dists(gals, penalty=1):
    dists=[]
    for i, gal in enumerate(gals):
        for j, gal in enumerate(gals):
            if j > i:
                dist = np.abs(gals[i][0] - gals[j][0]) + np.abs(gals[i][1] - gals[j][1])
                dist += penalty*penalty_count(gals[i], gals[j])
                dists.append(dist)
    return dists

def penalty_count(gal1, gal2):
    count = 0
    count += len(penalty_rows[(penalty_rows > min(gal1[0], gal2[0])) & (penalty_rows < max(gal1[0], gal2[0]))])
    count += len(penalty_cols[(penalty_cols > min(gal1[1], gal2[1])) & (penalty_cols < max(gal1[1], gal2[1]))])
    return count

print(np.sum(gal_dists(gals, penalty=1)))
print(np.sum(gal_dists(gals, penalty=9999999999)))
