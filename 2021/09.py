from queue import Queue
with open('09.txt') as file:
    data=file.read()

heatmap=[list(map(int,line)) for line in data.splitlines()]

max_x,max_y=len(heatmap[0]),len(heatmap)

def is_low(x,y):
    for ax,ay in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if 0<=ax<max_x and 0<=ay<max_y:
            if heatmap[ay][ax]<=heatmap[y][x]:
                return False
    return True

total=0
low_points=[]
for y in range(len(heatmap)):
    for x in range(len(heatmap[0])):
        if is_low(x,y):
            low_points.append((x,y))
            total+=heatmap[y][x]+1

print('Part 1:',total)

for y in range(len(heatmap)):
    for x in range(len(heatmap[0])):
        print('#' if heatmap[y][x]==9 else 'o' if (x,y) in low_points else ' ',end='')
    print()

class Basin:
    def __init__(self,low_xy):
        self.low_x,self.low_y=low_xy
        self.basin_contents={low_xy}
        self.walls=set()
    def solve(self):
        q=Queue()
        q.put((self.low_x,self.low_y))
        while not q.empty():
            #if len(self.basin_contents)>3:break
            x,y=q.get_nowait()
            for ax,ay in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=ax<max_x and 0<=ay<max_y:
                    if heatmap[ay][ax]!=9:
                        if (ax,ay) not in self.basin_contents|self.walls:
                            q.put((ax,ay))
                        self.basin_contents.add((ax,ay))
                    else:
                        self.walls.add((ax,ay))
    def size(self):
        return len(self.basin_contents)

basins=[]
for point in low_points:
    basin = Basin(point)
    basin.solve()
    basins.append(basin.size())
a,b,c=sorted(basins)[-3:]
print('Part 2:',a*b*c)