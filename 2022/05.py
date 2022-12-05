with open("05.txt") as file:
    raw_stacks,raw_lines = file.read().split("\n\n")
    lines = raw_lines.splitlines()
instructions = []
stacks = [[] for _ in range(10)] # 0 is empty filler
for row in raw_stacks.splitlines()[-2::-1]:
    for i,c in enumerate(row[1::4],start=1):
        if c!=" ": stacks[i].append(c)
for line in lines:
    instructions.append(tuple(map(int,line.split()[1::2])))
stacks2 = [s.copy() for s in stacks]

for n,s,d in instructions:
    for _ in range(n):
        stacks[d].append(stacks[s].pop())
    
    stacks2[d].extend(stacks2[s][-n:])
    del stacks2[s][-n:]
p1 = [s[-1] for s in stacks[1:]]
print("Part 1: ",*p1,sep="")
p2 = [s[-1] for s in stacks2[1:]]
print("Part 2: ",*p2,sep="")
