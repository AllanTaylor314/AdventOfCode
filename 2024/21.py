import os
from pathlib import Path
from time import perf_counter
from itertools import product
from collections import Counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
DIRECTIONS = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)][::2]
UP, RIGHT, DOWN, LEFT = DIRECTIONS
def add(*ps): return tuple(map(sum,zip(*ps)))
def sub(p1,p2):
    return tuple(a-b for a,b in zip(p1,p2))
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
num_pad_lines = """
789
456
123
.0A
""".strip().splitlines()
dir_pad_lines = """
.^A
<v>
""".strip().splitlines()
num_pad = {(i,j):c for i,line in enumerate(num_pad_lines) for j,c in enumerate(line) if c != "."}
dir_pad = {(i,j):c for i,line in enumerate(dir_pad_lines) for j,c in enumerate(line) if c != "."}
num_pad.update({v:k for k,v in num_pad.items()})
dir_pad.update({v:k for k,v in dir_pad.items()})
def manhattan_distance(a,b=(0,0)):
    d=0
    for j,k in zip(a,b):
        d+=abs(j-k)
    return d
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
def unpack_path(path,pad):
    ...
def gen_step(source, target, pad):
    ti,tj = pad[target]
    si,sj = pad[source]
    di = ti - si
    dj = tj - sj
    vert = "v"*di+"^"*-di
    horiz = ">"*dj+"<"*-dj
    if di == 0 or dj == 0:
        yield horiz+vert+"A"
    else:
        if (si,sj+dj) in pad:
            yield horiz+vert+"A"
        if (si+di,sj) in pad:
            yield vert+horiz+"A"
def step(source, target, pad):
    ti,tj = pad[target]
    si,sj = pad[source]
    di = ti - si
    dj = tj - sj
    vert = "v"*di+"^"*-di
    horiz = ">"*dj+"<"*-dj
    if dj > 0 and (ti,sj) in pad:
        return vert+horiz+"A"
    if (si,tj) in pad:
        return horiz+vert+"A"
    if (ti,sj) in pad:
        return vert+horiz+"A"
def routes(path, pad):
    out = []
    start = "A"
    for end in path:
        out.append(step(start,end,pad))
        start = end
    return "".join(out)

num_routes = [routes(line, num_pad) for line in lines]
rad_routes = [routes(route, dir_pad) for route in num_routes]
cold_routes = [routes(route, dir_pad) for route in rad_routes]
p1 = sum(len(route)*int(line[:-1]) for route, line in zip(cold_routes,lines))
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
def routes2(path, pad):
    out = []
    start = "A"
    for end in path:
        out.append(step(start,end,pad))
        start = end
    return Counter(out)

def route_len(route):
    return sum(len(k)*v for k,v in route.items())

robot_routes = [Counter([route]) for route in num_routes]
for _ in range(25):
    new_routes = []
    for route_counter in robot_routes:
        new_route = Counter()
        for sub_route, qty in route_counter.items():
            new_counts = routes2(sub_route, dir_pad)
            for k in new_counts:
                new_counts[k] *= qty
            new_route.update(new_counts)
        new_routes.append(new_route)
    robot_routes = new_routes

p2 = sum(route_len(route)*int(line[:-1]) for route, line in zip(robot_routes,lines))
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
