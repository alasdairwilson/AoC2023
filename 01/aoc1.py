import re
import numpy as np

wordtodigit = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four' : 'f4r',
    'five' : 'f5e',
    'six' : 's6x',
    'seven' : 's7n',
    'eight' : 'e8t',
    'nine' : 'n9e',
    '1': 1,
    '2': 2,
    '3': 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9
}

def read_input():
    with open('01/input.txt') as f:
        return [line for line in f]

def words_to_digits(line):
    for key in wordtodigit.keys():
        line = line.replace(key, str(wordtodigit[key]))
    return line
    
def find_first_last(line):
    numbers = re.findall(r'\d', line)
    print(numbers)
    return numbers[0], numbers[-1]

inp = read_input()
values = []
for line in inp:
    line = words_to_digits(line)
    first, last = find_first_last(line)
    values.append(str(first) + str(last))

values = [int(x) for x in values]
print(values[-10:])
print(np.sum(values))