from queue import Queue
A2Z="abcdefghijklmnopqrstuvwxyz"


def sort_str(s):
    return "".join(sorted(s))

with open('18.txt') as file:
    data = file.read()

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
rev_doors = {loc:d for d,loc in doors.items()}
rev_keys = {loc:k for k,loc in keys.items()}

visited = set()
queue = Queue()
queue.put(start+('',0))
while not queue.empty():
    xykd = queue.get_nowait()
    x,y,k,d = xykd
    xyk=x,y,k
    if xyk in visited:continue
    if (x,y) in rev_keys and rev_keys[x,y] not in k:
        k=sort_str(k+rev_keys[x,y])
    if k==A2Z:
        break
    for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
        if (nx,ny,k) in visited:
            pass
        elif (nx,ny) in passages:
            queue.put((nx,ny,k,d+1))
        elif (nx,ny) in rev_doors and rev_doors[nx,ny].lower() in k:
            queue.put((nx,ny,k,d+1))
    visited.add(xyk)
    if len(visited)%10000==0:
        print(f'Visited {len(visited)} places', flush=True)
print('Part 1:',d,flush=True)