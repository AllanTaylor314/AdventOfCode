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

with open("12.txt") as file:
    lines = file.read().splitlines()
# lines = """Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi""".splitlines()
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
p2 = 9**9 # inf
for start in (z for z,c in grid.items() if c=='a'):
    q = deque([(start,0)])
    dists = {start:0}
    while q:
        z,d = q.popleft()
        for w in valid_steps(z):
            if w not in dists:
                dists[w]=d+1
                q.append((w,d+1))
    if end in dists and dists[end]<p2:p2=dists[end]
print("Part 2:",p2)
