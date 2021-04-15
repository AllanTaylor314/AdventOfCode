def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


def next_positions(x, y):
    """Yields next posible locations to find route to, excluding walls"""
    global maze
    for r in [x - 1, x + 1]:
        if maze[r][y] != '#':
            yield (r, y)
    for c in [y - 1, y + 1]:
        if maze[x][c] != '#':
            yield (x, c)


def current_distance(x, y, loc_num):
    global distances_from_a_to_b
    adj = [distances_from_a_to_b[loc_num][_]
           for _ in next_positions(x, y) if _ in distances_from_a_to_b[loc_num]]
    if (x, y) in distances_from_a_to_b[loc_num]:
        adj.append(distances_from_a_to_b[loc_num][(x, y)] - 1)
    if len(adj) == 0:
        return 0
    return min(adj) + 1


# Create the map
maze = []
for line in lines_from_file('24.txt'):
    maze.append(list(line))

# print(maze)

places_of_interest = {}
for r in range(len(maze)):
    for c in range(len(maze[0])):
        if maze[r][c].isnumeric():
            places_of_interest[int(maze[r][c])] = (r, c)
print(places_of_interest)

distances_from_a_to_b = {}  # <start number 0-7>:(x,y) = dist from <start>
for loc_num, loc_coord in places_of_interest.items():
    distances_from_a_to_b.setdefault(loc_num, {})
    search_space = [loc_coord]
    searched_space = set()
    while len(search_space):
        x, y = search_space.pop(0)
        searched_space.add((x, y))
        distances_from_a_to_b[loc_num][(
            x, y)] = current_distance(x, y, loc_num)
        for loc in next_positions(x, y):
            if loc not in searched_space:
                search_space.append(loc)
