DXDY=((0,-1),(0,1),(-1,0),(1,0))

class BestWeightToPoint:
    loc_dict={}
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.weight=float('inf')
        self.risk=r%9 or 9
        self.loc_dict[x,y]=self
    def __repr__(self):
        return f"<{self.x,self.y}: risk={self.risk}; weight={self.weight}>"
    def __lt__(self, other):
        return self.weight<other.weight
    def update_best_path(self):
        x,y=self.x,self.y
        adjs=(self.loc_dict[x+dx,y+dy] for dx,dy in DXDY if (x+dx,y+dy) in self.loc_dict)
        self.weight=min(self.weight,min(adjs).weight+self.risk)

with open('15.txt') as file:
    data = file.read()
grid = [list(map(int,row)) for row in data.splitlines()]


PART2=True
if PART2:
    import numpy as np
    ng=np.array(grid)
    row=np.concatenate(tuple(ng+i for i in range(5)),axis=1)
    grid=np.concatenate(tuple(row+i for i in range(5)),axis=0)

TARGET=(len(grid[0])-1,len(grid)-1)

q=[]
for x in range(len(grid[0])):
    for y in range(len(grid)):
        q.append(BestWeightToPoint(x,y,grid[y][x]))
q[0].weight=0  # Set 0,0 cost to 0
for _ in range(10):
    for p in q:
        p.update_best_path()
    print(p)

print(f'Part {1+int(PART2)}:',BestWeightToPoint.loc_dict[TARGET].weight)
