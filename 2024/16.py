from collections import defaultdict
import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
DIRECTIONS = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)][::2]
N,E,W,S = DIRECTIONS
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
    loc,d = state
    di,dj = d
    return {
        (add(loc,d),d):1,
        (loc,(dj,-di)):1000,
        (loc,(-dj,di)):1000
    }

# state = (location, direction): cost
init_state = (start,E)
states = defaultdict(lambda:10**10)
states[init_state] = 0
to_update = {init_state}
while to_update:
    state = to_update.pop()
    cost = states[state]
    new_states = next_states(state)
    for new_state, cost_increase in new_states.items():
        new_loc, new_d = new_state
        if grid[new_loc] == "#":
            continue
        new_cost = cost+cost_increase
        if new_cost < states[new_state]:
            states[new_state] = new_cost
            to_update.add(new_state)
end_state = min(((end,d) for d in DIRECTIONS), key=states.get)
p1 = states[end_state]
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
def prev_states(state):
    loc,d = state
    di,dj = d
    return {
        (add(loc,(-di,-dj)),d):1,
        (loc,(-dj,di)):1000,
        (loc,(dj,-di)):1000
    }

locs_on_path = {end}
to_check = {end_state}
while to_check:
    state = to_check.pop()
    cost = states[state]
    for prev_state, cost_increase in prev_states(state).items():
        prev_loc, prev_d = prev_state
        if grid[prev_loc] == "#":
            continue
        if states[prev_state] + cost_increase == cost:
            to_check.add(prev_state)
            locs_on_path.add(prev_loc)
p2 = len(locs_on_path)
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
