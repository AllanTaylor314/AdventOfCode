import hashlib


def gen_hash(nonce):
    global salt
    text = (salt + str(nonce))
    for _ in range(2017):
        text = str(hashlib.md5(text.encode()).hexdigest())
        # print(text)
    return text


def test_hash(hashed):
    for j in range(len(hashed) - 2):
        if hashed[j:j + 3] == (hashed[j] * 3):
            return hashed[j]


def test_hash5(hashed):
    for k in range(len(hashed) - 5):
        if hashed[k:k + 5] == (hashed[k] * 5):
            yield hashed[k]


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
                        print(potential_hash)
    i += 1
    #need_hashes = i>23000
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
