def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


unders = set()
overs = set()
tops = set()
tree = {}
weights = {}

lines = lines_from_file("07.txt")
for line in lines:
    tmp = line.split(' -> ')
    under = tmp[0].split()[0]
    unders.add(under)
    if len(tmp) == 2:
        tmp_over = tuple(tmp[1].split(", "))
        tree[under] = tmp_over
        for over in tmp_over:
            overs.add(over)
    else:
        tops.add(under)
    weight = int(tmp[0].split()[1][1:-1])
    weights[under] = weight
root, = unders - overs
print("Part 1:", root)
total_weights = {}

heights = {}
inv_tree = {}
for base, branches in tree.items():
    for branch in branches:
        inv_tree[branch] = base

for top in tops:
    total_weights[top] = weights[top]
# unders-=tops

while root not in total_weights:
    for base, branches in tree.items():
        if base not in total_weights and all([b in total_weights for b in branches]):
            total_weights[base] = weights[base] + \
                sum(total_weights[b] for b in branches)

for base, branches in tree.items():
    if len(set(total_weights[b] for b in branches)) != 1:
        print(base, '->')
        for branch in branches:
            print(
                f'  {branch} -> {total_weights[branch]} ({weights[branch]})')

# fabacam should be 299
