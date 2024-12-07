import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
cals = [(int(a),list(map(int,b.split()))) for a,b in (line.split(": ") for line in lines)]

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
def un_mul(c,b):
    a,r = divmod(c,b)
    if not r:
        return a
    
def un_add(c,b):
    if c >= b:
        return c - b

def un_cat(c,b):
    a,b2 = divmod(c,10**len(str(b)))
    if b==b2:
        return a

UNOPERATORS = [un_add, un_mul]

def validate(test,nums):
    vals = {test}
    for b in nums[:0:-1]:
        vals = {unop(c,b) for c in vals for unop in UNOPERATORS if c is not None}
    return nums[0] in vals

p1 = sum(cal for cal, nums in cals if validate(cal,nums))
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
UNOPERATORS.append(un_cat)
p2 = sum(cal for cal, nums in cals if validate(cal,nums))
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
