import os
from pathlib import Path
from time import perf_counter
from collections import deque
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
N,E,W,S = -1j,1,-1,1j
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
GRID = {complex(x,y):c for y,line in enumerate(lines) for x,c in enumerate(line)}
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
TURNS = {
    ('|',E):[N,S],
    ('|',W):[N,S],
    ('-',N):[E,W],
    ('-',S):[E,W],
    ('/',S):[W],
    ('/',N):[E],
    ('/',W):[S],
    ('/',E):[N],
    ('\\',S):[E],
    ('\\',N):[W],
    ('\\',W):[N],
    ('\\',E):[S],
}

def next_beams(beam):
    loc,dr = beam
    new_loc = loc+dr
    if new_loc in GRID:
        new_dirs = TURNS.get((GRID[new_loc],dr),[dr])
        return [(new_loc,new_dir) for new_dir in new_dirs]
    return []

def trial(start_beam):
    active = set()
    q = deque(next_beams(start_beam))
    handled = set(q)
    while q:
        beam = q.popleft()
        active.add(beam[0])
        new = next_beams(beam)
        q.extend(b for b in new if b not in handled)
        handled|=set(new)
    return len(active)

p1 = trial((-1,E))
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
starts = []
h = len(lines)
w = len(lines[0])
for x in range(w):
    starts.append((complex(x,-1),S))
    starts.append((complex(x,h),N))
for y in range(h):
    starts.append((complex(-1,y),E))
    starts.append((complex(w,y),W))

p2 = max(map(trial,starts))
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
