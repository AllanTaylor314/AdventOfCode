from hashlib import md5
####### INPUT #######
PASSCODE = 'pslxynzg'
#####################

def gen_hash(path):
    return str(md5((PASSCODE + path).encode()).hexdigest())

def next_directions(path):
    return [path+door for door,char in zip('UDLR',gen_hash(path)) if char>'a']

def get_position(path):
    """(x,y)"""
    return path.count('D') - path.count('U'), path.count('R') - path.count('L')

paths_to_test = ['']
final_paths=[]
while paths_to_test:
    path = paths_to_test.pop(0)
    x, y = get_position(path)
    if not (0<=x<4 and 0<=y<4):  # Path out of bounds
        continue
    if (x, y) == (3, 3):
        final_paths.append(path)
    else:
        paths_to_test.extend(next_directions(path))
print('Part 1:',final_paths[0])
print('Part 2:',max(map(len,final_paths)))
