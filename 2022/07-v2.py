from pathlib import PurePosixPath as Path

with open("07.txt") as file:
    lines = file.read().splitlines()

dirs = {'/':0}
files = {}
current_path = Path('/')
for line in lines:
    units = line.split()
    if units[0]=='$':
        if units[1]=='cd':
            if units[2]=='..':
                current_path=current_path.parent
            else:
                current_path/=units[2]
    else:
        if units[0]=="dir":
            dirs[str(current_path/units[1])]=0
        else:
            files[str(current_path/units[1])] = int(units[0])

# Horrendous loop let's gooooo! 184*274
for d in dirs:
    for f in files:
        if f.startswith(d):
            dirs[d]+=files[f]
print("Part 1:",sum(s for s in dirs.values() if s<=100_000))
TOTAL_AVAILABLE = 70000000
MIN_UNUSED = 30000000
TOTAL_USED = dirs['/']
print("Part 2:",min(s for s in dirs.values() if (TOTAL_AVAILABLE-TOTAL_USED)+s>=MIN_UNUSED))
