import os
from pathlib import Path
from time import perf_counter
from collections import deque
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
dir_map = {"U":-1j,"R":1+0j,"L":-1+0j,"D":1j}
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
steps1 = [(dir_map[dr],int(ds),col) for dr,ds,col in (line.split() for line in lines)]
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
def print_grid(grid):
    minx = int(min(c.real for c in grid))
    miny = int(min(c.imag for c in grid))
    maxx = int(max(c.real for c in grid))
    maxy = int(max(c.imag for c in grid))
    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            print(end='.#'[complex(x,y) in grid])
        print()

def solver(steps):
    holes = {0j}
    loc = 0
    for dr,ds,col in steps:
        for _ in range(ds):
            loc += dr
            holes.add(loc)
    minx = int(min(c.real for c in holes))
    miny = int(min(c.imag for c in holes))
    maxx = int(max(c.real for c in holes))
    maxy = int(max(c.imag for c in holes))
    fill = set()
    start = complex((minx+maxx)//2,(miny+maxy)//2) # not perfect
    fill.add(start)
    q = deque(fill)
    while q:
        xy = q.popleft()
        if xy in holes:
            continue # edge
        for dxy in dir_map.values():
            if xy+dxy not in fill:
                fill.add(xy+dxy)
                q.append(xy+dxy)
    return len(holes|fill)

p1 = solver(steps1)
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
def shoelace(points:list):
    return sum((i.imag+j.imag)*(i.real-j.real) for i,j in zip(points,points[1:]+points[:1]))/2

def quick_solver(steps):
    edge_list = [0j]
    edge_length = 0
    loc = 0
    for dr,ds,col in steps:
        loc += dr*ds
        edge_length += ds
        edge_list.append(loc)
    return abs(int(shoelace(edge_list))+edge_length//2+1) # Pick's theorem?

assert quick_solver(steps1) == p1 # check it still works

steps2 = [(dir_map["RDLU"[int(col[-2])]],int(col[2:7],16),col) for dr,ds,col in steps1]
p2 = quick_solver(steps2)

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
