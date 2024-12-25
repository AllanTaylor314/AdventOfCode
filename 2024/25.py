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
def size(pattern):
    return tuple(l.count("#") for l in zip(*pattern))
with open(INPUT_PATH) as file:
    lines = file.read().split("\n\n")
keys = [size(line.splitlines()) for line in lines if line[0]=="."]
locks = [size(line.splitlines()) for line in lines if line[0]=="#"]
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = 0
for key in keys:
    for lock in locks:
        p1 += all((a+b)<=7 for a,b in zip(key,lock))

print("Part 1:",p1)
timer_part1_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
