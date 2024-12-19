from collections import defaultdict, deque
import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
DIRECTIONS = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)][::2]
def add(*ps): return tuple(map(sum,zip(*ps)))
INF_COST = 10**10
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
all_nums = [tuple(map(int,line.split(","))) for line in lines]
min_location = 0
max_location = 70

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
def get_path(nums):
    walls = set(nums)
    costs = defaultdict(lambda:INF_COST)
    start = (0,0)
    costs[start] = 0
    to_update = deque([start])
    while to_update:
        loc = to_update.popleft()
        new_cost = costs[loc] + 1
        new_locs = [(i,j) for i,j in (add(d,loc) for d in DIRECTIONS)
            if min_location<=i<=max_location
            and min_location<=j<=max_location
            and (i,j) not in walls]
        for new_loc in new_locs:
            if new_cost < costs[new_loc]:
                costs[new_loc] = new_cost
                to_update.append(new_loc)
    return costs[max_location,max_location]
p1 = get_path(all_nums[:1024])

print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
def binary_search(lb=0, ub=len(all_nums)-1):
    if lb >= ub:
        return lb
    mid = (lb+ub)//2
    res = get_path(all_nums[:mid+1])
    if res == INF_COST:
        return binary_search(lb,mid)
    return binary_search(mid+1,ub)
n = all_nums[binary_search()]
p2 = f"{n[0]},{n[1]}"

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
