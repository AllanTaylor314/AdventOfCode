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
def next_states(state):
    return [add(state,d) for d in DIRECTIONS]
def reverse_direction(direction):
    return tuple(-i for i in direction)
p1 = 0
init_state = end
states = defaultdict(lambda:10**10)
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
for ij,c in grid.items():
    if c == "#":
        for d in DIRECTIONS:
            before_cost = states[add(ij,reverse_direction(d))]
            after_cost = states[add(ij,d)]
            if before_cost != 10**10 and after_cost !=10**10:
                savings = after_cost - before_cost - 2
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
p2 = 0
for ijs,cs in grid.items():
    for ije,ce in grid.items():
        if ije == ijs:
            continue
        if manhattan_distance(ije, ijs) > 20:
            continue
        if cs != "#" and ce != "#":
            before_cost = states[ijs]
            after_cost = states[ije]
            if before_cost != 10**10 and after_cost !=10**10:
                savings = after_cost - before_cost - manhattan_distance(ijs,ije)
                if savings >= 100:
                    p2 += 1
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
