import numpy as np
from collections import defaultdict

PART2=False
VISUALISE=False

DXDY=((0,-1),(0,1),(-1,0),(1,0))

def best_path(x,y):
    global grid, loc_dict
    adjs=(loc_dict[x+dx,y+dy] for dx,dy in DXDY)
    return min(loc_dict[x,y],min(adjs)+(grid[x,y]%9 or 9))

def sweeping_xy(d):
    dr=range(d)
    for r in range(2*d):
        for x in range(r+1):
            y=r-x
            if x in dr and y in dr:
                yield x,y

with open('15.txt') as file:
    data = file.read()
grid = np.array([list(map(int,row)) for row in data.splitlines()])
loc_dict = defaultdict(lambda: float('inf'))
loc_dict[0,0]=0

if PART2:
    row=np.concatenate(tuple(grid+i for i in range(5)),axis=1)
    grid=np.concatenate(tuple(row+i for i in range(5)),axis=0)

TARGET=(len(grid[0])-1,len(grid)-1)

updates=True
iterations=0
sweep=tuple(sweeping_xy(len(grid)))
while updates:
    updates=False
    iterations+=1
    for x,y in sweep:
        new_best=best_path(x,y)
        if new_best<loc_dict[x,y]:
            loc_dict[x,y]=new_best
            updates=True
    print(end='.',flush=True)
print()
print(f'Part {1+int(PART2)}:',loc_dict[TARGET])
print(f'(Used {iterations} iterations to fully solve all spaces)')

### Visualise ###
rev_path=[TARGET]
next_xy=TARGET
while next_xy!=(0,0):
    c=rev_path[-1]
    x,y=c
    next_xy=min(((x+dx,y+dy) for dx,dy in DXDY if (x+dx,y+dy) not in rev_path),key=loc_dict.__getitem__)
    rev_path.append(next_xy)
if VISUALISE:
    path_set=set(rev_path)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            print(end=' #'[(x,y) in path_set])
        print()
