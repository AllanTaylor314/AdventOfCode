import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
def valid_index(i,j):
    return 0<=i<len(lines) and 0<=j<len(lines[i])
def get_c(i,j,d=""):
    if valid_index(i,j):
        return lines[i][j]
    return d
directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = 0
for i, line in enumerate(lines):
    for j,c in enumerate(line):
        if c == "X":
            for di, dj in directions:
                if "".join(get_c(i+n*di,j+n*dj) for n in range(4)) == "XMAS":
                    p1 += 1
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
p2 = 0
for i, line in enumerate(lines):
    for j,c in enumerate(line):
        if c == "A":
            for (di,dj),(di2,dj2) in zip(directions[::2],directions[2::2]+directions[:2:2]):
                if (get_c(i-di,j-dj)=="M" and get_c(i+di,j+dj)=="S" and 
                    get_c(i-di2,j-dj2)=="M" and get_c(i+di2,j+dj2)=="S"):
                    p2 += 1
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
