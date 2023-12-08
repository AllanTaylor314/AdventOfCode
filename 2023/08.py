import os
from pathlib import Path
from time import perf_counter
from itertools import cycle
from functools import reduce
from math import lcm
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    header,_,*lines = file.read().splitlines()
directions = {}
ghost_starts = []
for line in lines:
    a,b = line.split(' = ')
    c,d = b[1:-1].split(', ')
    directions[a]=c,d
    if a[-1]=='A':
        ghost_starts.append(a)
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = 0
loc = 'AAA'
for lr in cycle(header):
    if lr == 'L':
        loc = directions[loc][0]
    elif lr == 'R':
        loc = directions[loc][1]
    else:
        raise ValueError()
    p1+=1
    if loc == 'ZZZ':
        break
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
print(len(ghost_starts), "ghosts")
p2 = 0
for i,loc in enumerate(ghost_starts):
    count = 0
    for lr in cycle(header):
        if lr == 'L':
            loc = directions[loc][0]
        elif lr == 'R':
            loc = directions[loc][1]
        else:
            raise ValueError()
        count+=1
        if loc.endswith('Z'):
            ghost_starts[i] = count
            print(f"Ghost {i}: {count}")
            break
p2 = reduce(lcm, ghost_starts, 1)
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
