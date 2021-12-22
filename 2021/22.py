from itertools import product
from collections import Counter

def sector_size(sector):
    s = 1
    for a,b in sector:
        s*=(b-a+1)
    return s

with open('22.txt') as file:
    data = file.read()
instructions = []
for line in data.splitlines():
    on_off,xyz = line.split()
    io = {'on':1,'off':-1}[on_off]
    xr,yr,zr = xyz.split(',')
    minx,maxx = xr[2:].split('..')
    miny,maxy = yr[2:].split('..')
    minz,maxz = zr[2:].split('..')
    instructions.append((io,(int(minx),int(maxx)),(int(miny),int(maxy)),(int(minz),int(maxz))))

grid = {(x,y,z):0 for x,y,z in product(range(-50,51),repeat=3)}

for io,(mx,Mx),(my,My),(mz,Mz) in instructions:
    for xyz in product(range(max(mx,-50),min(Mx,50)+1),
                       range(max(my,-50),min(My,50)+1),
                       range(max(mz,-50),min(Mz,50)+1)):
        grid[xyz] = max(io,0)

print('Part 1:',sum(grid.values()))

# Almost entirely taken from
# https://www.reddit.com/r/adventofcode/comments/rlxhmg/comment/hpizza8/
cubes = Counter() # Use counter so that update adds values (not replace)
for nsgn,(nx0,nx1),(ny0,ny1),(nz0,nz1) in instructions:
    new = Counter()
    # Existing cubes
    for ((ex0,ex1),(ey0,ey1),(ez0,ez1)), esgn in cubes.items():
        # Intersecting cube bounds
        ix0 = max(nx0,ex0)
        ix1 = min(nx1,ex1)
        iy0 = max(ny0,ey0)
        iy1 = min(ny1,ey1)
        iz0 = max(nz0,ez0)
        iz1 = min(nz1,ez1)
        # If it does in fact intersect, counteract the existing sign
        if ix0<=ix1 and iy0<=iy1 and iz0<=iz1:
            new[(ix0,ix1),(iy0,iy1),(iz0,iz1)] -= esgn
    # Only add the current cubes volume if it turns stuff on
    if nsgn > 0:
        new[(nx0,nx1),(ny0,ny1),(nz0,nz1)] += nsgn
    cubes.update(new)

print('Part 2:',sum((sector_size(sec)*sgn for sec,sgn in cubes.items())))
