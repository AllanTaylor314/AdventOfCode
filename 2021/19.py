import numpy as np
from itertools import permutations, product
from collections import defaultdict, Counter

def orientations(xyz):
    ox,oy,oz = xyz
    out=[]
    for dx in (1,-1):
        x=ox*dx
        for dy in (1,-1):
            y=oy*dy
            for dz in (1,-1):
                z = dz*oz
                out.extend(permutations((x,y,z)))
    return out

IDENTITY = np.array([[1,0,0],[0,1,0],[0,0,1]])
ROTATIONS = [r for r in map(np.array,orientations(IDENTITY)) if np.linalg.det(r)==1]

class Scanner:
    def __init__(self, sid, beacons):
        self.scan_id = sid
        self.beacons = np.array(beacons)
        self.rotation = None
        self.position = None
    def global_positions(self, xyz=None, rotation=None):
        if rotation is None:
            if self.rotation is None: raise ValueError
            rotation = self.rotation
        if xyz is None:
            if self.position is None: raise ValueError
            xyz = self.position
        return list(map(tuple,self.beacons @ rotation + xyz))
    def overlap(self,other):
        return set(self.differences)&set(other.differences)
    def __repr__(self):
        return f"Scanner({self.scan_id}, \n{self.beacons}\n)"
    def all_dists(self,other):
        for r in ROTATIONS:
            for a,b in product(self.beacons,other.beacons @ r):
                yield sum(np.abs(a-b))
    def probable_rot_dist(self,other):
        for r_index,r in enumerate(ROTATIONS):
            l=[]
            for a,b in product(self.beacons,other.beacons @ r):
                l.append(tuple(a-b))
            dist,count = Counter(l).most_common(1)[0]
            if count>=12: return r_index,dist

with open('19.txt') as file:
    data = file.read()
scans = data.split('\n\n')
scanners = {}
for sid,scan in enumerate(scans):
    header, *coords = scan.splitlines()
    scanners[sid]=Scanner(sid,[tuple(map(int,c.split(','))) for c in coords])

scanners[0].rotation = IDENTITY
scanners[0].position = np.array([0,0,0])

prob_rot_dists = defaultdict(dict)
for i,s0 in scanners.items():
    for j,s1 in scanners.items():
        if i==j: continue
        res = s0.probable_rot_dist(s1)
        if res is not None:
            prob_rot_dists[i][j] = res

def positions_relative_to_a(a=0,ignore=None):
    if ignore is None: ignore = set()
    ignore.add(a)
    global prob_rot_dists, scanners
    output = [scanners[a].beacons]
    for b,(roti,offset) in prob_rot_dists[a].items():
        if b in ignore: continue
        r = ROTATIONS[roti]
        p = np.array(offset)
        rpos = positions_relative_to_a(b,ignore)
        output.append(rpos @ r + p)
        ignore.add(b)
    return np.concatenate(output)

NP_GLOBAL_POSITIONS = positions_relative_to_a()
GLOBAL_POSITIONS_SET = set(map(tuple,NP_GLOBAL_POSITIONS))
print('Part 1:',len(GLOBAL_POSITIONS_SET))

def relative_scanner_positions(a=0,ignore=None):
    if ignore is None: ignore = set()
    ignore.add(a)
    global prob_rot_dists, scanners
    output = [np.array([(0,0,0)])]
    for b,(roti,offset) in prob_rot_dists[a].items():
        if b in ignore: continue
        r = ROTATIONS[roti]
        p = np.array(offset)
        rpos = relative_scanner_positions(b,ignore)
        output.append(rpos @ r + p)
        ignore.add(b)
    return np.concatenate(output)

GLOBAL_SCANNER_POSITIONS = relative_scanner_positions()
mh_dists = []
for a in GLOBAL_SCANNER_POSITIONS:
    for b in GLOBAL_SCANNER_POSITIONS:
        mh_dists.append(sum(np.abs(a-b)))
print('Part 2:',max(mh_dists))

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
axes = plt.axes(projection='3d')
axes.plot3D(*zip(*GLOBAL_SCANNER_POSITIONS),'ro')
axes.plot3D(*zip(*GLOBAL_POSITIONS_SET),'bo')
