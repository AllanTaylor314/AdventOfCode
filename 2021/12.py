from queue import Queue

with open('12.txt') as file:
    data = file.read()

edges=[tuple(l.split('-')) for l in data.splitlines()]
nodes={}
for a,b in edges:
    if a not in nodes: nodes[a]=set()
    if b not in nodes: nodes[b]=set()
    nodes[a].add(b)
    nodes[b].add(a)
for nset in nodes.values():
    nset.discard('start')  # No backtrack - simplifies part 2

q=Queue()
q.put(['start'])
paths=[]
while q.qsize():
    path=q.get_nowait()
    current=path[-1]
    for next_node in nodes[current]:
        # Don't revisit small
        if next_node.islower() and next_node in path: continue
        if next_node == 'end':
            paths.append(path+['end'])
            continue
        q.put(path+[next_node])
print('Part 1:',len(paths))

q.put(['start'])
paths2=[]
while q.qsize():
    path=q.get_nowait()
    current=path[-1]
    for next_node in nodes[current]:
        # Don't revisit small, unless it is the first time
        if next_node.islower() and next_node in path:
            smalls = list(filter(str.islower, path))
            if len(smalls)!=len(set(smalls)):  # Already duplicate
                continue
        if next_node == 'end':
            paths2.append(path+['end'])
            continue
        q.put(path+[next_node])
print('Part 2:',len(paths2))
