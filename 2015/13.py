from itertools import permutations

with open('13.txt') as file:
    data = file.read().replace("lose ","gain -").splitlines()

seating_dict = {}
for line in data:
    _ = line.split()
    name1 = _[0]
    points = int(_[3])
    name2 = _[-1][:-1]
    if name1 not in seating_dict:
        seating_dict[name1]={}
    seating_dict[name1][name2]=points

totals = []
for arrangement in permutations(seating_dict.keys()):
    total = 0
    for n1,n2 in zip(arrangement,arrangement[1:]+(arrangement[0],)):
        total+=seating_dict[n1][n2]+seating_dict[n2][n1]
    totals.append(total)

print('Part 1:',max(totals))


# Part 2 - same diff, but without the circle (i.e. a linear table)
totals = []
for arrangement in permutations(seating_dict.keys()):
    total = 0
    for n1,n2 in zip(arrangement,arrangement[1:]):
        total+=seating_dict[n1][n2]+seating_dict[n2][n1]
    totals.append(total)

print('Part 2:',max(totals))