import numpy as np

maps = open('13/input.txt').read().split('\n\n')
example = "#.##..##.\n\
..#.##.#.\n\
##......#\n\
##......#\n\
..#.##.#.\n\
..##..##.\n\
#.#.##.#."
example2 = "#...##..#\n\
#....#..#\n\
..##..###\n\
#####.##.\n\
#####.##.\n\
..##..###\n\
#....#..#"
def in_map(map, i, j):
    if i not in range(len(map)):
        return False
    if j not in range(len(map[0])):
        return False
    return True
    
def reflect_rows(matrix, start_row):
    #check if the start row is past the halfway point
    if start_row > matrix.shape[0]//2:
        # then flip the left half of the matrix
        return np.concatenate((matrix[:start_row, :], np.flipud(matrix[:start_row, :])), axis=0)
    else: # flip the right half of the matrix
        return np.concatenate((np.flipud(matrix[start_row:, :]), matrix[start_row:, :]), axis=0)

def reflect_cols(matrix, start_col):
    if start_col > matrix.shape[1]//2:
        return np.concatenate((matrix[:, :start_col], np.fliplr(matrix[:, :start_col])), axis=1)
    else:
        return np.concatenate((np.fliplr(matrix[:, start_col:]), matrix[:, start_col:]), axis=1)

def count_differences(map1, map2):
    count = 0
    for i in range(len(map1)):
        for j in range(len(map1[0])):
            if map1[i][j] != map2[i][j]:
                count += 1
    return count

map = np.array([s for s in maps[0]])
map = example2.split('\n')
map = np.array([[s for s in row] for row in map])
print(map)

def count_total(maps,target):
    total = 0
    for im, map in enumerate(maps):
        map = map.split('\n')
        map = np.array([[s for s in row] for row in map])
        for i in np.arange(1,map.shape[0]-1):
            x = count_differences(map, reflect_rows(map, i))
            if x==target:
                print(im, 'col')
                total+=i*100
                break
        for i in np.arange(1,map.shape[1]-1):
            x = count_differences(map, reflect_cols(map, i))
            if x==target:
                print(im, 'row')
                total+=i
                break
    return total

print(count_total(maps, 0))
print(count_total(maps, 1))