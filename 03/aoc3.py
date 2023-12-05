import pprint
import parse
import numpy as np

example="467..114..\n\
...*......\n\
..35..633.\n\
......#...\n\
617*......\n\
.....+.58.\n\
..592.....\n\
......755.\n\
...$.*....\n\
.664.598.."

def read_input():
    input = open('03/input.txt').read().strip()
    return input.split('\n')       

def recursive_parse(text, numbers, row, start=0):
    pattern = "{:d}"
    if (match := parse.search(pattern, text)):
        numbers.append({"row":row, "res":match, "offset":start})
        text = text[match.spans[0][1]:]
        recursive_parse(text, numbers, row, start=start+match.spans[0][1])
    else:
        return

def find_adjacent(result, pt2):
    match=result["res"]
    row=result["row"]
    adjacent = []
    offset = result["offset"]
    for i in range(match.spans[0][0]-1, match.spans[0][1]+1):
        for j in range(-1,+2):
            x = row + j
            y = i + offset
            try:
                adjacent.append(input[x][y])
                # check if *
                if input[x][y] == '*':
                    try:
                        pt2 += (gears[(x,y)] *  match[0])
                    except:
                        gears[(x,y)] = match[0]
            except:
                adjacent.append('.')
    return adjacent, pt2
    

def check_adjacent(adjacent):
    for char in adjacent:
        if char != '.' and not char.isdigit():
            return True

input = read_input()
# input = example.split('\n')
pprint.pprint(input)
numbers=[]
for i, line in enumerate(input):
    recursive_parse(line, numbers, i, start=0)

serials = []
gears={}
pt2=0
for match in numbers:
    adjacent, pt2 = find_adjacent(match, pt2)
    if check_adjacent(adjacent):
        serials.append(match["res"][0])

print(np.sum(np.abs(serials)))
print(gears)
print(pt2)