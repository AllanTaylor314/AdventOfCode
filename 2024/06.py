import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
grid = {(i,j):c for i,line in enumerate(lines) for j,c in enumerate(line)}
start_location ,= (k for k,v in grid.items() if v=="^")
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
def step(loc,d,extra=None):
    di,dj = d
    nloc = tuple(map(sum,zip(loc,d)))
    if grid.get(nloc) == "#" or nloc==extra:
        d = dj, -di
        return step(loc,d,extra)
    return nloc, d
def solve(extra=None):
    visited_pairs = set()
    visited = set()
    location = start_location
    direction = (-1,0)
    while location in grid:
        if (location,direction) in visited_pairs:
            break
        visited_pairs.add((location,direction))
        visited.add(location)
        location, direction = step(location, direction, extra)
    else:
        return visited
    return True
og_path = solve()
p1 = len(og_path)
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
og_path.discard(start_location)
p2 = sum(solve(l) is True for l in og_path)
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
