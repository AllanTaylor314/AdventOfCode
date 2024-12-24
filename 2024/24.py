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
mid = lines.index("")
wires = {k:int(v) for k,v in (line.split(": ") for line in lines[:mid])}
rule_lines = lines[mid+1:]
ops = {"AND":lambda a,b:a*b, "OR":lambda a,b:a or b, "XOR":lambda a,b:int(a!=b)}
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
rules = {v[4]:v[:3] for v in map(str.split,rule_lines)}
rule_queue = list(rules)
while rule_queue:
    wire = rule_queue.pop()
    if wire in wires:
        continue
    left, op, right = rules[wire]
    left_op = wires.get(left)
    right_op = wires.get(right)
    if left_op is None or right_op is None:
        rule_queue.append(wire)
        if left_op is None:
            rule_queue.append(left)
        if right_op is None:
            rule_queue.append(right)
    else:
        wires[wire] = ops[op](left_op,right_op)
zs = sorted((wire for wire in wires if wire[0]=="z"), reverse=True)
z_vals = "".join(map(str,map(wires.get,zs)))
p1 = int(z_vals,2)

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
