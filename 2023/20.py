import os
from pathlib import Path
from time import perf_counter
from collections import deque, defaultdict
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
data = {a.lstrip('%&'):(a[0] if a[0]in"%&"else None,b.split(', ')) for a,b in (line.split(' -> ') for line in lines)}
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
BUTTON_PUSH = ('broadcaster',False,None)
wire = deque([BUTTON_PUSH])
states = defaultdict(bool)
def connect_conjunctions():
    for k,(t,_) in data.items():
        if t == '&':
            states[k] = {}
    for k,(t,ds) in data.items():
        for d in ds:
            if d in states:
                states[d][k] = False
def process_signal(module,pulse,src):
    global data,wire,states
    if module not in data:
        return
    module_type, destinations = data[module]
    if module_type == '%': # Flip-flop
        if not pulse:
            state = states[module] = not states[module]
            for dest in destinations:
                wire.append((dest,state,module))
    elif module_type == '&': # Conjunction
        states[module][src] = pulse
        state = not all(states[module].values())
        for dest in destinations:
            wire.append((dest,state,module))
    else: # None
        for dest in destinations:
            wire.append((dest,pulse,module))

connect_conjunctions()

counts = [0,0]
for _ in range(1000):
    while wire:
        mod,pulse,src = wire.popleft()
        counts[pulse] += 1
        process_signal(mod,pulse,src)
    wire.append(BUTTON_PUSH)
p1 = counts[0] * counts[1]
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
p2 = 0

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
