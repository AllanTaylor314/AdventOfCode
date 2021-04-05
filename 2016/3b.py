def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


def is_tri(vals):
    return (sum(vals) - (2 * max(vals))) > 0


lines = lines_from_file('3.txt')
next_lines = []
for line in lines:
    vals = [int(val) for val in line.split()]
    next_lines.append(vals)
lines = next_lines
new_lines = []
for i in range(0, len(lines), 3):
    for j in range(3):
        new_lines.append([lines[i][j], lines[i + 1][j], lines[i + 2][j]])
valid_triangles = 0
for line in new_lines:
    #vals = [int(val) for val in line.split()]
    valid_triangles += is_tri(line)
print(valid_triangles)
