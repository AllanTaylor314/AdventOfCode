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
lrs = list(map('LR'.index,header))
directions = {line[:3]:(line[7:10],line[12:15]) for line in lines}
ghost_starts = [loc for loc in directions if loc.endswith('A')]
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = 0
loc = 'AAA'
for lr in cycle(lrs):
    loc = directions[loc][lr]
    p1+=1
    if loc == 'ZZZ':
        break
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
ghost_counts = []
for i,loc in enumerate(ghost_starts):
    count = 0
    for lr in cycle(lrs):
        loc = directions[loc][lr]
        count+=1
        if loc.endswith('Z'):
            ghost_counts.append(count)
            break
p2 = reduce(lcm, ghost_counts)
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
