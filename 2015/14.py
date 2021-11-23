with open('14.txt') as file:
    data = file.read().splitlines()

reindeer = {}
for line in data:
    _=line.split()
    name = _[0]
    speed = int(_[3])
    duration = int(_[6])
    rest = int(_[13])
    reindeer[name]=(speed,duration,rest)

TIME = 2503

dist_dict = {n:0 for n in reindeer}
points = {n:0 for n in reindeer} # Part 2
for t in range(TIME):
    for n,(s,d,r) in reindeer.items():
        if t%(d+r)<d:
            dist_dict[n]+=s
    #---------- Part 2 ----------
    m = max(dist_dict.values())
    for n,d in dist_dict.items():
        if d==m:
            points[n]+=1
    #----------------------------

print('Part 1:', max(dist_dict.values()))
print('Part 2:', max(points.values()))