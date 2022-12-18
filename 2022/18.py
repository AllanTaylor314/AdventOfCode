
def adj_cubes(cube):
    a,b,c = cube
    yield a+1,b,c
    yield a-1,b,c
    yield a,b+1,c
    yield a,b-1,c
    yield a,b,c+1
    yield a,b,c-1
with open("18.txt") as file:
    lines = file.read().splitlines()
cubes = [tuple(map(int,line.split(","))) for line in lines]
scanned_cubes = set()
p1 = 0
# +6 -2*(num_adj)
for cube in cubes:
    p1 += 6
    for adj in adj_cubes(cube):
        if adj in scanned_cubes:
            p1 -= 2
    scanned_cubes.add(cube)
print("Part 1:",p1)
p2 = p1
xs,ys,zs = zip(*cubes)
minx=min(xs)
maxx=max(xs)
miny=min(ys)
maxy=max(ys)
minz=min(zs)
maxz=max(zs)
all_cubes = {(x,y,z) for x in range(minx-1,maxx+2) for y in range(miny-1,maxy+2) for z in range(minz-1,maxz+2)}
empty_cubes = all_cubes-scanned_cubes
q = [(minx-1,miny-1,minz-1)]
while q:
    c = q.pop()
    if c in empty_cubes:
        empty_cubes.remove(c)
        q.extend(adj_cubes(c))
for cube in empty_cubes:
    for adj in adj_cubes(cube):
        if adj in scanned_cubes:
            p2 -= 1
print("Part 2:",p2)
