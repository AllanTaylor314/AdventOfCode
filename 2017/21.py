import numpy as np


def condense(arr):
    return "/".join("".join((".", "#")[n] for n in ar) for ar in arr)


def vaporise(s):
    return np.array([[int(c == "#") for c in l] for l in s.split('/')])


def arr_flip(arr):
    yield arr
    yield np.rot90(arr)
    yield np.rot90(np.rot90(arr))
    yield np.rot90(np.rot90(np.rot90(arr)))
    yield arr.T
    yield np.rot90(arr.T)
    yield np.rot90(np.rot90(arr.T))
    yield np.rot90(np.rot90(np.rot90(arr.T)))


def enhance(arr):
    global rulebook
    for ar in arr_flip(arr):
        c = condense(ar)
        if c in rulebook:
            return rulebook[c]
    raise IndexError


with open('21.txt') as file:
    rules = file.read().splitlines()
# rules = ['../.# => ##./#../...','.#./..#/### => #..#/..../..../#..#']
rulebook = {}
for rule in rules:
    i, o = rule.split(' => ')
    rulebook[i] = o

art = np.array([
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
])
for _ in range(18):
    # Just so you know that something is happening
    print(f"Iteration {_} (size: {art.size})")
    if _ == 5:
        print('Part 1:', sum(sum(art)))
    # Odd will be True
    if len(art) % 2:
        # Do three stuff
        la = len(art)
        # Work backwards to avoid need to account for recently added rows
        for i in range(la, 0, -3):
            art = np.insert(art, i, np.zeros(len(art)), axis=0)
            art = np.insert(art, i, np.zeros(len(art)), axis=1)
        la = len(art)
        for x in range(0, la, 4):
            for y in range(0, la, 4):
                tile = art[x:x + 3, y:y + 3]
                art[x:x + 4, y:y + 4] = vaporise(enhance(tile))
    else:
        # Do two stuff
        la = len(art)
        for i in range(la, 0, -2):
            art = np.insert(art, i, np.zeros(len(art)), axis=0)
            art = np.insert(art, i, np.zeros(len(art)), axis=1)
        la = len(art)
        for x in range(0, la, 3):
            for y in range(0, la, 3):
                tile = art[x:x + 2, y:y + 2]
                art[x:x + 3, y:y + 3] = vaporise(enhance(tile))

print('Part 2:', sum(sum(art)))
# 193 too low
# 441 too high
# 197 was right

# Part 2: 3081737
