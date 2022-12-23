from collections import defaultdict

def print_map(positions):
    minx=min(int(z.real) for z in positions)
    maxx=max(int(z.real) for z in positions)
    miny=min(int(z.imag) for z in positions)
    maxy=max(int(z.imag) for z in positions)
    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            print(end="#" if complex(x,y) in positions else ".")
        print()

with open("23.txt") as file:
    lines = file.read().splitlines()
init_positions = set(complex(x,y) for y,row in enumerate(lines) for x,c in enumerate(row) if c=="#")
positions = set(init_positions)
proposals = [
    lambda elf:(elf-1j,elf-1-1j,elf+1-1j), # N
    lambda elf:(elf+1j,elf-1+1j,elf+1+1j), # S
    lambda elf:(elf-1,elf-1-1j,elf-1+1j),  # W
    lambda elf:(elf+1,elf+1-1j,elf+1+1j)   # E
]
for r in range(10): # 10 rounds
    new_positions = defaultdict(list)
    for elf in positions:
        if not {elf+1,elf+1+1j,elf+1j,elf-1+1j,elf-1,elf-1-1j,elf-1j,elf+1-1j}&positions: # All empty
            new_positions[elf].append(elf)
            continue
        for prop in proposals:
            if not set(prop(elf))&positions:
                new_positions[prop(elf)[0]].append(elf)
                break
        else:
            new_positions[elf].append(elf)
    positions={(pro if len(elves)==1 else elf) for pro,elves in new_positions.items() for elf in elves}
    assert len(positions)==len(init_positions) # Did we lose any elves?
    print(r+1)
    print_map(positions)
    proposals.append(proposals.pop(0))

minx=min(int(z.real) for z in positions)
maxx=max(int(z.real) for z in positions)
miny=min(int(z.imag) for z in positions)
maxy=max(int(z.imag) for z in positions)
p1 = (maxx-minx+1)*(maxy-miny+1)-len(positions)
print("Part 1:",p1) # Not 5994, 6474, 4018
p2 = 0

print("Part 2:",p2)
