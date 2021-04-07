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
tried_paths = set()
max_len = 0
longest_path = ""
while len(paths_to_test):
    path = paths_to_test.pop(0)
    x, y = get_position(path)
    if x > 3 or y > 3:  # Path out of bounds
        continue
    if (x, y) == (3, 3):
        if len(path) > max_len:
            max_len = len(path)
            longest_path = path
            print(max_len, path)
            # print(path)
        continue
    if path not in tried_paths:
        paths_to_test += next_directions(path)
        tried_paths.add(path)

print(max_len)
