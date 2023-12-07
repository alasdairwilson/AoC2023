import numpy as np
import parse

example = "32T3K 765\n\
T55J5 684\n\
KK677 28\n\
KTJJT 220\n\
QQQJA 483"


card_order = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6,
              '9':7, 'T':8, 'J':-1, 'Q':10, 'K':11, 'A':12}

def read_input():
    input = open('07/input.txt').read().strip()
    return input.split('\n')

def of_a_kind(cards):
    exclude = ['J']
    counts = []
    jokers=0
    jokers=cards.count('J')
    for i in range(len(cards)):
        if cards[i] not in exclude:
            counts.append(cards.count(cards[i]))
            exclude.append(cards[i])
    if jokers == 5:
        return 0
    elif np.max(counts) + jokers == 5:
        return 0
    elif np.max(counts) + jokers == 4:
        return 1
    elif np.max(counts) == 3 and np.min(counts) == 2:
        return 2
    elif counts.count(2) == 2 and jokers == 1:
        return 2
    elif np.max(counts) + jokers == 3:
        return 3
    elif counts.count(2) == 2:
        return 4
    elif counts.count(2) == 1:
        return 5
    elif jokers == 1:
        return 5
    else:
        return 6

class Hand():
    def __init__(self, cards, bid) -> None:
        self.cards = cards
        self.bid = bid
        self.score = np.nan
        self.tiebreak = [np.nan, np.nan, np.nan, np.nan, np.nan]
        self.winnings=0
    
    def score_hand(self):
        self.score = of_a_kind(self.cards)
        for i in range(len(self.cards)):
            self.tiebreak[i] = card_order[self.cards[i]]

    def __str__(self):
        return f"{self.cards} {self.bid}"
    
    def __repr__(self):
        return f"{self.cards} {self.bid}"

input = read_input()
# input = example.split('\n')

hands = []
for line in input:
    pattern = "{cards} {bid:d}"
    match = parse.parse(pattern, line)
    hand = Hand(match['cards'], match['bid'])
    hand.score_hand()
    hands.append(hand)

hands = sorted(hands, key=lambda x: x.score)
scores = set([x.score for x in hands])
print(scores)
hands2=[]
for score in scores:
    hands_score = [x for x in hands if x.score == score]
    if len(hands_score) > 0:
        hands_score = sorted(hands_score, key=lambda x: x.tiebreak, reverse=True)
    [hands2.append(hand) for hand in hands_score]

for i, card in enumerate(reversed(hands2)):
    card.winnings = (i+1)*card.bid

print(hands2[100:110])
print(np.sum([card.winnings for card in (hands2)]))
