def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


lines = lines_from_file('02.txt')
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# for grid[a][b], U dec a, D inc a, L dec b, R inc b
a, b = 1, 1  # Start in middle
for line in lines:
    for c in line:
        if c == 'U':
            a = max(a - 1, 0)
        if c == 'D':
            a = min(a + 1, 2)
        if c == 'L':
            b = max(b - 1, 0)
        if c == 'R':
            b = min(b + 1, 2)
    print(grid[a][b], end="")
