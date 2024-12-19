import os
from pathlib import Path
from time import perf_counter
import re
from math import prod
from PIL import Image
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
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
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
GENERATE_TEXT = False
GENERATE_IMAGES = False

def spread(locations):
    xs, ys = zip(*locations)
    mx = sum(xs)/len(xs)
    my = sum(ys)/len(ys)
    ex = sum(abs(x-mx) for x in xs)
    ey = sum(abs(y-my) for y in ys)
    return ex, ey

if GENERATE_TEXT:
    f = open("14-out.txt","w")
min_x_spread = min_y_spread = 10**10
min_x_spread_time = min_y_spread_time = 0

n_loops = width*height if GENERATE_TEXT or GENERATE_IMAGES else max(width, height)
for time in range(n_loops):
    locations = [((px+vx*time)%width, (py+vy*time)%height) for px, py, vx, vy in data]
    if GENERATE_TEXT:
        loc_set = set(locations)
        print(time,file=f)
        for y in range(height):
            for x in range(width):
                print(end=" #"[(x,y) in loc_set],file=f)
            print(file=f)
        print(file=f,flush=True)
    if GENERATE_IMAGES:
        img = Image.new("1",(width,height))
        for loc in locations:
            img.putpixel(loc,1)
        img.save(SCRIPT_PATH.parent/"14-out"/f"{time:05d}.png")
    sx, sy = spread(locations)
    if sx < min_x_spread:
        min_x_spread = sx
        min_x_spread_time = time
    if sy < min_y_spread:
        min_y_spread = sy
        min_y_spread_time = time

p2 = next(i for i in range(width*height) if i%width==min_x_spread_time and i%height==min_y_spread_time)
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
