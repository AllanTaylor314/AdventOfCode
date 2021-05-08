def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


ms = list(map(int, lines_from_file('01.txt')))
print("Part 1:", sum(m // 3 - 2 for m in ms))

fuel_for_fuel = 0
for m in ms:
    f = m
    module_fuel = 0
    while f // 3 - 2 > 0:
        f = f // 3 - 2
        module_fuel += f
    fuel_for_fuel += module_fuel
print("Part 2:", fuel_for_fuel)
