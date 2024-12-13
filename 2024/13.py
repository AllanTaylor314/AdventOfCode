import os
from pathlib import Path
from time import perf_counter
import re
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
DIRECTIONS = [(0,1),(1,0),(0,-1),(-1,0)]
def add(*ps): return tuple(map(sum,zip(*ps)))
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
nums = [list(map(int,re.findall(r"\d+",line))) for line in lines]
As = nums[::4]
Bs = nums[1::4]
Ps = nums[2::4]
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = 0
for a,b,p in zip(As,Bs,Ps):
    ax,ay = a
    bx,by = b
    x,y = p
    mat_div = ax*by-bx*ay
    na = by*x-bx*y
    nb = -ay*x+ax*y
    if na%mat_div == 0 and nb%mat_div==0:
        na//=mat_div
        nb//=mat_div
        if na >= 0 and nb >= 0:
            p1 += 3*na + nb
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
p2 = 0
for a,b,p in zip(As,Bs,Ps):
    ax,ay = a
    bx,by = b
    p = (p[0]+10000000000000,p[1]+10000000000000)
    x,y = p
    mat_div = ax*by-bx*ay
    na = by*x-bx*y
    nb = -ay*x+ax*y
    if na%mat_div == 0 and nb%mat_div==0:
        na//=mat_div
        nb//=mat_div
        if na >= 0 and nb >= 0:
            p2 += 3*na + nb

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
