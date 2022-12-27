from pathlib import Path
from collections import deque

def valid_steps(z):
    global grid
    c = grid[z]
    for i in range(4):
        nz = z+1j**i
        if nz not in grid:
            continue
        nc = grid[nz]
        if ord(nc)<=ord(c)+1:
            yield nz
def valid_backsteps(z):
    global grid
    c = grid[z]
    for i in range(4):
        pz = z+1j**i
        if pz not in grid:
            continue
        pc = grid[pz]
        if ord(c)<=ord(pc)+1:
            yield pz
datapack_root = Path(R"C:\Users\allan\AppData\Roaming\.minecraft\saves\AoC2022 Day 12\datapacks\AutoAOC")
functions_folder = datapack_root/"data"/"d12"/"functions"
with open("12.txt") as file:
    lines = file.read().splitlines()
dirt_positions = [(x,y,z) for x,row in enumerate(lines) for z,c in enumerate(row) for y in (ord(c)-ord("a")-63,) if c.islower()]

grid = {i+j*1j:c for i,row in enumerate(lines) for j,c in enumerate(row)}
start ,= (z for z,c in grid.items() if c=='S')
end ,= (z for z,c in grid.items() if c=='E')
grid[start]='a'
grid[end]='z'

q = deque([(start,0)])
dists = {start:0}
while q:
    z,d = q.popleft()
    for w in valid_steps(z):
        if w not in dists:
            dists[w]=d+1
            q.append((w,d+1))
imag_to_xyz = lambda z: (int(z.real),ord(grid[z])-ord("a")-63,int(z.imag))
def hueristic(z):
    fall_heights = [ord(grid[n])-ord(grid[z]) for n in valid_steps(z)]
    wall_heights = [ord(grid[n])-ord(grid[z]) for n in valid_backsteps(z)]
    return max(wall_heights),min(fall_heights)
path_positions = set()
q2 = {end}
while q2:
    z = q2.pop()
    path_positions.add(imag_to_xyz(z))
    options = []
    for nz in valid_backsteps(z):
        if (imag_to_xyz(nz) not in path_positions
        and nz in dists and dists[nz]==dists[z]-1):
            options.append(nz)
    if options: q2.add(max(options,key=hueristic))
    if len(q2)>1000:break

path_positions.discard(imag_to_xyz(start))
path_positions.discard(imag_to_xyz(end))

with open(functions_folder/"create.mcfunction","w") as file:
    for x,y,z in dirt_positions:
        file.write(f"fill {x} -63 {-z} {x} {y} {-z} minecraft:dirt\n")
        file.write(f"setblock {x} {y} {-z} minecraft:grass_block\n")
    file.write(f"setblock {start.real:.0f} -63 {-start.imag:.0f} minecraft:glowstone\n")
    file.write(f"fill {end.real:.0f} -63 {-end.imag:.0f} {end.real:.0f} -39 {-end.imag:.0f} minecraft:dirt\n")
    file.write(f"setblock {end.real:.0f} -38 {-end.imag:.0f} minecraft:shroomlight\n")
    
with open(functions_folder/"clear.mcfunction","w") as file:
    for x in range(len(lines)):
        file.write(f"fill {x} -63 0 {x} -36 {1-len(lines[0])} minecraft:air\n")

# with open(functions_folder/"solve1.mcfunction","w") as file:
#     for x,y,z in path_positions:
#         file.write(f"setblock {x} {y} {-z} minecraft:dirt_path\n")

with open(functions_folder/"start.mcfunction","w") as file:
    file.write(f"teleport @p {start.real:.0f} -62 {-start.imag:.0f} 180 0\n")
