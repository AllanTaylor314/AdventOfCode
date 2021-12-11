from queue import Queue
from itertools import permutations
DXDY=((0,-1),(0,1),(-1,0),(1,0))

def bfs_dist(axy,bxy):
    if axy==bxy:return 0
    visited=set()
    global loc_map
    q=Queue()
    q.put(axy+(0,))
    while q.qsize():
        x,y,d = q.get()
        if (x,y)==bxy: return d
        for dx,dy in DXDY:
            nx,ny=x+dx,y+dy
            if loc_map[ny][nx]=='#' or (nx,ny) in visited:continue
            if (nx,ny)==bxy:return d+1
            q.put((nx,ny,d+1))
            visited.add((nx,ny))

with open('24.txt') as file:
    data=file.read()

loc_map=[]
num_locs={}
for y,line in enumerate(data.splitlines()):
    loc_map.append([])
    for x,c in enumerate(line):
        loc_map[y].append(c)
        if c.isdigit():
            num_locs[int(c)]=x,y

dist_dict = {}
for n0,xy0 in num_locs.items():
    for n1,xy1 in num_locs.items():
        dist_dict[n0,n1]=bfs_dist(xy0,xy1)

dists=[]
dists2=[]
for perm in permutations(tuple(range(1,len(num_locs)))):
    dists.append(sum(dist_dict[step] for step in zip((0,)+perm,perm)))
    dists2.append(sum(dist_dict[step] for step in zip((0,)+perm,perm+(0,))))
print('Part 1:',min(dists))
print('Part 2:',min(dists2))
