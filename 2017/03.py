from math import ceil, sqrt
###### INPUT #######
mem_address = 289326
####################
"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

1,2,3,4,5,6,7,8,9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25, 26
0,1,2,1,2,1,2,1,2,  3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4,  5

Cycle increases one more than odd square
"""

def get_dist(n):
    """Finds the Manhattan Distance of the cell n from cell 1
    Relies on wizardry, magic, and chaos
    """
    sr = int(n**.5)
    sr -= sr % 2 == 0  # If square root is even, sub one
    os = sr**2
    perim = n - os
    if perim == 0:
        return sr - 1
    perim %= (sr + 1)
    return perim if (perim > sr // 2) else (1 + sr - perim)

print("Part 1:", get_dist(mem_address), flush=True)

def n_to_xy(n):
    """Takes a value n and returns the x,y coordinates of that location
    Based on code from the following answer:
    https://math.stackexchange.com/a/163101/376570
    To be honest, I have no idea how this really works, but it does!
    """
    k=ceil((sqrt(n)-1)/2)
    t=2*k+1
    m=t**2 
    t=t-1
    if n>=m-t:
        return k-(m-n),-k
    else:
        m=m-t
    if n>=m-t:
        return -k,-k+(m-n)
    else:
        m=m-t
    if n>=m-t:
        return -k+(m-n),k
    else:
        return k,k-(m-n-t)


def adj_coord(x,y):
    """Generate a list of coordinates adjacent to the current one"""
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if not dx==0==dy:
                yield x+dx,y+dy


def n_to_inf(n=1):
    """Generate an infinite series of numbers, starting from n"""
    while True: yield n; n+=1


MEMORY={}
def read_mem(coord):
    return MEMORY.get(coord,0)
def write_mem(coord, val):
    MEMORY[coord]=val

### Test n_to_xy
coord_n = {}
for n in range(10):
    coord_n[n_to_xy(n)]=n
for y in range(-1,2):
    for x in range(-1,2):
        print(coord_n.get((x,y),'.'),end='')
    print()
###############

write_mem((0,0),1)
for n in n_to_inf(2):
    xy=n_to_xy(n)
    val=sum(read_mem(c) for c in adj_coord(*xy))
    if n%1000==0: print(f'{n=}, {val=}')
    write_mem(xy,val)
    if val>mem_address: break
print(f'Part 2: {val}')