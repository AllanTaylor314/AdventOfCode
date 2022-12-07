from pprint import pprint

DEBUG = False

TOTAL_AVAILABLE = 70000000
MIN_UNUSED = 30000000
TOTAL_USED = 0
p1=0
p2=1e99

def dir_size(dirs):
    global p1,p2,TOTAL_USED
    if isinstance(dirs,dict):
        size = sum(dir_size(d) for n,d in dirs.items() if n!='..')
        if size<=100_000:
            if DEBUG: print(f"Adding {size} to p1")
            p1+=size
        if TOTAL_USED and (TOTAL_AVAILABLE-TOTAL_USED)+size>=MIN_UNUSED:
            p2 = min(p2,size)
    else:
        size = dirs # int
    return size
def print_dirs(dirs,depth=0):
    for name,value in dirs.items():
        if isinstance(value,dict):
            if name!='..':
                print("  "*depth+f"- {name} (dir)")
                print_dirs(value,depth+1)
        else:
            print("  "*depth+f"- {name} ({value})")


with open("07.txt") as file:
    lines = file.read().splitlines()

root = {"/":{}}
curr = root
for line in lines:
    units = line.split()
    if units[0]=='$':
        if units[1]=='cd':
            if '..' not in curr[units[2]]:
                curr[units[2]]['..']=curr # set parent
                if DEBUG: print(f"Moved in to {units[2]}")
            curr=curr[units[2]]
    else:
        dir_or_size,name = units
        if dir_or_size == "dir":
            curr[name]={"..":curr} # set parent
        else:
            curr[name]=int(dir_or_size)
print_dirs(root)
if DEBUG: pprint(root)
TOTAL_USED = dir_size(root['/'])
print(TOTAL_USED,"used")
print("Part 1:",p1)
dir_size(root['/']) # Rerun to set p2, now that TOTAL_USED it known
print("Part 2:",p2)
