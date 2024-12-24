import os
from pathlib import Path
from time import perf_counter
from functools import cache
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
inputs = list(wires)
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
rev_rules = {tuple(v):k for k,v in rules.items()}
rev_rules.update({tuple(reversed(v)):k for k,v in rules.items()})
@cache
def dependencies(rule):
    if rule in inputs:
        return set()
    left, op, right = rules[rule]
    return dependencies(left)|dependencies(right)|{left,right}

p2 = 0
i = 0
sum_out = rev_rules[f"x{i:02d}","XOR",f"y{i:02d}"]
carry_out = rev_rules[f"x{i:02d}","AND",f"y{i:02d}"]
s_ins = rules[f"z{i:02d}"]
for i in range(1,len(inputs)//2):
    ha_out = rev_rules[f"x{i:02d}","XOR",f"y{i:02d}"]
    hac_out = rev_rules[f"x{i:02d}","AND",f"y{i:02d}"]
    hac2_out = rev_rules[ha_out,"AND",carry_out]
    sum_out = rev_rules[ha_out,"XOR",carry_out]
    carry_out = rev_rules[hac_out,"OR",hac2_out]
    print(f"{i:02d}: ",sum_out, carry_out)

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
