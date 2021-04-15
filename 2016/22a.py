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
    u, a = int(used[:-1]), int(avail[:-1])
    nodes[(x, y)] = (u, a)

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

print(pairs)
print(len(pairs))
