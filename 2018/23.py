def manhattan_distance(a,b=(0,0,0)):
    d=0
    for j,k in zip(a,b):
        d+=abs(j-k)
    return d
def sign(a):
    try: return a//abs(a)
    except ZeroDivisionError: return 1

with open('23.txt') as file:
    data = file.read()

bots=[]
max_r=(0,-1)
for i,line in enumerate(data.splitlines()):
    x,y,z=map(int, line[5:line.index('>')].split(','))
    r=int(line.split()[1][2:])
    bots.append((x,y,z,r))
    max_r = max(max_r, (r,i))
sx,sy,sz,sr = bots[max_r[1]]
in_range = [(x,y,z,r) for x,y,z,r in bots if manhattan_distance((sx,sy,sz),(x,y,z))<=sr]
print('Part 1:',len(in_range),flush=True)

#field_density={}
#for bx,by,bz,br in bots:
    #bxyz=bx,by,bz
    #for x in range(bx-br,bx+br+1):
        #for y in range(by-br+abs(bx-x),by+br+1-abs(bx-x)):
            #for z in range(bz-br+abs(bx-x)+abs(by-y),bz+br+1-abs(bx-x)-abs(by-y)):
                #if manhattan_distance(bxyz, (x,y,z))<=br:
                    #if (x,y,z) not in field_density:
                        #field_density[x,y,z]=0
                    #field_density[x,y,z]+=1
                #else:
                    #print('Fail')
    #print(len(field_density))

#field_density={}
#for bx,by,bz,br in bots:
    #bxyz=bx,by,bz
    #y,z=by,bz
    #for x in range(bx-br,bx+br+1):
        #if (x,y,z) not in field_density:
            #field_density[x,y,z]=0
        #field_density[x,y,z]+=1
    #print(len(field_density))

#max_other_range=(0,(0,0,0))
#for ax,ay,az,ar in bots:
    #c=0
    #d=0
    #axyz=ax,ay,az
    #for bx,by,bz,br in bots:
        #md=manhattan_distance(axyz,(bx,by,bz))
        #if md<=br:
            #c+=1
        #if md<=ar:
            #d+=1
    #print(f"{axyz} has {d} bots in range and is in range of {c} other bots")
    #max_other_range=max(max_other_range,(c,axyz))

i=0
x,y,z=0,0,0
field_strength={(0,0,0):0}
MUL=10000000
for bx,by,bz,br in bots:
    if manhattan_distance((0,0,0),(bx,by,bz))<=br:field_strength[0,0,0]+=1
def search(ox,oy,oz,r=10,m=1):
    global field_strength
    i,x,y,z=0,0,0,0
    while abs(x)<r:
        if   i==0: x+=sign(x)*m
        elif i==1: y+=sign(y)*m
        elif i==2: z+=sign(z)*m
        elif i==3: x*=-1
        elif i==4: y*=-1
        elif i==5: z*=-1
        i=(i+1)%6
        xyz=ox+x,oy+y,oz+z
        if xyz in field_strength: continue
        field_strength[xyz]=0
        for bx,by,bz,br in bots:
            if manhattan_distance(xyz,(bx,by,bz))<=br:field_strength[xyz]+=1
step_size = 10000000
search(0,0,0,250000000,step_size)
while step_size>1:
    #print(f'Searching using {step_size=}')
    step_size//=10
    max_strength = max(field_strength.values())
    #for xyz,v in list(field_strength.items()):
    for xyz,v in sorted(field_strength.items(),
                        key=(lambda xyzv:(-xyzv[1],manhattan_distance(xyzv[0])))):
        if v<max_strength:break
        md=manhattan_distance(xyz)
        print(f'Exploring {xyz} ({v=}) with {step_size=} [dist={md}]')
        search(*xyz,10*step_size,step_size)

max_strength = max(field_strength.values())
x,y,z=min((xyz for xyz,v in field_strength.items() if v==max_strength),
                    key=lambda xyz: manhattan_distance(xyz))
print(f'Part 2: {abs(x)+abs(y)+abs(z)} ({x},{y},{z})')
# 87815237 too low
# 93878016 too low