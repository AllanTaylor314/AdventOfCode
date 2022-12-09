with open("09.txt") as file:
    lines = file.read().splitlines()
deltas = [(int(b),1j**"RDLU".index(a)) for a,b in map(str.split,lines)] # num, dir
directions = [1,1+1j,1j,-1+1j,-1,-1-1j,-1j,1-1j]
def sign(n):
    if n==0:return 0
    if n<0:return -1
    return 1
def difference_to_direction(diff: complex):
    return sign(diff.real)+sign(diff.imag)*1j
p1 = 0
HEAD = 0+0j
TAIL = 0+0j
tails = {TAIL}
for num,dire in deltas:
    for _ in range(num):
        HEAD+=dire
        while abs(TAIL-HEAD)>=2: # Up to sqrt2
            rough = HEAD-TAIL
            TAIL+=difference_to_direction(rough)
            tails.add(TAIL)
    

print("Part 1:",len(tails))
p2 = 0
tails2 = {0}
rope = [0+0j]*10
for num,dire in deltas:
    for _ in range(num):
        rope[0]+=dire
        for ti in range(1,len(rope)):
            hi = ti-1 # head index, tail index
            while abs(rope[ti]-rope[hi])>=2: # Up to sqrt2
                rope[ti]+=difference_to_direction(rope[hi]-rope[ti])
        tails2.add(rope[ti]) # last only
print("Part 2:",len(tails2))
