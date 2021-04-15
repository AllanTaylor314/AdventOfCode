# THIS IS NOT A COMPLETE SOLUTION. IT DOES NOT FIND ANY VIABLE PATHS
def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


lines = lines_from_file('22.txt')[2:]
nodes = {}  # (x,y):(used, available)
for line in lines:
    path, size, used, avail, use_percent = line.split()
    _, x_str, y_str = path.split('-')
    x, y = int(x_str[1:]), int(y_str[1:])
    u, a, s = int(used[:-1]), int(avail[:-1]), int(size[:-1])
    nodes[(x, y)] = (u, a, s)

grid_size = (max([xy[0] for xy in nodes.keys()]) + 1,
             max([xy[1] for xy in nodes.keys()]) + 1)
target = (grid_size[0] - 1, 0)
# print(nodes)
pairs = []
for a_xy, a_ua in nodes.items():
    # Node A is not empty (its Used is not zero).
    if a_ua[0] == 0:
        continue
    for b_xy, b_ua in nodes.items():
        # Nodes A and B are not the same node.
        if a_xy == b_xy:
            continue
        # The data on node A (its Used) would fit on node B (its Avail).
        if a_ua[0] <= b_ua[1]:
            pairs.append((a_xy, b_xy))

# print(pairs)
# print(len(pairs))
viable_pairs = []  # for moving data from A to B
for a_xy, b_xy in pairs:
    diff_x, diff_y = a_xy[0] - b_xy[0], a_xy[1] - b_xy[1]
    if (diff_x in {-1, 1} and diff_y == 0) or (diff_y in {-1, 1} and diff_x == 0):
        viable_pairs.append((a_xy, b_xy))
print(viable_pairs)

for x in range(grid_size[0]):
    for y in range(grid_size[1]):
        print(f"{nodes[(x,y)][0]:4}/{nodes[(x,y)][2]:<3}", end="")
    print()
