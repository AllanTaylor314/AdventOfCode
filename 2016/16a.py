DISK_LENGTH = 272


def gen_b(a):
    """Take a, reverse it, bitflip it, and prepend 0"""
    rev = a[::-1]
    return '0' + "".join([('1', '0')[int(c)] for c in rev])


def gen_checksum(a):
    """for each pair of bits, same = 1, diff = 0.
    If len(cs) is even, recurse, else return
    """
    cs = ""
    for i in range(0, len(a), 2):
        cs += ('1' if a[i] == a[i + 1] else '0')
    if len(cs) % 2 == 0:
        return gen_checksum(cs)
    else:
        return cs


a = '00111101111101000'  # Puzzle input
while len(a) < DISK_LENGTH:
    a += gen_b(a)

print(gen_checksum(a[:DISK_LENGTH]))
