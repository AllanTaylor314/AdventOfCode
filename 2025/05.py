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
    lines = [tuple(map(int,line.split('-'))) for line in file.read().splitlines() if line]
ingredient_ranges = [l for l in lines if len(l) == 2]
available_ingredients = [l[0] for l in lines if len(l) == 1]
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
def in_range(rng, n):
    a,b = rng
    return a <= n <= b

def in_any_range(rngs, n):
    return any(in_range(rng, n) for rng in rngs)

p1 = sum(in_any_range(ingredient_ranges, n) for n in available_ingredients)

print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
sorted_ranges = sorted(ingredient_ranges)
deduped = []
for c,d in sorted_ranges:
    if not deduped:
        deduped.append((c,d))
    else:
        a,b = deduped[-1]
        if d <= b:
            continue
        elif c <= b:
            deduped[-1] = (a,d)
        else:
            deduped.append((c,d))
p2 = sum(b-a+1 for a,b in deduped)

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
