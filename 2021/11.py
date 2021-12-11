from copy import deepcopy

with open('11.txt') as file:
    data=file.read()

grid = [list(map(int,line)) for line in data.splitlines()]

flashes=0
ry=range(len(grid))
rx=range(len(grid[0]))
step=0
while True:
    print('step',step)
    print("\n".join("".join(map(str,line)) for line in grid))
    print()
    flashed=set()
    for y in ry:
        for x in rx:
            grid[y][x]+=1
    flashing=True
    while flashing:
        flashing=False
        for y in ry:
            for x in rx:
                if (x,y) not in flashed and grid[y][x]>9:
                    if step<100:
                        flashes+=1
                    flashing=True
                    flashed.add((x,y))
                    for dx in (-1,0,1):
                        for dy in (-1,0,1):
                            if (x+dx) in rx and (y+dy) in ry:
                                grid[y+dy][x+dx]+=1
    for y in ry:
        for x in rx:
            if grid[y][x]>9:
                assert (x,y) in flashed
                grid[y][x]=0
    step+=1
    if len(flashed)==100: break
print('Final step:',step)
print("\n".join("".join(map(str,line)) for line in grid))
print('Part 1:',flashes)
print('Part 2:',step)
