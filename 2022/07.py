from pprint import pprint

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
            print(f"Adding {size} to p1")
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
                print("    "*depth+name)
                print_dirs(value,depth+1)
        else:
            print("    "*depth+f"{name} ({value})")


with open("07.txt") as file:
    lines = file.read().splitlines()
test_lines = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()
root = {"/":{}}
curr = root
for line in lines:
    units = line.split()
    if units[0]=='$':
        if units[1]=='cd':
            if '..' not in curr[units[2]]:
                curr[units[2]]['..']=curr # set parent
                print(f"Moved in to {units[2]}")
            curr=curr[units[2]]
    else:
        dir_or_size,name = units
        if dir_or_size == "dir":
            curr[name]={"..":curr} # set parent
        else:
            curr[name]=int(dir_or_size)
print_dirs(root)
pprint(root)
TOTAL_USED = dir_size(root['/'])
print(TOTAL_USED,"used")
print("Part 1:",p1) # Not 2712611
dir_size(root['/'])
print("Part 2:",p2)
