from itertools import cycle,product
from collections import Counter
from functools import cache

## INPUT ##
p1start = 7
p2start = 4
###########

class Player:
    die = cycle(range(1,101))
    die_count = 0
    def __init__(self,start):
        self.position = start
        self.score = 0
    def turn(self):
        for _ in range(3):
            self.position+=self.roll()
        self.position = self.position%10 or 10
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
THREE_ROLL_OUTCOMES = Counter(map(sum,product((1,2,3),repeat=3)))
@cache
def winners(p1,p2,s1=0,s2=0):
    if s2>=FINAL_SCORE: return (0,1)
    w1=w2=0
    for roll,weight in THREE_ROLL_OUTCOMES.items():
        np1 = (p1+roll)%10 or 10
        tw2,tw1 = winners(p2,np1,s2,s1+np1)
        w1+=weight*tw1
        w2+=weight*tw2
    return w1,w2
wins = winners(p1start,p2start)
print('Part 2:',max(wins))
