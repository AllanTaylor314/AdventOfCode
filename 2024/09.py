import os
from pathlib import Path
from time import perf_counter
from itertools import zip_longest
from heapq import heappop, heappush
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    data = file.read().strip()
# data = "2333133121414131402"
nums = list(map(int,data))
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
file_system = []
for i,n in enumerate(nums):
    fid = i//2
    if i%2: # gap
        file_system.extend((None for _ in range(n)))
    else:
        file_system.extend((fid for _ in range(n)))

left_ptr = 0
while True:
    while file_system[-1] is None:
        file_system.pop()
    while left_ptr < len(file_system) and file_system[left_ptr] is not None:
        left_ptr += 1
    if left_ptr >= len(file_system):
        break
    file_system[left_ptr] = file_system.pop()

p1 = sum(a*b for a,b in enumerate(file_system))
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
fills = nums[::2]
frees = nums[1::2]

running_space = 0
fill_locs = []
free_heaps = [[] for i in range(10)]
for fid,(fill,free) in enumerate(zip_longest(fills,frees,fillvalue=0)):
    fill_locs.append((running_space, fill))
    running_space += fill
    free_heaps[free].append(running_space)
    running_space += free

for fid in reversed(range(len(fill_locs))):
    fill_index, fill_size = fill_locs[fid]
    free_index = fill_index
    for size in range(fill_size, 10):
        heap = free_heaps[size]
        if heap:
            index = heap[0]
            if index < free_index:
                free_index = index
                free_size = size
    if free_index != fill_index:
        fill_locs[fid] = free_index, fill_size
        heappop(free_heaps[free_size])
        heappush(free_heaps[free_size-fill_size], free_index+fill_size)

p2 = sum(fid*sum(range(fi,fi+fs)) for fid,(fi,fs) in enumerate(fill_locs))
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
