def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines
# Logic: sets can't contain duplicates - lists can.
# If the length is the same, no duplicates


lines = lines_from_file("04.txt")
print("Part 1:", sum([len(l.split()) == len(set(l.split())) for l in lines]))

t = 0
for l in lines:
    ws = l.split()
    s = [tuple(sorted(w)) for w in ws]
    if len(s) == len(set(s)):
        t += 1
print("Part 2:", t)
