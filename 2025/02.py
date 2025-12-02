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
    pairs = [tuple(map(int,line.split('-'))) for line in file.read().strip().split(',')]

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
def is_invalid(n):
    s = str(n)
    if len(s)%2:
        return False
    return s[:len(s)//2] == s[len(s)//2:]

def sum_invalid_pairs(start, end):
    total = 0
    for i in range(start, end + 1):
        if is_invalid(i):
            total += i
    return total

p1 = 0
for a,b in pairs:
    p1 += sum_invalid_pairs(a,b)
    
# not 813
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
def is_invalid(n):
    s = str(n)
    for size in range(1,len(s)):
        if len({s[i:i+size] for i in range(0,len(s),size)}) == 1:
            return True
    return False
p2 = 0
for a,b in pairs:
    p2 += sum_invalid_pairs(a,b)
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
