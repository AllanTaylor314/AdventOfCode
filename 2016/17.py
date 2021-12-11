import hashlib
PASSCODE = 'pslxynzg'


def gen_hash(path):
    return str(hashlib.md5((PASSCODE + str(path)).encode()).hexdigest())


def next_directions(path):
    chars = gen_hash(path)[:4]
    doors = 'UDLR'
    out = []
    for i in range(4):
        if chars[i] > 'a':
            out.append(path + doors[i])
    return out


def get_position(path):
    """(x,y)"""
    return path.count('D') - path.count('U'), path.count('R') - path.count('L')


paths_to_test = ['']
final_paths=[]
part1=True
while paths_to_test:
    path = paths_to_test.pop(0)
    x, y = get_position(path)
    if not (0<=x<4 and 0<=y<4):  # Path out of bounds
        continue
    if (x, y) == (3, 3):
        final_paths.append(path)
        if part1:
            print('Part 1:',path)
            part1=False
    else:
        paths_to_test.extend(next_directions(path))
print('Part 2:',max(map(len,final_paths)))
