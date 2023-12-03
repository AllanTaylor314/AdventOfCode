import os
from pathlib import Path
from time import perf_counter
from collections import defaultdict
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = 0
num_str = ''
for r,line in enumerate(lines):
    line+='.'
    for c,char in enumerate(line):
        if char.isdigit():
            num_str += char
        elif num_str:
            if any(lines[r1][c1] not in '.0123456789' for r1 in (range(max(0,r-1),min(len(lines),r+2)))
                   for c1 in range(max(0,c-1-len(num_str)),min(len(line)-1,c+1))):
                p1 += int(num_str)
            num_str = ''
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
dct = defaultdict(list)
num_str = ''
for r,line in enumerate(lines):
    line+='.'
    for c,char in enumerate(line):
        if char.isdigit():
            num_str += char
        elif num_str:
            for r1 in (range(max(0,r-1),min(len(lines),r+2))):
                for c1 in range(max(0,c-1-len(num_str)),min(len(line)-1,c+1)):
                    if lines[r1][c1] == '*':
                        dct[r1,c1].append(int(num_str))
            num_str = ''

p2=sum(ab[0]*ab[1] for ab in dct.values() if len(ab)==2)
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
