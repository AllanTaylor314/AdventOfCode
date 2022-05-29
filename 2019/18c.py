from collections import defaultdict
import heapq

PART2 = False

def sort_str(s):
    return "".join(sorted(set(s)))

with open('18.txt') as file:
    data = file.read()
#data = """#########
#b.A.@.a#
#########"""


class State:
    STATE_DICT = {}
    def __init__(self,xys,keys,step):
        self.xys = xys
        self.keys = keys
        self.step = step
        lockey = (xys,keys)
        if lockey in self.STATE_DICT:
            raise ValueError('State already exists')
        self.STATE_DICT[lockey]=self
    def __lt__(self, elf):
        return self.step < elf.step
    def __le__(self, elf):
        return self.step <= elf.step
    def __repr__(self):
        return f"State({self.xys!r}, {self.keys!r}, {self.step!r})"
    def next_states(self):
        global passages
        global rev_doors
        global A2Z
        step = self.step+1
        if self.keys==A2Z:
            print(self)
            return
        for i,(x,y) in enumerate(self.xys):
            xys = list(self.xys)
            for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                nk = sort_str(self.keys+rev_keys.get((nx,ny),''))
                if ((nx,ny) in passages) or ((nx,ny) in rev_doors and rev_doors[nx,ny].lower() in nk):
                    xys[i]=(nx,ny)
                    new = self.create_or_update(tuple(xys),nk,step)
                    if new is not None: yield new
                    
    def create_or_update(self, xys, keys, step):
        lockey = (xys,keys)
        if lockey in self.STATE_DICT:
            state = self.STATE_DICT[lockey]
            state.step = min(state.step,step)
        else:
            return State(xys,keys,step)

maze = [list(_) for _ in data.splitlines()]

passages = set()
keys = {}
doors = {}
for y,row in enumerate(maze):
    for x,val in enumerate(row):
        if val.isalpha():
            if val.isupper():
                doors[val]=(x,y)
            else:
                keys[val]=(x,y)
                passages.add((x,y))
        elif val=='.':
            passages.add((x,y))
        elif val=='@':
            passages.add((x,y))
            start=(x,y)
A2Z = sort_str(keys)
rev_doors = {loc:d for d,loc in doors.items()}
rev_keys = {loc:k for k,loc in keys.items()}
if PART2:
    x,y=start
    starts = [(x+dx,y+dy) for dx in [-1,1] for dy in [-1,1]]
    for xy in [(x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        passages.remove(xy)
else:
    starts = [start]
##########################################################
pq = [State(tuple(starts),'',0)]
heapq.heapify(pq)
while pq:
    state = heapq.heappop(pq)
    pq.extend(state.next_states())
    heapq.heapify(pq)
    #print(pq)
    #input()
    if len(pq)%100==0:
        print(len(pq),state)
print(state)