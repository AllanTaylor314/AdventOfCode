#from queue import PriorityQueue
def manhattan_distance(a,b=None):
    if b is None: return sum(map(abs,a))
    d=0
    for j,k in zip(a,b):
        d+=abs(j-k)
    return d

with open('23.txt') as file:
    data = file.read()

bots=[]
for i,line in enumerate(data.splitlines()):
    x,y,z=map(int, line[5:line.index('>')].split(','))
    r=int(line.split()[1][2:])
    bots.append((x,y,z,r))

min_max_dists = []
for bot in bots:
    md = manhattan_distance(bot[:3])
    min_max_dists.append((md-bot[3],md+bot[3]))

mins,maxs=zip(*min_max_dists)
min_min=min(mins)
max_max=max(maxs)
counts={}
for mn,mx in min_max_dists:
    print(mn,mx,flush=True)
    for i in range(mn,mx+1):
        counts[i]=counts.get(i,0)