import re
L=-1j;R=1j
with open("22.txt") as file:
    raw_map,raw_instructions = file.read().split("\n\n")
instructions = re.findall(r"(\d+|R|L)",raw_instructions)
empties = set()
walls = set()
portals = {}
for y,row in enumerate(raw_map.splitlines(),1):
    for x,c in enumerate(row,1):
        if c=="#":
            walls.add(complex(x,y))
        elif c==".":
            empties.add(complex(x,y))
on_map = empties|walls
num_rows = max(int(z.imag) for z in on_map)
num_cols = max(int(z.real) for z in on_map)
for x in range(1,num_cols+1):
    for y in range(-1,num_rows+2):
        if complex(x,y) not in on_map and complex(x,y+1) in on_map:
            start = complex(x,y)
        if complex(x,y) not in on_map and complex(x,y-1) in on_map:
            portals[start,-1j]=complex(x,y-1)
            portals[complex(x,y),1j]=start+1j
            break

for y in range(1,num_rows+1):
    for x in range(-1,num_cols+2):
        if complex(x,y) not in on_map and complex(x+1,y) in on_map:
            start = complex(x,y)
        if complex(x,y) not in on_map and complex(x-1,y) in on_map:
            portals[start,-1]=complex(x-1,y)
            portals[complex(x,y),1]=start+1
            break
d=d0=1 # Right
p=p0=min(empties,key=lambda z:(z.imag,z.real))

for ins in instructions:
    if ins=='L':d*=L
    elif ins=='R':d*=R
    else:
        for _ in range(int(ins)):
            n=p+d
            if n not in on_map:
                n=portals[n,d]
            if n in walls:break
            assert n in empties
            p=n

print("Part 1:",int(1000*p.imag+4*p.real+(1,1j,-1,-1j).index(d)))

cube_portals = dict(( # Some of these are backwards!
    *(((complex( 50+i,  0  ),-1j),(complex(  1  ,150+i), 1 )) for i in range(1,51)), # A 2 1 ^
    *(((complex(  0  ,150+i),-1 ),(complex( 50+i,  1  ), 1j)) for i in range(1,51)), # B 1 4 <
    *(((complex(100+i,  0  ),-1j),(complex(    i,200  ),-1j)) for i in range(1,51)), # C 3 1 ^
    *(((complex(    i,201  ), 1j),(complex(100+i,  1  ), 1j)) for i in range(1,51)), # D 1 4 v
    *(((complex( 50  ,    i),-1 ),(complex(  1  ,151-i), 1 )) for i in range(1,51)), # E 2 1 < OP
    *(((complex(  0  ,100+i),-1 ),(complex( 51  , 51-i), 1 )) for i in range(1,51)), # F 1 3 < OP
    *(((complex( 50  , 50+i),-1 ),(complex(    i,101  ), 1j)) for i in range(1,51)), # G 2 2 <
    *(((complex(    i,100  ),-1j),(complex( 51  , 50+i), 1 )) for i in range(1,51)), # H 1 3 ^
    *(((complex(151  ,    i), 1 ),(complex(100  ,151-i),-1 )) for i in range(1,51)), # I 3 1 > OP
    *(((complex(101  ,100+i), 1 ),(complex(150  , 51-i),-1 )) for i in range(1,51)), # J 2 3 > OP
    *(((complex(100+i, 51  ), 1j),(complex(100  , 50+i),-1 )) for i in range(1,51)), # K 3 1 v
    *(((complex(101  , 50+i), 1 ),(complex(100+i, 50  ),-1j)) for i in range(1,51)), # L 2 2 >
    *(((complex( 50+i,151  ), 1j),(complex( 50  ,150+i),-1 )) for i in range(1,51)), # M 2 3 v
    *(((complex( 51  ,150+i), 1 ),(complex( 50+i,150  ),-1j)) for i in range(1,51)), # N 1 4 >
))
count=0
for (source,sd),(dest,dd) in cube_portals.items():
    if count%50==0:print(end=chr(ord('A')+count//50))
    assert source not in on_map
    assert source-sd in on_map
    assert source-50*sd in on_map
    assert dest in on_map
    assert dest+49*dd in on_map
    assert dest-dd not in on_map
    assert cube_portals[dest-dd,-dd]==(source-sd,-sd)
    count+=1
assert count==14*50
assert len(set(cube_portals.values()))==len(cube_portals)
print("\nAssertions passed")

d=d0
p=p0
for ins in instructions:
    if ins=='L':d*=L
    elif ins=='R':d*=R
    else:
        for _ in range(int(ins)):
            np=p+d
            nd=d
            if np not in on_map:
                np,nd=cube_portals[np,d]
                assert np-nd not in on_map
            if np in walls:break
            assert np in empties
            p=np
            d=nd
print("Part 2:",int(1000*p.imag+4*p.real+(1,1j,-1,-1j).index(d)))
