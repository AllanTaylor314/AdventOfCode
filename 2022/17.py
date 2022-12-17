from itertools import cycle
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
LOOP_HEIGHT = 2778 # Difference between floors (Using CTRL+F on the output)
LOOP_LENGTH = 1745 # Number of rocks (Seeing which loops had those heights)
iterations,offset = divmod(1000000000000,LOOP_LENGTH)
print("Part 2:",i2height[offset]+LOOP_HEIGHT*iterations)
