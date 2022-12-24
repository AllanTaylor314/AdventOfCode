DELTAS = {1,-1,1j,-1j,0}
with open("24.txt") as file:
    lines = file.read().splitlines()
# lines="""#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""".splitlines()
blizzards = {"^":[],"v":[],"<":[],">":[],"#":[],".":[]}
for y,row in enumerate(lines):
    for x,c in enumerate(row):
        blizzards[c].append(complex(x,y))
start = min(blizzards["."],key=lambda z: z.imag)
final = max(blizzards["."],key=lambda z: z.imag)
size = max(blizzards["#"],key=abs) # Lower right corner (% and +1)
maxx = int(size.real-1)
maxy = int(size.imag-1)
def move_blizzards():
    for direction,delta in (("^",-1j),("v",1j),("<",-1),(">",1)):
        new_list = []
        for blizz in blizzards[direction]:
            blizz+=delta
            x,y=int(blizz.real),int(blizz.imag)
            if x==0:x=maxx
            if x>maxx:x=1
            if y==0:y=maxy
            if y>maxy:y=1
            new_list.append(complex(x,y))
        blizzards[direction]=new_list
del blizzards["."]
blizzards["#"].extend((start-1j,final+1j))
def print_blizzards():
    for y in range(maxy+2):
        for x in range(maxx+2):
            p = complex(x,y)
            bzs = []
            for d,vs in blizzards.items():
                if p in vs:bzs.append(d)
            print(end=bzs[0] if len(bzs)==1 else str(len(bzs) or "."))
        print()
time = 0
for repeat in range(3):
    current_positions = {start}
    while final not in current_positions:
        time+=1
        move_blizzards()
        full_places = {p for l in blizzards.values() for p in l}
        next_positions = set()
        for curr in current_positions:
            for delta in DELTAS:
                new = curr+delta
                if new not in full_places:
                    next_positions.add(new)
        current_positions = next_positions
        print(time,len(current_positions))
        # print_blizzards()
    if repeat==0:print("Part 1:",time)
    start,final=final,start
print("Part 2:",time) # Not 830
