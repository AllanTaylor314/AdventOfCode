from collections import deque, defaultdict

INF = float('inf')
SPRING = (500,0)

GRID = defaultdict(int)

EMPTY= 0
FLOW = 1
STILL= 2
CLAY = 3

DISPLAY_CHARS = '.|~#'

min_x=min_y=INF
max_x=max_y=-INF

def print_grid():
    for y in range(0,max_y+1):
        for x in range(min_x,max_x+1):
            print(end=DISPLAY_CHARS[GRID[(x,y)]])
        print()

with open('17.txt') as file:
    data = file.read().splitlines()

#data="""x=495, y=2..7
#y=7, x=495..501
#x=501, y=3..7
#x=498, y=2..4
#x=506, y=1..2
#x=498, y=10..13
#x=504, y=10..13
#y=13, x=498..504
#""".splitlines()

horiz = []
verts = []

for line in data:
    a_str,b_str = line.split(', ')
    a=int(a_str[2:])
    b0,b1=map(int,b_str[2:].split('..'))
    if a_str[0]=='x':
        horiz.append((a,(b0,b1)))
        min_x=min(min_x,a)
        max_x=max(max_x,a)
        min_y=min(min_y,b0)
        max_y=max(max_y,b1)
    else:
        verts.append(((b0,b1),a))
        min_y=min(min_y,a)
        max_y=max(max_y,a)
        min_x=min(min_x,b0)
        max_x=max(max_x,b1)

# Any x is valid
min_x-=1
max_x+=1

for x,(y0,y1) in horiz:
    for y in range(y0,y1+1):
        GRID[(x,y)]=CLAY
for (x0,x1),y in verts:
    for x in range(x0,x1+1):
        GRID[(x,y)]=CLAY

GRID[SPRING]=FLOW

q = deque([SPRING])
while q:
    x,y = q.popleft()
    if not (min_x<=x<=max_x and 0<=y<=max_y): continue
    below = GRID[(x,y+1)]
    if below == EMPTY:
        GRID[(x,y+1)] = FLOW
        q.append((x,y+1))
    elif below >= STILL:  # STILL or CLAY
        blocked=0
        for dx in [-1,1]: # Flow left and right
            if GRID[x+dx,y] == EMPTY:
                GRID[x+dx,y] = FLOW
                q.append((x+dx,y))
            else: # Can't flow that way
                blocked+=1
        if blocked==2:  # Something on both sides
            lx = rx = x
            while GRID[lx,y] == FLOW:
                lx-=1
            while GRID[rx,y] == FLOW:
                rx+=1
            if GRID[lx,y] == EMPTY or GRID[rx,y] == EMPTY:
                pass  # Not trapped, leave it
            else: # Trapped (still) water
                GRID[x,y] = STILL
                for dx in [-1,1]:
                    if GRID[x+dx,y] == FLOW:
                        q.append((x+dx,y))
                # Find the row above us
                if GRID[x,y-1]==FLOW:
                    q.append((x,y-1))

total=still=0
for y in range(min_y,max_y+1):
    for x in range(min_x,max_x+1):
        if GRID[x,y]%CLAY:
            total+=1
        if GRID[x,y]==STILL:
            still+=1
print('Part 1:',total)
print('Part 2:',still)

#Part 1: 31412
#Part 2: 25857
