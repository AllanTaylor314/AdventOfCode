def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


lines = lines_from_file("02.txt")
maps = list(map(lambda b: list(map(int, b.split())), lines))
print("Part 1:", sum(max(a) - min(a) for a in maps))
t = 0
for r in maps:
    t += [n // m for n in r for m in r if n != m and n % m == 0][0]
print("Part 2:", t)
