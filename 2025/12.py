from math import prod
import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
DIRECTIONS = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)][::2]
def add(*ps): return tuple(map(sum,zip(*ps)))
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    text = file.read()

def parse_shape(shape_def):
    shape_id, *shape_lines = shape_def.splitlines()
    return int(shape_id[:-1]), tuple(shape_lines)

def parse_region(region_def):
    size_str, count_str = region_def.split(':')
    size = tuple(map(int, size_str.split('x')))
    counts = tuple(map(int,count_str.split()))
    return size, counts

*shape_defs, region_defs = text.replace('\r','').split('\n\n')
shapes = {k:v for k,v in map(parse_shape, shape_defs)}
regions = list(map(parse_region, region_defs.splitlines()))

def num_hashes(shape):
    return sum(l.count('#') for l in shape)

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = 0
shape_counts = {k:num_hashes(v) for k,v in shapes.items()}
for region_size, num_shapes in regions:
    p1 += prod(region_size) >= sum(shape_counts[i] * n for i,n in enumerate(num_shapes))

print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
p2 = 0

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
