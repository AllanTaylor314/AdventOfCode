def manhattan_distance(a,b=None):
    if b is None: return sum(map(abs,a))
    d=0
    for j,k in zip(a,b):
        d+=abs(j-k)
    return d

class Bot:
    def __init__(self,x,y,z,r):
        self.x=x
        self.y=y
        self.z=z
        self.r=r
        #self.vertices=[
            #(x+r,y,z),
            #(x-r,y,z),
            #(x,y+r,z),
            #(x,y-r,z),
            #(x,y,z+r),
            #(x,y,z-r),
        #]
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
        yield self.r
    def __repr__(self):
        return f"pos=<{self.x},{self.y},{self.z}>, r={self.r}"
    def overlap(self,other):
        o = other.x,other.y,other.z
        s = self.x,self.y,self.z
        return manhattan_distance(o,s)<=self.r+other.r
        #return any(s in other for s in self.vertices) or any(o is self for o in other.vertices)
    def __contains__(self,o):
        if isinstance(o,type(self)): o = o.x,o.y,o.z
        s=self.x,self.y,self.z
        return manhattan_distance(s,o)<=self.r

def count_bots(point):
    global bots
    c=0
    for bot in bots:
        if point in bot:
            c+=1
    return c

def count_nearby(point, stepsize=1, steps=10):
    px,py,pz=point
    limit = stepsize*steps
    c=0
    for x in range(px-limit, px+limit+1, stepsize):
        for y in range(px-limit, px+limit+1, stepsize):
            for z in range(px-limit, px+limit+1, stepsize):
                yield count_bots((x,y,z)),x,y,z

with open('23.txt') as file:
    data = file.read()

bots=[]
max_r=(0,-1)
for i,line in enumerate(data.splitlines()):
    x,y,z=map(int, line[5:line.index('>')].split(','))
    r=int(line.split()[1][2:])
    bots.append(Bot(x,y,z,r))
    max_r = max(max_r, (r,i))
max_bot = bots[max_r[1]]
sx,sy,sz,sr = max_bot
in_range = [(x,y,z,r) for x,y,z,r in bots if manhattan_distance((sx,sy,sz),(x,y,z))<=sr]
in_range2= [tuple(bot) for bot in bots if bot in max_bot]
print(f'{max_bot=}')
print('Part 1:',len(in_range),flush=True)
print('Part 1:',len(in_range2),'(using in_range2)')

######## Test ##########
test_bots = [
    Bot(0,0,0,5),
    Bot(5,0,0,1),
    Bot(6,0,0,1),
    Bot(1000,0,0,1),
    Bot(0,0,0,1000)
]
########################
#overlaps=set()
#overlap_dict={}
#for a,bot in enumerate(bots):
    #for b,obot in enumerate(bots):
        #if bot.overlap(obot):
            #assert obot.overlap(bot)
            #overlaps.add((a,b))
            #if a not in overlap_dict:
                #overlap_dict[a]=set()
            #overlap_dict[a].add(b)
#print(f'Found {len(overlaps)} overlaps')

#overlaps3=set()
#for a in range(len(bots)):
    #for b in range(len(bots)):
        #if (a,b) not in overlaps: continue
        #for c in range(len(bots)):
            #if (b,c) in overlaps and\
               #(c,a) in overlaps:
                #overlaps3.add((a,b,c))

#maybe_points=[]
#for bot in bots:
    #*xyz,r=bot
    #xyz=tuple(xyz)
    #maybe_points.extend(count_nearby(xyz,stepsize=r,steps=1))

#best_count=max(maybe_points)[0]
#best_points=[p for p in maybe_points if p[0]==best_count]
#more_probable_points=[]
#for c,x,y,z in best_points:
    #for p in count_nearby((x,y,z)):
        #if p[0]>=best_count:
            #more_probable_points.append(p)

from heapq import *
start=tuple(max_bot)[:3] #0,0,0
print(f'Starting at {start}')
heap = [(-count_bots(start),start)]
count_coordlist={}
best_pc=0
while heap:
    #print(best_pc,heap)
    pc,xyz=heappop(heap)
    if -pc>best_pc:
        print(f'New best count: {best_pc} => {-pc}',flush=True)
        best_pc=-pc
    if -pc not in count_coordlist:
        count_coordlist[-pc]=[]
    count_coordlist[-pc].append(xyz)
    for dx,dy,dz in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
        pos=x+dx,y+dy,z+dz
        heappush(heap,(-count_bots(pos),pos))