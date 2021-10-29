import treelib
with open('06.txt') as file:
    data = file.read().splitlines()
orbits = {_[1]: _[0] for _ in [__.split(')') for __ in data]}

all_orbits = {}
for sat, bod in orbits.items():
    all_orbits[sat] = [bod]
    star = bod
    while star != 'COM':
        star = orbits[bod]
        all_orbits[sat].append(star)
        bod = star

print('Part 1:', sum([len(_) for _ in all_orbits.values()]))
# Part 1: 154386
san_orb = all_orbits['SAN']
you_orb = all_orbits['YOU']
common = set(san_orb) & set(you_orb)
steps = you_orb[:-len(common)] + san_orb[:len(common) - 1:-1]
print('Part 2:', len(steps))
# 344 too low
# 346
