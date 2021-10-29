import collections
inp = 125730, 579381 + 1


def valid(pw):
    pair = False
    pws = str(pw)
    for i in range(len(pws) - 1):
        if pws[i] == pws[i + 1]:
            pair = True
        if int(pws[i]) > int(pws[i + 1]):
            return False
    return pair


def valid2(pw):
    pws = str(pw)
    pwc = collections.Counter(pws)
    return 2 in pwc.values() and list(pws) == sorted(pws)


c = 0
b = 0
for i in range(*inp):
    c += valid(i)
    b += valid2(i)
print('Part 1:', c)
print('Part 2:', b)
