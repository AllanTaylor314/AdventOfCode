import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    steps = file.read().strip().split(',')

def HASH(s):
    v = 0
    for c in s:
        v+=ord(c)
        v*=17
        v%=256
    return v

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = sum(map(HASH,steps))
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
lens = [{} for _ in range(256)]
for step in steps:
    if '-' == step[-1]:
        l = step[:-1]
        h = HASH(l)
        if l in lens[h]:
            del lens[h][l]
    else:
        l,v = step.split('=')
        h = HASH(l)
        lens[h][l] = int(v)

p2 = 0
for box_n, hmap in enumerate(lens):
    for lens_n, focal_length in enumerate(hmap.values(),1):
        p2 += (box_n + 1) * lens_n * focal_length

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
