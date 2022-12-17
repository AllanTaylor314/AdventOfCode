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
for i,rock in zip(range(2022),rock_cycle):
    print(end=f"Dropping {i}...")
    rock = tuple(r+floor*1j for r in rock) # Offset 3 above current max
    while True:
        # Push
        gas = next(gas_cycle)
        new_rock = tuple(r+gas for r in rock)
        if all(0<=z.real<7 for z in new_rock) and not filled&set(new_rock):
            rock = new_rock
        #     print("Gas moved rock",rock,new_rock)
        # else:
        #     print("Didn't move",rock,new_rock)
        # Drop
        new_rock = tuple(r-1j for r in rock)
        if filled&set(new_rock):
            filled.update(rock)
            floor = max(floor, *(int(z.imag)+1 for z in rock))
            # print("Didn't fall",rock,new_rock)
            break
        else:
            # print("Fell one",rock,new_rock)
            rock = new_rock
    print(f"Done: {floor=}")

print("Part 1:",floor)
p2 = 0

print("Part 2:",p2)
