mem_address = 289326
"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

1,2,3,4,5,6,7,8,9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25, 26
0,1,2,1,2,1,2,1,2,  3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4,  5

Cycle increases one more than odd square
"""


def get_dist(n):
    """Finds the Manhattan Distance of the cell n from cell 1
    Relies on wizardry, magic, and chaos
    """
    sr = int(n**.5)
    sr -= sr % 2 == 0  # If square root is even, sub one
    os = sr**2
    perim = n - os
    if perim == 0:
        return sr - 1
    perim %= (sr + 1)
    return perim if (perim > sr // 2) else (1 + sr - perim)


print("Part 1:", get_dist(mem_address))


def adj_ids(n):
    """Only yield positions smaller than n"""
    if n > 1:
        yield n - 1  # Previous cell (if not the first cell)
    # yield n+1 # The next cell - not much use as will be empty


