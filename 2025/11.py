from functools import cache
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

servers = {a[:-1]: b for a,*b in map(str.split, lines)}
# print(servers)
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
@cache
def num_paths(source):
    if source == 'out':
        return 1
    return sum(map(num_paths, servers[source]))
p1 = num_paths('you')


print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
@cache
def num_paths2(source, has_dac=False, has_fft=False):
    if source == 'out':
        return 1 if has_dac and has_fft else 0
    if source == 'dac':
        has_dac = True
    if source == 'fft':
        has_fft = True
    return sum(num_paths2(server, has_dac, has_fft) for server in servers[source])
p2 = num_paths2('svr')

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
