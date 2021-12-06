with open('06.txt') as file:
    data=file.read().split(',')
fish_init=list(map(int,data))

fish=fish_init
for day in range(80):
    new_fish=[]
    for i,f in enumerate(fish):
        if f==0:
            new_fish.append(6)
            new_fish.append(8)
        else:
            new_fish.append(f-1)
    fish=new_fish
print('Part 1:',len(fish),flush=True)

# Second approach - store the fish in a dict of the number of
# fish with each value - linear time rather than exponential

fish_counts={i:fish_init.count(i) for i in range(9)}
for day in range(256):
    new_counts={}
    for i in range(1,9): # Decrement all fish
        new_counts[i-1]=fish_counts[i]
    new_counts[8]=fish_counts[0] # Create new fish with time=8
    new_counts[6]+=fish_counts[0] # 'Decrement' 0 (+= not = for 7->6)
    fish_counts=new_counts
    # Check that the original approach for part 1 matches
    if day==79: print('Part 1:',sum(fish_counts.values()))
print('Part 2:',sum(fish_counts.values()))
