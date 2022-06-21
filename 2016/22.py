from copy import deepcopy
from queue import Queue
DXDY=((0,1),(0,-1),(1,0),(-1,0))
class State:
    def __init__(self,grid,step=0):
        self.grid=deepcopy(grid)
        self.tx,self.ty=len(grid[0])-1,0
        self.step=step
        self.prev=None
    def gen_next_states(self):
        if self.grid[self.ty][self.tx][1]>self.grid[0][0][0]:
            print(self.grid[self.ty][self.tx][1],'is too big')
            return
        for y,line in enumerate(grid):
            for x,(siz,use,ava) in enumerate(line):
                assert use+ava==siz
                for dx,dy in DXDY:
                    if 0<=x+dx<len(self.grid[0]) and 0<=y+dy<len(self.grid) and \
                       use<=self.grid[y+dy][x+dx][2]: # Used <= available
                        new=deepcopy(self)
                        new.prev=self
                        new.step+=1
                        asiz,ause,aava = new.grid[y][x]
                        bsiz,buse,bava = new.grid[y+dy][x+dx]
                        if buse+ause>bsiz: continue
                        new.grid[y][x] = (asiz,0,asiz)
                        new.grid[y+dy][x+dx] = (bsiz, buse+ause, bava-ause)
                        if (x,y)==(self.tx,self.ty):
                            new.tx+=dx
                            new.ty+=dy
                        yield new
    def __eq__(self, other):
        return type(self) is type(other) and self.grid==other.grid
    def __lt__(self, other):
        return self.tx+self.ty<other.tx+other.ty
    def __repr__(self):
        t=self.tx,self.ty
        op=' ('
        cp=' )'
        return f"Step: {self.step}\n"+\
                "\n".join("|".join(f"{op[int((x,y)==t)]}{node[1]:3d}/{node[0]:<3d}{cp[int((x,y)==t)]}"
                for x,node in enumerate(line))
                for y,line in enumerate(self.grid)).replace('  0','_ 0')
    def past_states(self):
        if self.prev is None:
            return repr(self)
        return self.prev.past_states()+'\n\n'+repr(self)

with open('22.txt') as file:
    data=file.read().splitlines()

#data="""a
#Filesystem            Size  Used  Avail  Use%
#/dev/grid/node-x0-y0   10T    8T     2T   80%
#/dev/grid/node-x0-y1   11T    6T     5T   54%
#/dev/grid/node-x0-y2   32T   28T     4T   87%
#/dev/grid/node-x1-y0    9T    7T     2T   77%
#/dev/grid/node-x1-y1    8T    0T     8T    0%
#/dev/grid/node-x1-y2   11T    7T     4T   63%
#/dev/grid/node-x2-y0   10T    6T     4T   60%
#/dev/grid/node-x2-y1    9T    8T     1T   88%
#/dev/grid/node-x2-y2    9T    6T     3T   66%
#""".splitlines()

cmd,headers,*lines=data

grid=[]
fs={}
for line in lines:
    file,size,used,avail,use_pc=line.split()
    _,xs,ys=file.split('-')
    x=int(xs[1:])
    y=int(ys[1:])
    siz=int(size[:-1])
    use=int(used[:-1])
    ava=int(avail[:-1])
    fs[x,y]=(siz,use,ava)

target=max(fs)
mx,my=target
for y in range(my+1):
    grid.append([])
    for x in range(mx+1):
        grid[-1].append(fs[x,y])

q=Queue()
q.put(State(grid))
while q.qsize():
    state=q.get()
    if state.tx==0==state.ty:
        print('Part 2:',state.step)
        break
    for new in state.gen_next_states():
        if new.tx==0==new.ty:
            print(new.past_states())
            print('Part 2:',new.step)
            q=Queue()
            break
        q.put(new)
        if q.qsize()%1000==0:
            print(q.qsize(), state.step, flush=True)