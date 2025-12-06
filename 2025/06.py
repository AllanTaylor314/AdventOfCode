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
    lines = file.read().splitlines()

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = 0
cols = list(zip(*(line.split() for line in lines)))
for *col, op in cols:
    nums = list(map(int,col))
    if op == '+':
        p1 += sum(nums)
    elif op == '*':
        p1 += prod(nums)
    else:
        raise op

print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
p2 = 0
trans = [l.strip() for l in map(''.join,zip(*lines[:-1]))]
ops = lines[-1].split()
groups = [[]]
for n in trans:
    if n:
        groups[-1].append(int(n))
    else:
        groups.append([])
for nums, op in zip(groups, ops, strict=True):
    if op == '+':
        p2 += sum(nums)
    elif op == '*':
        p2 += prod(nums)
    else:
        raise op

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
