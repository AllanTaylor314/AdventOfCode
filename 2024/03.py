import os
import re
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read()
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
pairs = (map(int,line) for line in re.findall(pattern,lines))
p1 = sum(a*b for a,b in pairs)
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
data = [line.split("don't()")[0] for line in lines.split("do()")]
p2 = sum(a*b for a,b in (map(int,line) for line in re.findall(pattern,"X".join(data))))
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
