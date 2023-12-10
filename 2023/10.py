import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
ALL_DIR = frozenset((-1,1,1j,-1j))
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
grid = {j+i*1j:c for i,line in enumerate(lines) for j,c in enumerate(line)}
start ,= [k for k,v in grid.items() if v=='S']
# grid[start] = 'L' # manual - what I actually used
# auto - done later
options = set('FL7J-|')
if grid[start-1] in '.|7J':
    options.discard('7')
    options.discard('J')
    options.discard('-')
if grid[start+1] in '.|FL':
    options.discard('F')
    options.discard('L')
    options.discard('-')
if grid[start-1j] in '.-LJ':
    options.discard('L')
    options.discard('J')
    options.discard('|')
if grid[start+1j] in '.-F7':
    options.discard('F')
    options.discard('7')
    options.discard('|')
grid[start] ,= options
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
lut = {
    ('L',+1j):+1,
    ('L',-1):-1j,
    ('J',+1j):-1,
    ('J',+1):-1j,
    ('7',+1):+1j,
    ('7',-1j):-1,
    ('F',-1j):+1,
    ('F',-1):+1j,
    ('|',+1j):+1j,
    ('|',-1j):-1j,
    ('-',-1):-1,
    ('-',+1):+1,
}
# direction = 1 # manual right
direction = next(lut[grid[start],d] for d in ALL_DIR if (grid[start],d) in lut)
path = [start,start+direction]
p1 = 1
while path[-1] != start:
    direction = lut[grid[path[-1]],direction]
    path.append(path[-1]+direction)
    p1 += 1
p1 //= 2
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
## Draw a pretty picture!
# from turtle import *
# wn = Screen()
# wn.tracer(0)
# t = Turtle()
# t.hideturtle()
# t.speed("fastest")
# for p in path:
#     p = (p-start) * 3
#     t.goto(p.real,-p.imag)
# wn.update()
lut_left = {
    ('L',+1j):set(),
    ('L',-1):{-1,+1j},
    ('J',+1j):{+1j,+1},
    ('J',+1):set(),
    ('7',+1):{-1j,+1},
    ('7',-1j):set(),
    ('F',-1j):{-1j,-1},
    ('F',-1):set(),
    ('|',+1j):{+1},
    ('|',-1j):{-1},
    ('-',-1):{+1j},
    ('-',+1):{-1j},
}
left_points = set()
right_points = set()
for p0,p1 in zip(path[-2:-1]+path[:-2],path): # start is repeated, so exclude final
    d = p1-p0
    left_points|={p1+p for p in lut_left[grid[p1],d]}
    right_points|={p1+p for p in ALL_DIR-lut_left[grid[p1],d]}
path_set = set(path)
left_points -= path_set
right_points -= path_set
remaining_points = set(grid) - path_set - left_points - right_points
remaining_points.add(-1) # outside canary - to tell inside from out
while remaining_points: # aint pretty but it works
    tmp = set()
    for p in left_points:
        for d in ALL_DIR:
            p0 = p+d
            if p0 in remaining_points:
                tmp.add(p0)
                remaining_points.remove(p0)
    left_points|=tmp

    tmp = set()
    for p in right_points:
        for d in ALL_DIR:
            p0 = p+d
            if p0 in remaining_points:
                tmp.add(p0)
                remaining_points.remove(p0)
    right_points|=tmp
assert not left_points&right_points
if -1 in left_points:
    p2 = len(right_points)
elif -1 in right_points:
    p2 = len(left_points)
else:
    raise ValueError("The canary flew away!")
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
