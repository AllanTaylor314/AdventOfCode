# P1: A,B,C; X,Y,Z; R,P,S
# P2: X,Y,Z; L,T,W
p1_combos = {
    "A X":1+3,
    "A Y":2+6,
    "A Z":3+0,
    "B X":1+0,
    "B Y":2+3,
    "B Z":3+6,
    "C X":1+6,
    "C Y":2+0,
    "C Z":3+3,
}
p2_combos = {
    "A X":0+3, 
    "A Y":3+1,
    "A Z":6+2,
    "B X":0+1,
    "B Y":3+2,
    "B Z":6+3,
    "C X":0+2,
    "C Y":3+3,
    "C Z":6+1,
}
with open("02.txt") as file:
    lines = file.read().splitlines()
print(sum(p1_combos[line] for line in lines))
print(sum(p2_combos[line] for line in lines))

