from itertools import cycle
from collections import Counter, defaultdict
DELTA = {
    ">":1,
    "<":-1,
}
ROCKS = [
    (2+3j,3+3j,4+3j,5+3j),          # -
    (3+3j,2+4j,3+4j,4+4j,3+5j),     # +
    (2+3j,3+3j,4+3j,4+4j,4+5j),     # _|
    (2+3j,2+4j,2+5j,2+6j),          # |
    (2+3j,3+3j,3+4j,2+4j)           # []
]
with open("17.txt") as file:
    line = file.read().strip()
gas_cycle = cycle(map(DELTA.get,line))
rock_cycle = cycle(ROCKS)
floor = 0
filled = {i-1j for i in range(7)}
i2height = {}
for i,rock in zip(range(1,10_001),rock_cycle):
    rock = tuple(r+floor*1j for r in rock) # Offset 3 above current max
    while True:
        # Push
        gas = next(gas_cycle)
        new_rock = tuple(r+gas for r in rock)
        if all(0<=z.real<7 for z in new_rock) and not filled&set(new_rock):
            rock = new_rock
        new_rock = tuple(r-1j for r in rock)
        if filled&set(new_rock):
            filled.update(rock)
            floor = max(floor, *(int(z.imag)+1 for z in rock))
            break
        else:
            rock = new_rock
    i2height[i]=floor

## For the CTRL+F trickery
# with open("17-map.txt","w",newline="\n") as f:
#     for y in range(floor,-1,-1):
#         for x in range(7):
#             f.write(".#"[x+y*1j in filled])
#         f.write("\n")

print("Part 1:",i2height[2022])

# 5 (n-rocks) is prime, 10091 (gas cycle length) is also prime
NUM_ROWS = 10 # Number of rows to try to match: Larger is more accurate, Smaller is faster
zs = [x+y*1j for x in range(7) for y in range(floor-NUM_ROWS-1,floor)]
bools = [z in filled for z in zs]
offset = 0
while True:
    offset+=1
    if all(((z-offset*1j) in filled)==b for z,b in zip(zs,bools)):
        LOOP_HEIGHT = offset
        break
# Surely there is a better way to do this, but it seems to work ok
height2i = defaultdict(list)
loop_sizes = Counter()
prevheight = 0
for i,height in i2height.items():
    height%=LOOP_HEIGHT
    if height!=prevheight:
        if height2i[height]:
            loop_sizes[i-height2i[height][-1]]+=1
        height2i[height].append(i)
    prevheight = height
LOOP_LENGTH = max(loop_sizes,key=loop_sizes.get)

iterations,offset = divmod(1000000000000,LOOP_LENGTH)
print("Part 2:",i2height[offset]+LOOP_HEIGHT*iterations)
