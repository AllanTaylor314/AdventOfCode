import os
from pathlib import Path
from time import perf_counter
from collections import Counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
JOKERS = False
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()

class CamelHand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.counts = Counter(cards)
    def type(self):
        sizes = sorted(self.counts.values())
        js = self.counts['J']
        if JOKERS and js not in (0,5):
            sizes.remove(js)
            sizes[-1]+=js
        if sizes == [5]:
            return 6 # 5 kind
        if sizes == [1,4]:
            return 5 # 4 kind
        if sizes == [2,3]:
            return 4 # Full house
        if sizes == [1,1,3]:
            return 3 # 3 kind
        if sizes == [1,2,2]:
            return 2 # 2 pair
        if sizes == [1,1,1,2]:
            return 1 # pair
        return 0 # High
    def card_order(self):
        cards = []
        for c in self.cards:
            if c.isdigit():
                cards.append(int(c))
            elif JOKERS and c=='J':
                cards.append(0)
            else:
                cards.append(10+"TJQKA".index(c))
        return cards
    def key(self):
        return self.type(), self.card_order()
hands = [CamelHand(*line.split()) for line in lines]

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
hands.sort(key=CamelHand.key)

p1 = sum(hand.bid*i for i,hand in enumerate(hands,start=1))
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
JOKERS = True
hands.sort(key=CamelHand.key)
p2 = sum(hand.bid*i for i,hand in enumerate(hands,start=1))
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
