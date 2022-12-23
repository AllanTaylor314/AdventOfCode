from collections import defaultdict
N=-1j;S=1j;W=-1;E=1

with open("23.txt") as file:
    lines = file.read().splitlines()
init_positions = set(complex(x,y) for y,row in enumerate(lines) for x,c in enumerate(row) if c=="#")
positions = set(init_positions)
proposals = [
    lambda elf:(elf+N,elf+N+E,elf+N+W), # N
    lambda elf:(elf+S,elf+S+E,elf+S+W), # S
    lambda elf:(elf+W,elf+N+W,elf+S+W), # W
    lambda elf:(elf+E,elf+N+E,elf+S+E)  # E
]
r=0
num_moved = -1
while num_moved:
    if r==10:
        minx=min(int(z.real) for z in positions)
        maxx=max(int(z.real) for z in positions)
        miny=min(int(z.imag) for z in positions)
        maxy=max(int(z.imag) for z in positions)
        p1 = (maxx-minx+1)*(maxy-miny+1)-len(positions)
        print("Part 1:",p1) # Not 5994, 6474, 4018
    num_moved=0
    new_positions = defaultdict(list)
    for elf in positions:
        if not {elf+E,elf+S+E,elf+S,elf+S+W,elf+W,elf+N+W,elf+N,elf+N+E}&positions: # All empty
            new_positions[elf].append(elf)
            continue
        for prop in proposals:
            if not set(prop(elf))&positions:
                new_positions[prop(elf)[0]].append(elf)
                break
        else:
            new_positions[elf].append(elf)
    old_positions = positions
    positions={(pro if len(elves)==1 else elf) for pro,elves in new_positions.items() for elf in elves}
    num_moved = len(old_positions-positions)
    assert len(positions)==len(init_positions) # Did we lose any elves?
    r+=1
    proposals.append(proposals.pop(0))

print("Part 2:",r)
