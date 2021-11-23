with open('16.txt') as file:
    data = file.read().replace(':','').replace(',','').splitlines()

ticker = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

sues = {}
for line in data:
    _,sue,*info=line.split()
    sues[int(sue)] = {a:int(b) for a,b in zip(info[::2],info[1::2])}

for sue,info in sues.items():
    for item,count in ticker.items():
        if item in info and info[item]!=count:
            break
    else:
        print('Part 1:',sue)


comps = {}
for x in ['cats','trees']: comps[x]=int.__gt__
for x in ['pomeranians','goldfish']: comps[x]=int.__lt__

for sue,info in sues.items():
    for item,count in ticker.items():
        if item in info and not comps.get(item,int.__eq__)(info[item],count):
            break
    else:
        print('Part 2:',sue)