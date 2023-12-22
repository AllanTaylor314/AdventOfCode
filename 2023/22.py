import os
from pathlib import Path
from time import perf_counter
import math
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
class Brick:
    def __init__(self, start, end):
        self.start,self.end = sorted([start,end])
        self.supports = []
        self.supported_by = []
    def __repr__(self):
        return f"Brick({self.start}, {self.end})"
    @staticmethod
    def tuple_sub(p1,p2):
        return tuple(a-b for a,b in zip(p1,p2))
    def __len__(self):
        return math.prod(1+i for i in self.tuple_sub(self.end,self.start))
    def intersect(self,other:"Brick"):
        xs1,ys1,zs1 = self.start
        xe1,ye1,ze1 = self.end
        xs2,ys2,zs2 = other.start
        xe2,ye2,ze2 = other.end
        return (xs1<=xe2 and xs2<=xe1 and
                ys1<=ye2 and ys2<=ye1 and
                zs1<=ze2 and zs2<=ze1)
    def step_down(self):
        return Brick(self.tuple_sub(self.start,(0,0,1)),
                     self.tuple_sub(self.end,(0,0,1)))
    def key_z(self):
        return self.start[2]
    def __iter__(self):
        return ((x,y,z) for x in range(self.start[0],self.end[0]+1)
                        for y in range(self.start[1],self.end[1]+1)
                        for z in range(self.start[2],self.end[2]+1))
    def __hash__(self):
        return hash((self.start,self.end))

def parse_line(line):
    a,b = line.split('~')
    return Brick(tuple(map(int,a.split(','))),tuple(map(int,b.split(','))))

with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
data = list(map(parse_line,lines))
data.sort(key=Brick.key_z)
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
# data = eval(open("22_data.py").read()) # poor man's pickle
for i in range(len(data)):
    while True:
        brick = data[i]
        new_brick = brick.step_down()
        if new_brick.start[2]<=0:
            break
        for j,b in enumerate(data):
            if i==j:
                continue
            if new_brick.intersect(b):
                break
        else:
            data[i] = new_brick
            continue
        break

data.sort(key=Brick.key_z)
# with open('22_data.py','w') as f: f.write(str(data))

for brick in data:
    dropped_brick = brick.step_down()
    for lower_brick in data:
        if brick is lower_brick: continue
        if dropped_brick.intersect(lower_brick):
            lower_brick.supports.append(brick)
            brick.supported_by.append(lower_brick)

p1 = sum(all(len(top.supported_by)>1 for top in brick.supports) for brick in data)
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
def count_falls(brick, fallen=None):
    if fallen is None:
        fallen = set()
    fallen.add(brick)
    # if I remove a brick, anything that depends on it (or on already fallen blocks) will fall
    for sub in brick.supports:
        if not (set(sub.supported_by) - fallen):
            count_falls(sub,fallen) # let it mutate the shared set
    return len(fallen) - 1 # don't count the removed block

p2 = sum(count_falls(brick) for brick in data)
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
