with open('06.txt') as file:
    data=list(map(int,file.read().split(',')))
fish_counts=[data.count(i) for i in range(9)]
for day in range(256):
    fish_counts=fish_counts[1:]+fish_counts[:1]
    fish_counts[6]+=fish_counts[8]
    if day==79: print('Part 1:',sum(fish_counts))
print('Part 2:',sum(fish_counts))
