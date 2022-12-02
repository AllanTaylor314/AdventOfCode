# P1: A,B,C; X,Y,Z; R,P,S
# P2: X,Y,Z; L,T,W
R,P,S,L,T,W = 1,2,3,0,3,6
p1_combos = {
    "A X":R+T,
    "A Y":P+W,
    "A Z":S+L,
    "B X":R+L,
    "B Y":P+T,
    "B Z":S+W,
    "C X":R+W,
    "C Y":P+L,
    "C Z":S+T,
}
p2_combos = {
    "A X":L+S, 
    "A Y":T+R,
    "A Z":W+P,
    "B X":L+R,
    "B Y":T+P,
    "B Z":W+S,
    "C X":L+P,
    "C Y":T+S,
    "C Z":W+R,
}
with open("02.txt") as file:
    lines = file.read().splitlines()
print("Part 1:",sum(p1_combos[line] for line in lines))
print("Part 2:",sum(p2_combos[line] for line in lines))
