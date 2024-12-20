from collections import defaultdict
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
grid = {(i,j):c for i,line in enumerate(lines) for j,c in enumerate(line)}
start ,= (ij for ij,c in grid.items() if c=="S")
end ,= (ij for ij,c in grid.items() if c=="E")
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
UNREACHABLE = 10**10
def next_states(state):
    return [add(state,d) for d in DIRECTIONS]
def reverse_direction(direction):
    return tuple(-i for i in direction)
def bfs(init_state):
    states = defaultdict(lambda:UNREACHABLE)
    states[init_state] = 0
    to_update = {init_state}
    while to_update:
        state = to_update.pop()
        cost = states[state]
        for new_state in next_states(state):
            new_loc = new_state
            if grid[new_loc] == "#":
                continue
            new_cost = cost+1
            if new_cost < states[new_state]:
                states[new_state] = new_cost
                to_update.add(new_state)
    return states
p1 = 0
end_states = bfs(end)
start_states = bfs(start)
full_cost = start_states[end]

for ij,c in grid.items():
    if c == "#":
        for d in DIRECTIONS:
            before_cost = start_states[add(ij,reverse_direction(d))]
            after_cost = end_states[add(ij,d)]
            if before_cost != UNREACHABLE and after_cost != UNREACHABLE:
                savings = full_cost - after_cost - before_cost - 2
                if savings >= 100:
                    p1 += 1
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
def manhattan_distance(a,b=(0,0)):
    d=0
    for j,k in zip(a,b):
        d+=abs(j-k)
    return d
def gen_manhattan(loc, dist):
    i, j = loc
    for di in range(dist):
        dj = dist - di
        yield (i+di,j+dj)
        yield (i+dj,j-di)
        yield (i-di,j-dj)
        yield (i-dj,j+di)
p2 = 0
for ijs,cs in grid.items():
    for dist in range(1,21):
        for ije in gen_manhattan(ijs,dist):
            ce = grid.get(ije)
            if ce is None:
                continue
            if cs != "#" and ce != "#":
                before_cost = start_states[ijs]
                after_cost = end_states[ije]
                savings = full_cost - after_cost - before_cost - dist
                if savings >= 100:
                    p2 += 1
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
