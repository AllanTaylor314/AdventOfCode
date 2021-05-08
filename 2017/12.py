def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


lines = lines_from_file("12.txt")
connections = {}
for line in lines:
    program, pipes = line.split(' <-> ')
    pipe_list = list(map(int, pipes.split(', ')))
    connections[int(program)] = pipe_list

all_nodes = set(connections.keys())
quorums = []
while all_nodes:
    to_check = [min(all_nodes)]
    quorum = set()
    while to_check:
        curr = to_check.pop(0)
        for c in connections[curr]:
            if c not in quorum:
                to_check.append(c)
                quorum.add(c)
    quorums.append(quorum)
    all_nodes -= quorum
print('Part 1:', len(quorums[0]))
print('Part 2:', len(quorums))
