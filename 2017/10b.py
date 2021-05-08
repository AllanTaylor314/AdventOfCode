import numpy as np
from functools import reduce
LENGTH = 256

inp = '157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30'
lens = list(map(ord, inp)) + [17, 31, 73, 47, 23]

rope = np.arange(0, LENGTH)
skip = 0
s = 0
for _ in range(64):
    for l in lens:
        e = s + l
        e += LENGTH * (s > e)
        rope[np.arange(s, e) % LENGTH] = rope[np.arange(s, e) % LENGTH][::-1]
        s += l + skip
        skip += 1
        s %= LENGTH

dense_nums = []
for o in range(0, LENGTH, 16):
    dense_nums.append(reduce(int.__xor__, map(int, rope[o:o + 16])))
dense = "".join(("0" + hex(n)[2:])[-2:] for n in dense_nums)
print('Part 2:', dense)
