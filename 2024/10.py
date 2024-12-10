import os
from pathlib import Path
from time import perf_counter
from functools import cache
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
grid = {(i,j):int(c) for i,line in enumerate(lines) for j,c in enumerate(line) if c != '.'}
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
candidate_heads = [ij for ij,h in grid.items() if h==0]

DIRECTIONS = [(0,1),(1,0),(0,-1),(-1,0)]

def add(*ps):
    return tuple(map(sum,zip(*ps)))

@cache
def trails_from_loc(ij):
    if grid[ij] == 9:
        return {ij}
    ends = set()
    for d in DIRECTIONS:
        nij = add(ij,d)
        if grid.get(nij) == grid[ij] + 1:
            ends |= trails_from_loc(nij)
    return ends
def num_trails_from_loc(ij):
    return len(trails_from_loc(ij))
p1 = sum(map(num_trails_from_loc,candidate_heads))
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
@cache
def num_distinct_trails_from_loc(ij):
    if grid[ij] == 9:
        return 1
    count = 0
    for d in DIRECTIONS:
        nij = add(ij,d)
        if grid.get(nij) == grid[ij] + 1:
            count += num_distinct_trails_from_loc(nij)
    return count
p2 = sum(map(num_distinct_trails_from_loc,candidate_heads))

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
