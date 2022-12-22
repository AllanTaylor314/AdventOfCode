import re
L=-1j;R=1j
with open("22.txt") as file:
    raw_map,raw_instructions = file.read().split("\n\n")
if 0:
    raw_map,raw_instructions="""        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
""".split("\n\n")
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
            # print(f"Start for {x=}: {start}")
        if complex(x,y) not in on_map and complex(x,y-1) in on_map:
            portals[start,-1j]=complex(x,y-1)
            portals[complex(x,y),1j]=start+1j
            break
    # else:
    #     print(f"No portal on for {x=}")

for y in range(1,num_rows+1):
    for x in range(-1,num_cols+2):
        if complex(x,y) not in on_map and complex(x+1,y) in on_map:
            start = complex(x,y)
            # print(f"Start for {y=}: {start}")
        if complex(x,y) not in on_map and complex(x-1,y) in on_map:
            portals[start,-1]=complex(x-1,y)
            portals[complex(x,y),1]=start+1
            break
    # else:
    #     print(f"No portal on for {y=}")
d=1 # Right
p=min(empties,key=lambda z:(z.imag,z.real))
print(f"Starting at {p}")
for ins in instructions:
    if ins=='L':d*=L
    elif ins=='R':d*=R
    else:
        for _ in range(int(ins)):
            n=p+d
            if n not in on_map:
                print(end=f"Pop! from {n}")
                n=portals[n,d]
                print(f" to {n}")
            # n = portals.get(n,n)
            if n in walls:break
            assert n in empties
            p=n
            print(p)

print("Part 1:",int(1000*p.imag+4*p.real+(1,1j,-1,-1j).index(d)))
p2 = 0

print("Part 2:",p2)
