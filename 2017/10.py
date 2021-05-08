import numpy as np
LENGTH = 256

lens = [157, 222, 1, 2, 177, 254, 0, 228,
        159, 140, 249, 187, 255, 51, 76, 30]
#lens = [3, 4, 1, 5]
rope = np.arange(0, LENGTH)
skip = 0
s = 0
for l in lens:
    e = s + l
    e += LENGTH * (s > e)
    rope[np.arange(s, e) % LENGTH] = rope[np.arange(s, e) % LENGTH][::-1]
    s += l + skip
    skip += 1
    s %= LENGTH
print('Part 1:', rope[0] * rope[1])
