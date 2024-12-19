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
towel_patterns = set(lines[0].split(", "))
designs = lines[2:]
max_pattern_size = max(map(len,towel_patterns))

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
@cache
def num_patterns(design,index=0):
    if index == len(design):
        return 1
    if index > len(design):
        return 0
    total = 0
    for pattern_size in range(1,max_pattern_size+1):
        pattern = design[index:index+pattern_size]
        if len(pattern) != pattern_size:
            break
        if pattern in towel_patterns:
            total += num_patterns(design,index+pattern_size)
    return total
p1 = sum(n!=0 for n in map(num_patterns,designs))

print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
p2 = sum(map(num_patterns,designs))

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
