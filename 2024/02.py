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
data = [list(map(int,line.split())) for line in lines]
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
def is_safe(l):
    return (all(a<b for a,b in zip(l,l[1:])) or all(a>b for a,b in zip(l,l[1:]))) and all(0<abs(a-b)<=3 for a,b in zip(l,l[1:]))
p1 = sum(map(is_safe,data))
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
def is_almost_safe(l):
    return any(is_safe(l[:i]+l[i+1:]) for i in range(len(l)))
p2 = sum(map(is_almost_safe,data))
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
