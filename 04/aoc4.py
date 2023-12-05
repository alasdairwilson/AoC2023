import parse
import numpy as np
import re

example="Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n\
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n\
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n\
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n\
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n\
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"

def read_input():
    input = open('04/input.txt').read().strip()
    return input.split('\n')   

class scratchCard():
    def parseCard(self):
        pattern = "Card{}{card:d}: {numbers1} | {numbers2}"
        match = parse.parse(pattern, self.line)
        try:
            self.card_no = match['card']
            self.winners = [int(x) for x in match['numbers1'].split()]
            self.numbers = [int(x) for x in match['numbers2'].split()]
            self.numbers.sort()
            self.winners.sort()
        except:
            print('error:', self.line)
    
    def check(self):
        self.winnings = 0
        self.bonus = 0
        self.winning_numbers = []
        for number in self.numbers:
            if number in self.winners:
                self.bonus += 1
                if self.winnings==0:
                    self.winnings = 1
                else:
                    self.winnings *= 2
                self.winning_numbers.append(number)
        if self.bonus > 0:
            for i in range(self.bonus):
                cards[self.card_no+i]["card"].count += self.count

    def __init__(self, line) -> None:
        self.line=line
        self.count=1
        self.numbers = []
        self.winners=[]


input = read_input()
# input = example.split('\n')
cards = {}
for i, line in enumerate(input):
    card = scratchCard(line)
    cards[i] = {"card":card}

for i in np.arange(len(cards)):
    cards[i]["card"].parseCard()
    cards[i]["card"].check()

print(np.sum([cards[i]["card"].winnings for i in range(len(cards))]))
print(np.sum([cards[i]["card"].count for i in range(len(cards))]))