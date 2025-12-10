from collections import deque
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
def read_not_a_tuple(s):
    return tuple(map(int,s[1:-1].split(',')))

with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
machines = []
for line in lines:
    lights, *wiring, joltage = line.split()
    lights = tuple(c=='#' for c in lights[1:-1])
    wiring = tuple(map(read_not_a_tuple,wiring))
    joltage = read_not_a_tuple(joltage)
    machines.append((lights, wiring, joltage))

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
def apply(lights, button):
    return tuple(on != (i in button) for i,on in enumerate(lights))
# @cache
# def min_pushes(lights, wiring):
#     if not any(lights): # all off
#         return 0
#     return min(min_pushes(apply(lights, button),wiring) for button in wiring) + 1

def min_pushes(lights, wiring):
    q = deque([lights])
    costs = {lights: 0}
    while q:
        state = q.popleft()
        new_cost = costs[state] + 1
        for b in wiring:
            new_state = apply(state, b)
            if new_state in costs:
                continue
            costs[new_state] = new_cost
            q.append(new_state)
            if not any(new_state):
                return new_cost

p1 = 0
for lights, wiring, joltage in machines:
    p1 += min_pushes(lights, wiring)

print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
import z3
def min_pushes3(joltages, wiring):
    opt = z3.Optimize()
    button_push_counts = [z3.Int(f'button_push_{i}') for i in range(len(wiring))]
    for j, jolt in enumerate(joltages):
        tot = 0
        for i,button in enumerate(wiring):
            if j in button:
                tot += button_push_counts[i]
        opt.add(tot == jolt)
    for b in button_push_counts:
        opt.add(b >= 0)
    h = opt.minimize(z3.Sum(button_push_counts))
    assert opt.check() == z3.sat
    return opt.lower(h).py_value()


# def apply2(jolts, button):
#     return tuple(jolt - (i in button) for i,jolt in enumerate(jolts))

# def min_pushes2(joltages, wiring):
#     q = deque([joltages])
#     costs = {joltages: 0}
#     while q:
#         state = q.popleft()
#         new_cost = costs[state] + 1
#         for b in wiring:
#             new_state = apply2(state, b)
#             if new_state in costs or any(j < 0 for j in new_state):
#                 continue
#             costs[new_state] = new_cost
#             q.append(new_state)
#             if not any(new_state):
#                 return new_cost

p2 = 0
for lights, wiring, joltage in machines:
    mp = min_pushes3(joltage, wiring)
    print(joltage, mp)
    p2 += mp
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
