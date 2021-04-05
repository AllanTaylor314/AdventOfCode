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
valid_triangles = 0
for line in lines:
    vals = [int(val) for val in line.split()]
    valid_triangles += is_tri(vals)
print(valid_triangles)
