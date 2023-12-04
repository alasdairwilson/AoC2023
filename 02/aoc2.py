import parse
import re
import numpy as np

example="Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n\
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n \
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n \
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n \
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"

class aocRound():
    def __init__(self, **kwargs):
        self.red=kwargs['red']
        self.green=kwargs['green']
        self.blue=kwargs['blue']
    
    def check(self, red, green, blue):
        if (self.red > red) or (self.green > green) or (self.blue > blue):
            return False
        else:
            return True
    
    def __str__(self):
        return "red: {}, green: {}, blue: {}".format(self.red, self.green, self.blue)
    def __repr__(self):
        return "red: {}, green: {}, blue: {}".format(self.red, self.green, self.blue)


class aocGame():
    def __init__(self, line):
        sections = re.split(':|;', line)
        pattern_game  = "Game {game:d}"
        self.game = parse.search(pattern_game, sections[0])['game']
        self.rounds = []
        for i in range(1, len(sections)):
            print(sections[i])
            pattern_red = "{red:d} red"
            pattern_blue = "{blue:d} blue"
            pattern_green = "{green:d} green"
            try:
                red = int(parse.search(pattern_red, sections[i])['red'])
            except:
                red = 0
            try:
                blue = int(parse.search(pattern_blue, sections[i])['blue'])
            except:
                blue = 0
            try:
                green = int(parse.search(pattern_green, sections[i])['green'])
            except:
                green = 0
            round = aocRound(red=red, blue=blue, green=green)
            self.rounds.append(round)
    def check(self, red, green, blue):
        for round in self.rounds:
            print(round.red)
            if not round.check(red, green, blue):
                return False
        return self.game
    
    def power(self):
        red = 0
        green = 0
        blue = 0
        for round in self.rounds:
            if round.red > red:
                red = round.red
            if round.green > green:
                green = round.green
            if round.blue > blue:
                blue = round.blue
        return red * green * blue
            

def read_input():
    with open('02/input.txt') as f:
        return [line for line in f]
    

input = read_input()
games = [aocGame(line) for line in input]
sum = 0
for game in games:
    sum += game.check(12, 13, 14)

## part 1
print(sum)

## part 2
print(np.sum([game.power() for game in games]))