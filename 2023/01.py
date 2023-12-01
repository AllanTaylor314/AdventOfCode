import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open(INPUT_PATH) as file:
    lines = file.read().splitlines()

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = 0
for line in lines:
    ints = [c for c in line if c.isdigit()]
    p1+=int(ints[0]+ints[-1])
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
p2 = 0
for line in lines:
    for c,dig in zip("123456789",DIGITS):
        line=line.replace(dig,dig+c+dig) # Deal with overlapping digits ("oneight")
    ints = [c for c in line if c.isdigit()]
    p2+=int(ints[0]+ints[-1])
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
