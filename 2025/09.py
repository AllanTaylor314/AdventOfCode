from math import prod
import os
from pathlib import Path
from time import perf_counter
from itertools import combinations
from shapely import Polygon

timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
DIRECTIONS = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)][::2]
def add(*ps): return tuple(map(sum,zip(*ps)))
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()

coords = [tuple(map(int,line.split(','))) for line in lines]

def area(p1,p2):
    return prod(abs(a-b)+1 for a,b in zip(p1,p2,strict=True))

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = area(*max(combinations(coords, 2), key=lambda ps: area(*ps)))
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
bounds = Polygon(coords).buffer(0.3)
options = []

for a,b in combinations(coords, 2):
    x1,y1 = a
    x2,y2 = b
    box = Polygon.from_bounds(min(x1,x2)-.1,min(y1,y2)-.1,max(x1,x2)+.1,max(y1,y2)+.1)
    if box.within(bounds):
        options.append((a,b))

p2 = area(*max(options, key=lambda ps: area(*ps)))
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
