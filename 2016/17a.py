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
while True:
    path = paths_to_test.pop(0)
    x, y = get_position(path)
    if x > 3 or y > 3:  # Path out of bounds
        continue
    if (x, y) == (3, 3):
        print(path)
        break
    paths_to_test += next_directions(path)
