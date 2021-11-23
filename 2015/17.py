from itertools import combinations

with open('17.txt') as file:
    containers = list(map(int,file.readlines()))

count = 0
p2=True
for r in range(1,len(containers)+1):
    for c in combinations(containers,r):
        if sum(c)==150:
            if p2: p2=False;min_r=r
            count+=1
print('Part 1:',count)

min_count = 0
for c in combinations(containers,min_r):
    if sum(c)==150:
        min_count+=1
print('Part 2:',min_count)