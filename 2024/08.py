import os
from pathlib import Path
from time import perf_counter
from collections import defaultdict
from itertools import combinations
from math import gcd
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
all_locs = {complex(i,j):c for i,line in enumerate(lines) for j,c in enumerate(line)}
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
freq_locs = defaultdict(list)
for loc, c in all_locs.items():
    if c != ".":
        freq_locs[c].append(loc)

in_range = set(all_locs)
antinodes = set()
for freq, locs in freq_locs.items():
    for a, b in combinations(locs, 2):
        delta = a-b
        antinodes.add(a+delta)
        antinodes.add(b-delta)
p1 = len(antinodes&in_range)

print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
actual_antinodes = set()
for freq, locs in freq_locs.items():
    for a, b in combinations(locs, 2):
        delta = a-b
        delta/=gcd(int(delta.real),int(delta.imag))
        for i in range(-60,60):
            actual_antinodes.add(a+i*delta)
p2 = len(actual_antinodes&in_range)

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
