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
data = {(i,j):c for i, line in enumerate(lines) for j,c in enumerate(line)}
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
DIRECTIONS = [(0,1),(1,0),(0,-1),(-1,0)]

def add(*ps):
    return tuple(map(sum,zip(*ps)))

def num_sides(border_pairs:set):
    sides = []
    while border_pairs:
        loc, out = border_pairs.pop()
        side = [(loc,out)]
        (di, dj) = out
        right = (dj, -di)
        left = (-dj, di)
        rloc = add(loc, right)
        while (rloc,out) in border_pairs:
            border_pairs.remove((rloc,out))
            side.append((rloc,out))
            rloc = add(rloc, right)
        lloc = add(loc, left)
        while (lloc,out) in border_pairs:
            border_pairs.remove((lloc,out))
            side.append((lloc,out))
            lloc = add(lloc, left)
        sides.append(side)
    return len(sides)

p1 = 0
p2 = 0
covered_regions = set()
loc_to_region = {}
all_regions = []
for loc,c in data.items():
    if loc in covered_regions:
        continue
    new_region = {loc}
    all_regions.append(new_region)
    loc_to_region[loc] = new_region
    stack = {loc}
    border = set()
    while stack:
        nloc = stack.pop()
        for d in DIRECTIONS:
            nei = add(nloc,d)
            if data.get(nei) == c:
                if nei not in covered_regions:
                    stack.add(nei)
                    loc_to_region[nei] = new_region
                    new_region.add(nei)
                    covered_regions.add(nei)
            else:
                border.add((nloc,d))
    p1 += len(border) * len(new_region)
    p2 += num_sides(border) * len(new_region)

print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
