import os
from pathlib import Path
from time import perf_counter
import z3
import numpy.linalg as la
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
XY_LB = 200000000000000
XY_UB = 400000000000000
def is_in_test_area(point):
    return point is not None and all(XY_LB<=c<=XY_UB for c in point)
class Point2D:
    def __init__(self,x,y,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    def intersect(self,other:"Point2D"):
        try:
            t1, t2 = la.solve([[self.dx,-other.dx],[self.dy,-other.dy]],[other.x-self.x,other.y-self.y])
        except la.LinAlgError:
            print(f"Failed to intersect {self} and {other}")
        else:
            if t1<0 or t2<0:
                return None # in the past
            return (self.x+t1*self.dx,self.y+t1*self.dy)
        return None # Parallel lines
    
    def __repr__(self) -> str:
        return f"Point2D({self.x}, {self.y}, {self.dx}, {self.dy})"

class Point3D:
    def __init__(self,x,y,z,dx,dy,dz):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.dz = dz
    
    def __repr__(self) -> str:
        return f"Point3D({self.x}, {self.y}, {self.z}, {self.dx}, {self.dy}, {self.dz})"

with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
point_tuples = [tuple(map(int,line.replace(" @",",").split(', '))) for line in lines]
points2d = [Point2D(x,y,dx,dy) for x,y,z,dx,dy,dz in point_tuples]
points3d = [Point3D(x,y,z,dx,dy,dz) for x,y,z,dx,dy,dz in point_tuples]
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = sum(is_in_test_area(a.intersect(b)) for i,a in enumerate(points2d) for b in points2d[i+1:])
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
x,y,z,u,v,w = map(z3.Int,"xyzuvw")
ts = [z3.Int(f"t{i}") for i in range(len(point_tuples))]
s = z3.Solver()
for t,c in zip(ts,points3d):
    s.add(x+t*u == c.x+t*c.dx)
    s.add(y+t*v == c.y+t*c.dy)
    s.add(z+t*w == c.z+t*c.dz)
s.check()
m = s.model()
p2 = sum(m[c].as_long() for c in (x,y,z))
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
