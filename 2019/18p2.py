from collections import deque
from itertools import chain
from time import perf_counter

PART2 = False

def sort_str(s):
    return "".join(sorted(set(s)))

def can_go(doors, keys):
    'Can go through the required doors with the current keys'
    return not (set(doors.lower())-set(keys))
t0 = perf_counter()
with open('18.txt') as file:
    data = file.read()
#data = """#########
#b.A.@.a#
#########"""
#data="""#############
#DcBa.#.GhKl#
#.###...#I###
#e#d#.@.#j#k#
###C#...###J#
#fEbA.#.FgHi#
#############"""

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

t1 = perf_counter()
print(f'Loaded in {t1-t0:.4f}s')
#########################################################################
def bfs_from(xy):
    # xy, doors, steps, prev
    q = deque([(xy,'',0,set())])
    outs = set()
    while q:
        xy,doors,step,prev = q.popleft()
        if xy in rev_keys:
            out = rev_keys[xy],step,doors
            if out not in outs:
                outs.add(out)
                yield out
        x,y=xy
        for nxy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if nxy in prev: continue  # Backsteps are pointless
            if nxy in passages or nxy in rev_doors:
                ndoors = sort_str(doors+rev_doors.get(nxy,''))
                q.append((nxy,ndoors,step+1,prev|{xy}))

step_reqs = {}
for key,loc in chain(enumerate(starts),keys.items()):
    for tar,steps,doors in bfs_from(loc):
        if key==tar:continue
        if (key,tar) not in step_reqs:
            step_reqs[key,tar] = steps,doors
        else:
            ps,pd = step_reqs[key,tar]
            assert steps>ps and doors==pd
t2 = perf_counter()
print(f'BFS in {t2-t1:.4f}s',flush=True)

#####################################################################################
# Every direct dependency
start_to_key_dependency = {}
sector_keys = ['']*len(starts)
for i,xy in enumerate(starts):
    for key in A2Z:
        if (i,key) in step_reqs:
            steps,doors=step_reqs[(i,key)]
            start_to_key_dependency[key]=doors
            sector_keys[i]+=key

# Every key that access to this key depends on (recursively)
def full_dependency(key):
    doors = start_to_key_dependency[key].lower()
    return sort_str(doors + ''.join(map(full_dependency,doors)))
full_dependencies = {_:full_dependency(_) for _ in A2Z}

# Every local key that this key depends on (directly or indirectly)
local_dependencies = [{s:sort_str(set(full_dependencies[s])&set(sector)) for s in sector} for sector in sector_keys]
full_local_dependency_dict = {}
for _ in local_dependencies: full_local_dependency_dict.update(_)


def validate_local_order(local_order):
    """Verifies that this order is """
    global full_local_dependency_dict
    for i,key in enumerate(local_order):
        # Any dependency that hasn't been met
        if set(full_local_dependency_dict[key])-set(local_order[:i]):
            return False
    return True

def path_len(start_index,path):
    total = 0
    curr = start_index
    for nex in path:
        total+=step_reqs[curr,nex][0]
        curr = nex
    return total

def sector_permutations(sector,used=''):
    if not sector: # Nothing more to permute
        yield used
        return
    for i,k in enumerate(sector):
        if not set(full_local_dependency_dict[k])-set(used): # Can go to k?
            yield from sector_permutations(sector[:i]+sector[i+1:],used+k)

t3 = perf_counter()
print(f'Generated dependencies in {t3-t2:.4f}s',flush=True)

total_steps = 0
total_paths = 0
for i,sector in enumerate(sector_keys):
    possible_steps = float('inf')
    for path in sector_permutations(sector):
        possible_steps = min(possible_steps,path_len(i,path))
        total_paths+=1
        if total_paths%50000==0:
            print(f"Tried {total_paths} paths... {path} ({path_len(i,path)}), best={possible_steps}",flush=True)
    total_steps+=possible_steps

t4 = perf_counter()
print(f"Part {1+PART2}: {total_steps} (Time: {t4-t0:.2f}s)")