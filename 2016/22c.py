BLOCKS = "▁▂▃▄▅▆▇█"

def complex_range(n):
    for real in range(int(n.real)):
        for imag in range(int(n.imag)):
            yield real+imag*j

def display_complex_grid(grid_dict, display=str):
    last = max(grid_dict, key=abs)
    for row in range(int(last.imag)+1):
        for col in range(int(last.real)+1):
            print(end=display(grid_dict[row*1j+col]))
        print()

def us_to_block(us):
    use, siz = us
    return BLOCKS[int(use/siz*len(BLOCKS))]
def block(us):
    use, siz = us
    if siz>400: return BLOCKS[-1]
    if use==0: return ' '
    return '#'
def frac(us):
    use, siz = us
    #if use>200: return BLOCKS[-1]*8
    if use==0: return f" __/{siz:<3d}"
    return f"{use:>3d}/{siz:<3d}"

with open('22.txt') as file:
    data=file.read().splitlines()

cmd,headers,*lines=data

grid={}

uses=[]
avas=[]
sizs=[]

walls=set()

for line in lines:
    file,size,used,avail,use_pc=line.split()
    _,xs,ys=file.split('-')
    x=int(xs[1:])
    y=int(ys[1:])
    siz=int(size[:-1])
    use=int(used[:-1])
    ava=int(avail[:-1])
    assert use+ava==siz
    pos=x+y*1j
    grid[pos]=(use,siz)
    if use==0: hole=pos
    if siz>400:walls.add(pos)
    uses.append(use)
    avas.append(ava)
    sizs.append(siz)

smallest_nonzero = sorted(uses)[1]
largest_nonempty_space = sorted(avas)[-2]
assert largest_nonempty_space<smallest_nonzero

#display_complex_grid(grid,us_to_block)
display_complex_grid(grid,frac)
display_complex_grid(grid,block)
print('Hole:',hole)
print('Walls:',walls)

goal=max(grid, key=lambda _:(_.real, -_.imag))
left_wall = min(walls, key=abs)
steps_left = (hole-left_wall+1).real
steps_up = hole.imag
steps_right = goal.real-left_wall.real # Aiming just left of goal
goal_steps = goal.real # Goal needs to move left this many times
hole_steps_for_goal = 5*goal_steps-4 # 1 for the goal, 4 for the hole (except first step)

total = steps_left+steps_up+steps_right+hole_steps_for_goal
print('Part 2:', total)

####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
#███████████████████████████████████
################# ##################
####################################
####################################

# 248 too high