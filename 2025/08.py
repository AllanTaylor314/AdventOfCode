from collections import defaultdict, deque
import os
from pathlib import Path
from time import perf_counter
from itertools import combinations
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
DIRECTIONS = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)][::2]
def add(*ps): return tuple(map(sum,zip(*ps)))
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()

coords = [tuple(map(int,line.split(','))) for line in lines]

def distance2(p1,p2):
    return sum((a-b)**2 for a,b in zip(p1,p2,strict=True))

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
connections = sorted(combinations(coords, 2), key=lambda ps: distance2(*ps))

adj_matrix = defaultdict(set)
for a,b in connections[:1000]:
    adj_matrix[a].add(b)
    adj_matrix[b].add(a)

to_add = set(adj_matrix)
circuits = []
while to_add:
    root = to_add.pop()
    q = deque([root])
    current_group = set()
    while q:
        new = q.popleft()
        if new in current_group:
            continue
        current_group.add(new)
        to_add.discard(new)
        q.extend(adj_matrix[new])
    circuits.append(current_group)

*_, a, b, c = sorted(map(len, circuits))

p1 = a * b * c

print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
main_group = {coords[0]}

def expand_group(new_coord):
    q = deque([new_coord])
    new_group = set()
    while q:
        new = q.popleft()
        if new in new_group:
            continue
        new_group.add(new)
        q.extend(adj_matrix[new])
    main_group.update(new_group)

for a,b in connections[1000:]:
    if a in main_group and b not in main_group:
        expand_group(b)
    if b in main_group and a not in main_group:
        expand_group(a)
    adj_matrix[a].add(b)
    adj_matrix[b].add(a)
    if len(main_group) == len(coords):
        break
else:
    raise "idk, this shouldn't happen"

p2 = a[0] * b[0]

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
