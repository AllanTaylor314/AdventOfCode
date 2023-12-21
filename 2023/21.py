import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
N,E,W,S = NEWS = -1j,1,-1,1j
BIG_NUM = 26501365
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
SIZE = len(lines)
grid = {complex(x,y):c for y,line in enumerate(lines) for x,c in enumerate(line)}
opens = {k for k,v in grid.items() if v=='.'}
start,=(k for k,v in grid.items() if v=='S')
def print_pos(pos):
    for y in range(SIZE):
        for x in range(SIZE):
            print(end="O" if complex(x,y) in pos else "." if complex(x,y) in opens else '#')
        print()

opens.add(start)
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
pos = {start}
for _ in range(64):
    pos = {p+d for p in pos for d in NEWS if p+d in opens}
p1 = len(pos)
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
# Every second cell that is reachable in 26501365 steps
# input has a large open diamond
# 26501365%131 == 65
reachable = {start}
for _ in range(SIZE): # slow but works
    reachable = {p+d for p in reachable for d in NEWS+(0,) if p+d in opens}
inner_even_pos = pos
pos = {start}
for _ in range(65):
    pos = {p+d for p in pos for d in NEWS if p+d in opens}
inner_odd_pos = pos
two_steps = {a+b for a in NEWS for b in NEWS}
all_odd_pos = {complex(x,y) for x in range(SIZE) for y in range(not x%2,SIZE,2)} & reachable # odd steps
all_even_pos = {complex(x,y) for x in range(SIZE) for y in range(x%2,SIZE,2)} & reachable # even steps
square_length = (2*BIG_NUM+1)//SIZE
outer_odd_pos = all_odd_pos - inner_odd_pos
outer_even_pos = all_even_pos - inner_even_pos
outer_pve_pos = {c for c in outer_odd_pos if (c.real-65)*(c.imag-65)>0} | {c for c in outer_even_pos if (c.real-65)*(c.imag-65)<0}
outer_nve_pos = {c for c in outer_odd_pos if (c.real-65)*(c.imag-65)<0} | {c for c in outer_even_pos if (c.real-65)*(c.imag-65)>0}

AO = len(inner_odd_pos)
AE = len(inner_even_pos)
BP = len(outer_pve_pos)
BN = len(outer_nve_pos)
even_half, odd_half = sorted([square_length//2, -((-square_length)//2)], key=lambda x: x%2)
p2 = odd_half**2 * AO + even_half * odd_half * (BN+BP) + even_half**2 * AE

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
