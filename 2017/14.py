import numpy as np
from functools import reduce
LENGTH = 256  # For knot hash
key = 'xlqgujun'  # input


def knot(inp):
    """Applies the knot hash from day 10"""
    lens = list(map(ord, inp)) + [17, 31, 73, 47, 23]

    rope = np.arange(0, LENGTH)
    skip = 0
    s = 0
    for _ in range(64):
        for l in lens:
            e = s + l
            e += LENGTH * (s > e)
            rope[np.arange(s, e) %
                 LENGTH] = rope[np.arange(s, e) % LENGTH][::-1]
            s += l + skip
            skip += 1
            s %= LENGTH

    dense_nums = []
    for o in range(0, LENGTH, 16):
        dense_nums.append(reduce(int.__xor__, map(int, rope[o:o + 16])))
    return "".join(("0" + hex(n)[2:])[-2:] for n in dense_nums)


# Convert the knot hashes back to binary (including some leading zeros)
out = "\n".join(("0" * 128 + bin(int(knot(f"{key}-{n}"), 16))[2:])[-128:]
                for n in range(128))

# Print out the memory with # where in use
print(out.replace('0', ' ').replace('1', '#'))
print("Part 1:", out.count('1'))


mem = out.splitlines()
# Create a set of all the used spaces
used = {(x, y) for x in range(128)
        for y in range(128) if mem[x][y] == '1'}
groups = []
lone_groups = []
for x in range(128):
    for y in range(128):
        if (x, y) in used:
            new_group = {(x, y)}
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (x + dx, y + dy) in used:
                    new_group.add((x + dx, y + dy))
            if len(new_group) > 1:
                groups.append(new_group)
            else:
                lone_groups.append((x, y))

complete_groups = []
while len(groups):
    match = True
    new_set = groups.pop(0)
    while match:
        match = False
        for group in groups:
            if new_set & group:
                new_set |= group
                groups.remove(group)
                match = True
                break
    complete_groups.append(new_set)

print('Part 2:', len(complete_groups) + len(lone_groups))
