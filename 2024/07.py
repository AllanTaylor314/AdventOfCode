import os
from pathlib import Path
from time import perf_counter
from operator import add, mul
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
cals = {int(a):list(map(int,b.split())) for a,b in (line.split(": ") for line in lines)}

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
OPERATORS = [add, mul]
def gen_vals(line,index=-1):
    index %= len(line)
    if index == 0:
        yield line[index]
    else:
        for val in gen_vals(line,index-1):
            for op in OPERATORS:
                yield op(val, line[index])

p1 = sum(cal for cal, nums in cals.items() if any(a==cal for a in gen_vals(nums)))
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
OPERATORS.append(lambda a,b:int(f"{a}{b}"))
p2 = sum(cal for cal, nums in cals.items() if any(a==cal for a in gen_vals(nums)))
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
