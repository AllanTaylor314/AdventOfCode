from itertools import cycle,product
from collections import Counter
from functools import cache

ROLLS = 3
SIDES = 3
TRACK_SIZE = 10

####### INPUT #######
p1start,p2start = 7,4
#####################

class Player:
    die = cycle(range(1,101))
    die_count = 0
    def __init__(self,start):
        self.position = start
        self.score = 0
    def turn(self):
        for _ in range(ROLLS):
            self.position+=self.roll()
        self.position = self.position%TRACK_SIZE or TRACK_SIZE
        self.score+=self.position
        return self.score<1000
    @classmethod
    def roll(cls):
        cls.die_count+=1
        return next(cls.die)

player1 = Player(p1start)
player2 = Player(p2start)
while player1.turn() and player2.turn(): pass
print('Part 1:',min(player1.score,player2.score)*Player.die_count)

FINAL_SCORE = 21
ROLL_OUTCOMES = Counter(map(sum,product(range(1,SIDES+1),repeat=ROLLS)))
@cache
def winners(p1,p2,s1=0,s2=0):
    if s2>=FINAL_SCORE: return (0,1)
    w1=w2=0
    for roll,weight in ROLL_OUTCOMES.items():
        np1 = (p1+roll)%TRACK_SIZE or TRACK_SIZE
        tw2,tw1 = winners(p2,np1,s2,s1+np1)
        w1+=weight*tw1
        w2+=weight*tw2
    return w1,w2
wins = winners(p1start,p2start)
print('Part 2:',max(wins))
