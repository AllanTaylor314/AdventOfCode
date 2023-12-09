import os
from pathlib import Path
from time import perf_counter
import numpy as np
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
data = [list(map(int,line.split())) for line in lines]
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
def extrapolate(row):
    new_row = row[1:]-row[:-1]
    if any(new_row):
        return row[-1]+extrapolate(new_row)
    return row[-1]
p1 = sum(extrapolate(np.array(row)) for row in data)
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
p2 = 0
def backtrapolate(row):
    new_row = row[1:]-row[:-1]
    if any(new_row):
        return row[0]-backtrapolate(new_row)
    return row[0]
p2 = sum(backtrapolate(np.array(row)) for row in data)
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
