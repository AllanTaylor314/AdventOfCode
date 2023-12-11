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
# grid = {j+i*1j for i,line in enumerate(lines) for j,c in enumerate(line) if c=='#'}
empty_rows = [i for i,row in enumerate(lines) if '#' not in row]
empty_cols = [i for i,col in enumerate(zip(*lines)) if '#' not in col]
grid1 = set()
grid2 = set()
y1_offset = y2_offset = 0
for y0,line in enumerate(lines):
    if y0 in empty_rows:
        y1_offset += 1
        y2_offset += 999_999
    y1 = y0 + y1_offset
    y2 = y0 + y2_offset
    x1_offset = x2_offset = 0
    for x0,c in enumerate(line):
        if x0 in empty_cols:
            x1_offset += 1
            x2_offset += 999_999
        x1 = x0 + x1_offset
        x2 = x0 + x2_offset
        if c == '#':
            grid1.add(x1+y1*1j)
            grid2.add(x2+y2*1j)

def print_grid(grid):
    for y in range(int(max(n.imag for n in grid))+1):
        for x in range(int(max(n.real for n in grid))+1):
            print(end='.#'[complex(x,y) in grid])
        print()

def manhattan(n:complex):
    return abs(int(n.real))+int(abs(n.imag))

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = sum(manhattan(a-b) for a in grid1 for b in grid1)//2
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
p2 = sum(manhattan(a-b) for a in grid2 for b in grid2)//2
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
