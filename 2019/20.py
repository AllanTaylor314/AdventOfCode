from queue import Queue

class MazeSpace:
    _exisiting={}
    def __init__(self, xy, source=None):
        global spaces
        global portals
        if xy not in spaces: raise IndexError('Supplied coordinate is not a valid passage')
        self.x,self.y=xy
        x,y=xy
        self.source=source
        self.next_locations={(x+1,y),(x-1,y),(x,y-1),(x,y+1)}&spaces
        if xy in portals: self.next_locations.add(portals[xy])
        self.next_locations-={source}
        # Only keep the first source that got us here, otherwise we get loops
        if xy not in self._exisiting: self._exisiting[xy]=self
    def __repr__(self):
        return f"MazeSpace(({self.x}, {self.y}), {self.source}); Next: {self.next_locations}"


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
        portals[a]=b
        portals[b]=a


# BFS using a Queue - should find the shortest path to any point
explore_queue = Queue()
explore_queue.put((portal_endpoints['AA'][0],None))
final = portal_endpoints['ZZ'][0]
while not explore_queue.empty():
    xy,source = explore_queue.get_nowait()
    for next_xy in MazeSpace(xy,source).next_locations:
        explore_queue.put((next_xy,xy))
    if xy==final:break

source = MazeSpace._exisiting[final].source
steps = 0
while source is not None:
    steps+=1
    source = MazeSpace._exisiting[source].source
print('Part 1:',steps)