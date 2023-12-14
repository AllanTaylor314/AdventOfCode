import os
from pathlib import Path
from time import perf_counter
from collections import deque
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
N,E,W,S = -1j, 1, -1, 1j
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
N_COLS = len(lines[0])
N_ROWS = len(lines)
rocks = {j+i*1j for i,line in enumerate(lines) for j,c in enumerate(line) if c=='O'}
blocks = (frozenset(j+i*1j for i,line in enumerate(lines) for j,c in enumerate(line) if c=='#') | 
          frozenset(complex(-1,i) for i in range(N_ROWS)) |
          frozenset(complex(N_COLS,i) for i in range(N_ROWS)) |
          frozenset(complex(i,-1) for i in range(N_COLS)) |
          frozenset(complex(i,N_ROWS) for i in range(N_COLS)))

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
n_rocks = len(rocks)
def print_grid():
    for j in range(N_ROWS):
        for i in range(N_COLS):
            n = complex(i,j)
            print(end='.#O'[(n in blocks) or 2*(n in rocks)])
        print()
def roll(d):
    global rocks, blocks
    blocked_rocks = set(blocks)
    q = deque(rocks)
    while q:
        rock = q.popleft()
        new_rock = rock+d
        if new_rock in blocked_rocks:
            blocked_rocks.add(rock) # rock stays put
        elif new_rock in rocks:
            q.append(rock) # existing rock -> requeue
        else:
            rocks.remove(rock)
            rocks.add(new_rock)
            q.append(new_rock)

roll(N)
p1 = sum(N_ROWS-int(r.imag) for r in rocks)
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
def cycle():
    roll(N)
    roll(W)
    roll(S)
    roll(E)
history = {}
for i in range(1000000000):
    cycle()
    prev_set = frozenset(rocks)
    if prev_set in history:
        loop_start = history[prev_set]
        loop_size = i - loop_start
        break
    history[prev_set] = i
target = loop_start + (999999999-loop_start)%loop_size
p2 = sum(N_ROWS-int(r.imag) for r in next(k for k,v in history.items() if v==target))
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
