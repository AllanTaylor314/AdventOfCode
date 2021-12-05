def irange(a,b):
    """Inclusive range (works with with 'backwards' ranges)"""
    if a<b:
        return range(a,b+1)
    return range(a,b-1,-1)

def diag_range(xy0,xy1):
    """Diagonal range (45 degree diagonal lines)"""
    x0,y0=xy0
    x1,y1=xy1
    dx=1 if x1-x0>0 else -1
    dy=1 if y1-y0>0 else -1
    x,y=x0,y0
    for _ in range(abs(x1-x0)):
        yield x,y
        x+=dx
        y+=dy
    yield x,y

with open('05.txt') as file:
    data=file.read().splitlines()

lines=[]
for line in data:
    a,b=line.split(' -> ')
    x0,y0=a.split(',')
    x1,y1=b.split(',')
    lines.append(((int(x0),int(y0)),(int(x1),int(y1))))

grid_lines = [((x0,y0),(x1,y1)) for (x0,y0),(x1,y1) in lines if x0==x1 or y0==y1]
diag_lines = [((x0,y0),(x1,y1)) for (x0,y0),(x1,y1) in lines if x0!=x1 and y0!=y1]
grid = {}
for ((x0,y0),(x1,y1)) in grid_lines:
    for x in irange(x0,x1):
        for y in irange(y0,y1):
            if (x,y) not in grid: grid[x,y]=0
            grid[x,y]+=1

overlaps=[(xy,c) for xy,c in grid.items() if c>=2]
print('Part 1:',len(overlaps))

for xy0,xy1 in diag_lines:
    for x,y in diag_range(xy0,xy1):
        if (x,y) not in grid: grid[x,y]=0
        grid[x,y]+=1

overlaps_p2=[(xy,c) for xy,c in grid.items() if c>=2]
print('Part 2:',len(overlaps_p2))
