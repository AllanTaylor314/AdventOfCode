def lines_from_file(filename):
    """ Returns a list of lines from the given file. MODIFIED
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read().replace('dec ', 'inc -').replace('--', '')
        lines = raw_data.splitlines()
    return lines


reg = {}
high = 0


def compare(regkey, op, value):
    return eval(f"{reg.get(regkey,0)}{op}{value}")


lines = lines_from_file("08.txt")
for line in lines:
    regkey, _, delta, _, condreg, op, condval = line.split()
    if regkey not in reg:
        reg[regkey] = 0
    if compare(condreg, op, condval):
        reg[regkey] += int(delta)
        if reg[regkey] > high:
            high = reg[regkey]
print('Part 1:', max(reg.values()))
print('Part 2:', high)
