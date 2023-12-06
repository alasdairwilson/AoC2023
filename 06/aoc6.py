import numpy as np
import parse

example = "Time:      7  15   30\n\
Distance:  9  40  200"

def read_input():
    input = open('06/input.txt').read().strip()
    return input.split('\n')

def parse_input(input):
    times = [int(x) for x in input[0].split()[1:]]
    distances = [int(x) for x in input[1].split()[1:]]
    return times, distances

def make_options(time):
    distance = np.zeros(time)
    for i in range(time):
        time_pressed = i
        time_release = time-i
        speed = time_pressed * 1
        distance[i] = speed * time_release
    return distance

def compare_options(options, best):
    winners = []
    for i, option in enumerate(options):
        if option > best:
            winners.append(i)

    return winners

input = read_input()
# input = example.split('\n')

times, distances = parse_input(input)

winners_overall = []
for i in range(len(times)):
    options = make_options(times[i])
    winners = compare_options(options, distances[i])
    winners_overall.append(winners)

print(np.prod([len(win) for win in winners_overall]))

time = ('').join([str(x) for x in times])
distance = ('').join([str(x) for x in distances])
print(time, distance)
options = make_options(int(time))
winners = compare_options(options, int(distance))
print(len(winners))
