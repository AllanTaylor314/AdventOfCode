from functools import cache
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
    lines = file.read().splitlines()

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = 0
beams = {start := lines[0].index('S')}
for line in lines:
    new_beams = set(beams)
    for i in beams:
        if line[i] == '^':
            new_beams.discard(i)
            new_beams.add(i-1)
            new_beams.add(i+1)
            p1 += 1
    beams = new_beams

print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
@cache
def num_worlds(beam_column, row):
    if row >= len(lines):
        return 1
    line = lines[row]
    if line[beam_column] == '^':
        return num_worlds(beam_column + 1, row + 1) + num_worlds(beam_column - 1, row + 1)
    return num_worlds(beam_column, row + 1)

p2 = num_worlds(start, 0)
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
