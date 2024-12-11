import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
from collections import Counter
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    data = list(map(int,file.read().strip().split()))

timer_parse_end=timer_part1_start=timer_part2_start=perf_counter()
############################## PART 1 ##############################
stones = Counter(data)
for _ in range(75):
    if _ == 25:
        p1 = sum(stones.values())
        print("Part 1:",p1)
        timer_part1_end=perf_counter()
    new_stones = Counter()
    for stone, qty in stones.items():
        if stone == 0:
            new_stones[1] += qty
        elif len(str(stone)) % 2 == 0:
            full = str(stone)
            left = int(full[:len(full)//2])
            right = int(full[len(full)//2:])
            new_stones[left] += qty
            new_stones[right] += qty
        else:
            new_stones[stone * 2024] += qty
    stones = new_stones
############################## PART 2 ##############################
p2 = sum(stones.values())
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
