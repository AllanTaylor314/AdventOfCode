def imag_range(a,b): # inclusive
    delta = (b-a)/abs(a-b)
    for i in range(int(abs(a-b))+1):
        yield a+i*delta
with open("14.txt") as file:
    lines = file.read().splitlines()
pair_lists = [[tuple(map(int,pair.split(","))) for pair in line.split(" -> ")] for line in lines]
imag_lists = [[x+y*1j for x,y in l] for l in pair_lists]
WALLS = {n for il in imag_lists for a,b in zip(il,il[1:]) for n in imag_range(a,b)}
BOTTOM_Y = int(max(z.imag for z in WALLS))
SANDS = set()
sand = 500+0j
while sand.imag < BOTTOM_Y:
    sand = 500+0j
    while True:
        full = WALLS | SANDS
        if sand+1j not in full:
            sand+=1j
        elif sand-1+1j not in full:
            sand+=-1+1j
        elif sand+1+1j not in full:
            sand+=1+1j
        else: # at rest
            SANDS.add(sand)
            break
        if sand.imag >= BOTTOM_Y:
            break
    if sand.imag >= BOTTOM_Y:
        break

p1 = len(SANDS)
print("Part 1:",p1)
p2 = 0

print("Part 2:",p2)
