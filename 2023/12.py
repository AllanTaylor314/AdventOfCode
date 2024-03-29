import os
from pathlib import Path
from time import perf_counter
from functools import cache
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
# nonograms. great.
data = []
for line in lines:
    springs, cluestr = line.split()
    clues = tuple(map(int,cluestr.split(',')))
    data.append((springs,clues))
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
@cache
def num_valid_arrangements(springs, clues, run_size = 0):
    if not springs:
        if ((len(clues)==1 and clues[0] == run_size)
        or (len(clues)==0 and run_size == 0)):
            return 1
        return 0
    spring = springs[0]
    springs = springs[1:]
    clue, *new_clues = clues or [0]
    new_clues = tuple(new_clues)
    if spring == '?':
        return num_valid_arrangements('#'+springs, clues, run_size) + num_valid_arrangements('.'+springs, clues, run_size)
    if spring == '#':
        return 0 if run_size > clue else num_valid_arrangements(springs, clues, run_size + 1)
    if spring == '.':
        if run_size == 0:
            return num_valid_arrangements(springs, clues, 0)
        if run_size == clue:
            return num_valid_arrangements(springs, new_clues, 0)
        return 0
    raise ValueError("Spring not one of #.?")


p1 = sum(num_valid_arrangements(*sc) for sc in data)
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
def unfold(springs, clues):
    return "?".join([springs]*5), clues*5


p2 = sum(num_valid_arrangements(*unfold(*sc)) for sc in data)
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
