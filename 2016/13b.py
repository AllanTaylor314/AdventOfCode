NUMBER = 1358
TARGET = (50, 50)  # Can't get any further in 50 steps


def is_open(x, y):
    """Number of 1s in binary is even means open"""
    if offices.get((x, y), 0) in ['X', ' ']:
        return False
    if offices.get((x, y), 0) in ['R', 'T']:
        return True
    if x < 0 or y < 0:
        return False
    num = x * x + 3 * x + 2 * x * y + y + y * y + NUMBER
    binary = "{0:b}".format(num)
    return binary.count('1') % 2 == 0


def num_adjacent_open(x, y):
    return (is_open(x + 1, y)
            + is_open(x - 1, y)
            + is_open(x, y + 1)
            + is_open(x, y - 1))


def close_deadend(x, y):
    global changed_dict
    if num_adjacent_open(x, y) < 2 and offices.get((x, y), 0) not in ['R', 'T', ' ']:
        offices[(x, y)] = ' '
        # print('Eliminated', (x, y))
        changed_dict = True


def close_deadends_to(mx, my):
    for x in range(mx):
        for y in range(my):
            close_deadend(x, y)


def enum_adj_spaces(x, y):
    if is_open(x + 1, y):
        yield (x + 1, y)
    if is_open(x - 1, y):
        yield (x - 1, y)
    if is_open(x, y + 1):
        yield (x, y + 1)
    if is_open(x, y - 1):
        yield (x, y - 1)
    # return


def adj_vals(x, y):
    out = []
    if (val := distances.get((x, y), None)) != None:
        out.append(val - 1)
    for t in enum_adj_spaces(x, y):
        if (val := distances.get(t, None)) != None:
            out.append(val)
    return out


offices = {}  # (x,y):<open/closed>
distances = {(1, 1): 0}  # (x,y):<dist from R>

# for x in range(TARGET[0] + 10):
# for y in range(TARGET[1] + 10):
# if (x, y) == TARGET:
# print('0')
# else:
# print('O' if is_open(x, y) else " ", end="")
# offices[(x, y)] = is_open(x, y)
# print()

# Fill out dictionary
for x in range(TARGET[0] + 10):
    for y in range(TARGET[1] + 10):
        offices[(x, y)] = ('#' if is_open(x, y) else " ")

# Set start and end points
offices[(1, 1)] = 'R'
#offices[TARGET] = 'T'

# Eliminate dead ends (can't solve loops)
# while changed_dict:
#    changed_dict = False
#    close_deadends_to(TARGET[0] + 10, TARGET[1] + 10)

# Print map
for x in range(TARGET[0] + 10):
    for y in range(TARGET[1] + 10):
        print(offices.get((x, y), " "), end="")
    print()
print()  # another line


next_places = [(1, 1)]
x, y = (1, 1)
while x < TARGET[0] and y < TARGET[1]:
    x, y = next_places.pop(0)
    for nx, ny in enum_adj_spaces(x, y):
        if (nx, ny) not in distances:
            next_places.append((nx, ny))
    distances[x, y] = min(adj_vals(x, y)) + 1
    # print(next_places)
    #print(f"({x}, {y}):{distances[x, y]}")

# for x in range(TARGET[0] + 10):
#    for y in range(TARGET[1] + 10):
#        print(offices.get((x, y), " "), end="")
#    print()
# print()  # another line

# print(distances)
count = 0
for key, dist in distances.items():
    if dist <= 50:
        #offices[key] = 'A'
        offices[key] = str(distances[key])[-1]
        count += 1

for x in range(TARGET[0] + 10):
    for y in range(TARGET[1] + 10):
        print(offices.get((x, y), " "), end="")
    print()
print()  # another line

print(count, 'rooms can be reached in up to 50 steps')
