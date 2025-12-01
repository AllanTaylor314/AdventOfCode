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
deltas = [int(line.replace('R','').replace('L','-')) for line in lines]

timer_parse_end=timer_part1_start=perf_counter()
############################# PART 1&2 #############################
p1 = 0
p2 = 0
val = 50
for d in deltas:
    for i in range(d):
        val = (val + 1) % 100
        p2 += val == 0
    for i in range(-d):
        val = (val - 1) % 100
        p2 += val == 0
    p1 += val == 0

print("Part 1:",p1)
print("Part 2:",p2)

timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Parts: {timer_part2_end-timer_part1_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
