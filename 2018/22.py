#### INPUT ####
depth = 11991
target = 6,797
###############
## Example input
## Part 1: 114
## Part 2: 45
#depth=510
#target=10,10

NEITHER=0
TORCH=1
CLIMBING=2
ITEMS = ['neither','torch','climbing gear']

ROCKY=0
WET=1
CLIMBING=2


GEOLOGIC_CACHE={}
def geologic_index(x,y):
    if (x,y) in GEOLOGIC_CACHE:
        return GEOLOGIC_CACHE[x,y]
    if (x,y)==(0,0) or (x,y)==target:
        out = 0
    elif y==0:
        out = x*16807
    elif x==0:
        out = y*48271
    else:
        out = erosion_level(x-1,y)*erosion_level(x,y-1)
    GEOLOGIC_CACHE[x,y]=out
    return out

def erosion_level(x,y):
    return (geologic_index(x,y)+depth)%20183


tx,ty=target
risk_level=0
for y in range(ty+1):
    for x in range(tx+1):
        el=erosion_level(x,y)%3
        risk_level+=el
        print('.=|'[el],end='')
    print()
print(f'Part 1: {risk_level}',flush=True)

import heapq
class State:
    def __init__(s,x,y,eq,source,time):
        s.x=x
        s.y=y
        s.eq=eq
        s.sx,s.sy = source or (None,None)
        s.time=time
    def _prio(s):
        # Smallest time, then smallest abs distance
        return (s.time,abs(ty-s.y)+abs(tx-s.x))
    def __lt__(s,o):
        return s._prio()<o._prio()
    def __repr__(s):
        return f"<{s.x,s.y} @ t={s.time} from {s.sx,s.sy} with {ITEMS[s.eq]}>"
    def __iter__(s):
        yield s.x
        yield s.y
        yield s.eq
        yield None if s.x is s.y is None else (s.x,s.y)
        yield s.time

q=[]
visited=set()
heapq.heappush(q,State(0,0,TORCH,(-1,0),0))
mx,my=0,0
while q:
    x,y,equipped,source,time = heapq.heappop(q)
    mx,my=max(x,mx),max(y,my)
    if (x,y,equipped) in visited: continue # Don't revisit
    if len(visited)%10000==0: print(f'Queue @ {len(q)} items; max={mx,my}; (visited {len(visited)} loc/eq combos)')
    if (x,y)==target and equipped==TORCH:  # Final state
        print(f'Part 2: {time}')
        break
    if source is None:
        sx,sy=None,None
    else:
        sx,sy=source
        swap,={0,1,2}-{erosion_level(x,y)%3,equipped}
        heapq.heappush(q,State(x,y,swap,None,time+7))
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx,ny=x+dx,y+dy
        if nx<0 or ny<0: continue  # Solid rock
        if (nx,ny)==(sx,sy): continue  # Don't backtrack
        if erosion_level(nx,ny)%3==equipped: continue  # Wrong equipment
        heapq.heappush(q,State(nx,ny,equipped,(x,y),time+1))
    visited.add((x,y,equipped))  # Mark as done