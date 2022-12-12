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

with open("12.txt") as file:
    lines = file.read().splitlines()
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
print("Part 1:",dists[end])
q = deque([(end,0)])
dists = {end:0}
while q:
    z,d = q.popleft()
    for w in valid_backsteps(z):
        if w not in dists:
            dists[w]=d+1
            q.append((w,d+1))
p2 = 9**9 # inf
for start in (z for z,c in grid.items() if c=='a'):
    if start in dists and dists[start]<p2:p2=dists[start]
print("Part 2:",p2)
