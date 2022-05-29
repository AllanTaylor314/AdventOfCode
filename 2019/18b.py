from collections import deque
PART2 = False
DEBUG = True

def sort_str(s):
    return "".join(sorted(s))

with open('18.txt') as file:
    data = file.read()

if DEBUG:
    data="""#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba...BcIJ#
#####.@.#####
#nK.L...G...#
#M###N#H###.#
#o#m..#i#jk.#
#############"""
    data = """#########
#b.A.@.a#
#########"""

#data="""#########
##b.A.@.a#
##########""";A2Z="ab"

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

# (((x,y),...),keys,step)
visited = set()
queue = deque()
init_state = (tuple(starts),'',0)
queue.append(init_state)
kandidates = []
while queue:
    xykd = queue.pop()
    xys,k,d = xykd
    if (xys,k) in visited:continue
    for i,(x,y) in enumerate(xys):
        xysl = list(xys)
        nk=k # Copy it so loop doesn't break stuff
        if (x,y) in rev_keys and rev_keys[x,y] not in nk:
            if DEBUG: print(f'{i} collected {rev_keys[x,y]}')
            nk=sort_str(nk+rev_keys[x,y])
        if nk==A2Z:
            kandidates.append(d)
            print('Maybe',d)
            continue
        for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if (nx,ny,nk) in visited:
                pass
            elif ((nx,ny) in passages) or ((nx,ny) in rev_doors and rev_doors[nx,ny].lower() in nk):
                xysl[i]=(nx,ny)
                state = tuple(xysl),nk
                if state not in visited:
                    queue.append(state+(d+1,))
    visited.add((xys,k))
    if len(visited)%10000==0:
        print(f'Visited {len(visited)} places', flush=True)
print(f'Part {1+PART2}:',min(kandidates),flush=True)

#P2: 1887 too high