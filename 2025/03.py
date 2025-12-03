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
# initial part 1 solution
def max_jolt(s: str):
    first = max(s)
    idx = s.index(first)
    if idx + 1 == len(s):
        second = first
        first = max(s[:idx])
    else:
        second = max(s[idx+1:])
    return int(first+second)

# adjusted for part 2 to solve both parts
def max_jolt(s, n=2):
    js = []
    for i in range(n-1,-1,-1):
        js.append(max(s[:-i or None]))
        s = s[s.index(js[-1])+1:]
    return int(''.join(js))

p1 = 0
for line in lines:
    p1 += max_jolt(line)

print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
p2 = 0
for line in lines:
    p2 += max_jolt(line, 12)

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
