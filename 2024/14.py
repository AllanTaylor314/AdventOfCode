from itertools import count
import os
from pathlib import Path
from time import perf_counter
import re
from math import prod, lcm
from PIL import Image
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
DIRECTIONS = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,1)][::2]
def add(*ps): return tuple(map(sum,zip(*ps)))
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
data = [tuple(map(int,re.findall(r"-?\d+",line))) for line in lines]
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = 0
width, height = 101, 103
time = 100
def get_quadrant(location):
    x,y = location
    if x == width//2 or y == height//2:
        return 0
    return (x<width//2)*2+(y<height//2)+1
end_locs = []
for px, py, vx, vy in data:
    loc = (px+vx*time)%width, (py+vy*time)%height
    end_locs.append(loc)
quads = [0 for _ in range(5)]
for loc in end_locs:
    quads[get_quadrant(loc)] += 1
p1 = prod(quads[1:])
print("Part 1:",p1) # not 230582440
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
GENERATE_TEXT = False
GENERATE_IMAGES = False
p2 = 0
def how_disconnected(locations):
    num_isolated = 0
    for loc in locations:
        neis = {add(loc,d) for d in DIRECTIONS}
        if not neis & locations:
            num_isolated += 1
    return num_isolated
def covered_area(locations):
    xs, ys = zip(*locations)
    return (max(xs)-min(xs)+1),(max(ys)-min(ys)+1)
def spread(locations):
    xs, ys = zip(*locations)
    mx = sum(xs)/len(xs)
    my = sum(ys)/len(ys)
    ex = sum(abs(x-mx) for x in xs)
    ey = sum(abs(y-my) for y in ys)
    return ex, ey

if GENERATE_TEXT:
    f = open("14-out.txt","w")

for time in range(width*height):
    locs = {((px+vx*time)%width, (py+vy*time)%height) for px, py, vx, vy in data}
    if GENERATE_TEXT:
        print(time,file=f)
        for y in range(height):
            for x in range(width):
                print(end=" #"[(x,y) in locs],file=f)
            print(file=f)
        print(file=f,flush=True)
    if GENERATE_IMAGES:
        img = Image.new("1",(width,height))
        for loc in locs:
            img.putpixel(loc,1)
        img.save(SCRIPT_PATH.parent/"14-out"/f"{time:05d}.png")

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
