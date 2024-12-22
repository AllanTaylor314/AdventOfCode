import os
from pathlib import Path
from time import perf_counter
from collections import Counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
nums = list(map(int,lines))
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
PRUNE_MOD = 16777216

p1 = 0
costs = []
for secret in nums:
    costs.append([])
    for _ in range(2000):
        secret = (secret << 6 ^ secret) % PRUNE_MOD
        secret = (secret >> 5 ^ secret) % PRUNE_MOD
        secret = (secret <<11 ^ secret) % PRUNE_MOD
        costs[-1].append(secret%10)
    p1 += secret

print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
cost_deltas = [[b-a for a,b in zip(cost,cost[1:])] for cost in costs]

total_counts = Counter()
for i,deltas in enumerate(cost_deltas):
    this_count = Counter()
    for j in range(len(deltas)-4):
        pattern = tuple(deltas[j:j+4])
        if pattern not in this_count:
            this_count[pattern] += costs[i][j+4]
    total_counts.update(this_count)

p2 = max(total_counts.values())
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
