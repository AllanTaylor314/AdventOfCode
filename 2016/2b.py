grid = [
    [None, None, 1, None, None, None],
    [None, 2, 3, 4, None, None],
    [5, 6, 7, 8, 9, None],
    [None, 'A', 'B', 'C', None, None],
    [None, None, 'D', None, None, None],
    [None, None, None, None, None, None],
]


def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


def is_valid_button(a, b):
    return not (grid[a][b] == None)


def new_coords(a, b, c):
    an, bn = a, b
    if c == 'U':
        an = a - 1
    if c == 'D':
        an = a + 1
    if c == 'L':
        bn = b - 1
    if c == 'R':
        bn = b + 1
    return ((an, bn) if is_valid_button(an, bn) else (a, b))


lines = lines_from_file('2.txt.')


# for grid[a][b], U dec a, D inc a, L dec b, R inc b
a, b = 2, 0  # Start in middle
for line in lines:
    for c in line:
        a, b = new_coords(a, b, c)
    print(grid[a][b], end="")
