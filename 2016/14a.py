import hashlib


def gen_hash(nonce):
    global salt
    return str(hashlib.md5((salt + str(nonce)).encode()).hexdigest())


def test_hash(hashed):
    for i in range(len(hashed) - 2):  # had -3 here instead of -2, deleting ...aaa
        if hashed[i:i + 3] == (hashed[i] * 3):
            return hashed[i]


def test_hash5(hashed):
    for i in range(len(hashed) - 5):
        if hashed[i:i + 5] == (hashed[i] * 5):
            yield hashed[i]


salt = 'ngcjuoqr'
#salt = 'abc'
potential_hashes = {}
needed_fives = {}
confirmed_hashes = {}
confirmed_by = {}
need_hashes = True
upper_bound = None
i = 0
while need_hashes == True:
    hashed = gen_hash(i)
    if repeat3 := test_hash(hashed):
        potential_hashes[i] = hashed
        needed_fives[repeat3] = needed_fives.get(repeat3, []) + [i]
        for repeat5 in test_hash5(hashed):
            if repeat5 in needed_fives:
                for hash_id in needed_fives[repeat5]:
                    potential_hash = potential_hashes[hash_id]
                    if 0 < (i - hash_id) < 1001:
                        confirmed_hashes[hash_id] = potential_hash
                        confirmed_by[hash_id] = (i, hashed)
    i += 1

    if len(confirmed_hashes) > 64:
        upper_bound = upper_bound or (sorted(confirmed_by.keys())[-1] + 1500)
    if upper_bound and i > upper_bound:
        need_hashes = False
# print(confirmed_hashes)
n = 0
keys = list(confirmed_hashes.keys())
keys.sort()
for key in keys:
    n += 1
    cb = confirmed_by.get(key, ('', ''))
    print(
        f"{n:2}{key:6}  {confirmed_hashes[key]}{cb[0]:6} {cb[1]}")
print(keys[63])
