import re
TEST = 0

def manhattan(a,b):
    u,v=a
    x,y=b
    return abs(u-x)+abs(v-y)

with open("15.txt") as file:
    lines = file.read().splitlines()
Y1 = 2000000
if TEST:
    lines = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines()
    Y1 = 10

SENSORS = {}
BEACONS = set()
nums = [tuple(map(int,re.findall(r"([\-\d]+)",line))) for line in lines]
sensor_distances = {}
ranges = []
for sx,sy,bx,by in nums:
    SENSORS[(sx,sy)] = (bx,by)
    BEACONS.add((bx,by))
    taxicab = manhattan((sx,sy),(bx,by))
    sensor_distances[sx,sy]=taxicab
    ranges.append(range(sx-(taxicab-abs(sy-Y1)),sx+(taxicab-abs(sy-Y1)+1)))

def print_grid():
    num_empty = 0
    num_y1 = 0
    for y in range(-2,23):
        for x in range(-4,27):
            if (x,y) in SENSORS:
                print(end="S")
            elif (x,y) in BEACONS:
                print(end="B")
            elif any(manhattan((x,y),s)<=manhattan(b,s) for s,b in SENSORS.items()):
                print(end="#")
                num_empty+=1
                if y==Y1:
                    num_y1+=1
            else:
                print(end=".")
        print(f"(Finished y={y})")
    print(num_empty,num_y1)

rset = set()
for r in ranges: rset.update(r)
rset-={x for x,y in BEACONS if y==Y1}
print("Part 1:",len(rset)) # not 4858853, 4858851, 4919282; is 4919281

# 0<=x,y<=4_000_000
ex,ey = 3157535,3363767
print("Part 2:",ex*4000000+ey) # 41646000000 too low
for (sx,sy),dist in sorted(sensor_distances.items(),key=lambda _:-_[1]):
    # print(f"{sx:10,d}, {sy:10,d}:{dist:10,d}")
    print(R"\operatorname{abs}\left(x-"+str(sx)+R"\right)+\operatorname{abs}\left(y-"+str(sy)+R"\right)\le"+str(dist)+r"-a")

# Paste that into desmos (https://www.desmos.com/calculator/rq42ebsqns), slide a=1000000 down to a=0 to pinpoint the empty square
