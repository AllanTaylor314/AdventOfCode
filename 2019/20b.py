from collections import deque

class RecMazeSpace:
    _exisiting={}
    def __init__(self, xyz, source=None):
        global spaces
        global portals
        if xyz[:2] not in spaces: raise IndexError('Supplied coordinate is not a valid passage')
        self.x,self.y,self.depth=xyz
        x,y,d=xyz
        self.source=source
        next_locations_no_depth = {(x+1,y),(x-1,y),(x,y-1),(x,y+1)}&spaces
        next_locations = set()
        for loc in next_locations_no_depth:
            next_locations.add(loc+(d,))
        if (x,y) in portals:
            nx,ny,nd = portals[x,y]
            nd+=self.depth
            if nd>=0:  # Only go down
                next_locations.add((nx,ny,nd))
        next_locations-={source}
        self.next_locations=next_locations
        # Only keep the first source that got us here
        if xyz not in self._exisiting: self._exisiting[xyz]=self
    def __repr__(self):
        return f"RecMazeSpace(({self.x}, {self.y}, {self.depth}), {self.source}); Next: {self.next_locations}"


with open('20.txt') as file:
    data = file.read()

spaces = set()
alpha = set()
maze = {}
for y,row in enumerate(data.splitlines()):
    for x,c in enumerate(row):
        maze[x,y]=c
        if c==".":
            spaces.add((x,y))
        elif c.isalpha():
            alpha.add((x,y))
maze_size=x,y

spaces_with_portals = {}
portal_endpoints = {}
for x,y in alpha:
    if maze.get((x-1,y))=='.':
        space = x-1,y
        label = maze[x,y]+maze[x+1,y]
    elif maze.get((x+1,y))=='.':
        space = x+1,y
        label = maze[x-1,y]+maze[x,y]
    elif maze.get((x,y-1))=='.':
        space = x,y-1
        label = maze[x,y]+maze[x,y+1]
    elif maze.get((x,y+1))=='.':
        space = x,y+1
        label = maze[x,y-1]+maze[x,y]
    else:
        continue
    spaces_with_portals[space]=label
    if label not in portal_endpoints:
        portal_endpoints[label]=[]
    portal_endpoints[label].append(space)

portals = {}
for pair in portal_endpoints.values():
    if len(pair)==2:
        a,b=pair
        ax,ay=a
        if ax in range(4,maze_size[0]-4) and ay in range(4,maze_size[1]-4):
            ad = -1
        else: ad = 1
        bd=-ad  # Assumption
        portals[a]=b+(bd,)
        portals[b]=a+(ad,)

print('Begin the search',flush=True)
explore_queue = deque([(portal_endpoints['AA'][0]+(0,),None)])
final = portal_endpoints['ZZ'][0]+(0,)
i=0
while explore_queue:
    i+=1
    if i%100000==0:print('...',i,flush=True)
    xyz,source = explore_queue.popleft()
    if xyz in RecMazeSpace._exisiting: continue # This line saves about 25200000 checks!
    for next_xyz in RecMazeSpace(xyz,source).next_locations:
        explore_queue.append((next_xyz,xyz))
    if xyz==final:break

print('Begin the backtrack',flush=True)
source = RecMazeSpace._exisiting[final].source
steps = 0
while source is not None:
    steps+=1
    #print(source)
    source = RecMazeSpace._exisiting[source].source
print('Part 2:',steps)  # 5754
