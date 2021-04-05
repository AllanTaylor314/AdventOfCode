def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    Don't worry about how.
    The file needs to exist :)
    Students should call this from their function to
    get the list lines from a file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


def val(a):
    if a.isnumeric():
        return int(a)
    else:
        return reg[a]


lines = lines_from_file('12.txt')
i = 0
reg = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
while i < len(lines):
    cmd = lines[i].split()
    if cmd[0] == 'cpy':
        reg[cmd[2]] = val(cmd[1])
        # if cmd[1].isnumeric:
        #    reg[cmd[2]] = int(cmd[1])
        # else:
        #    reg[cmd[2]] = reg[cmd[1]]
    elif cmd[0] == 'inc':
        reg[cmd[1]] += 1
    elif cmd[0] == 'dec':
        reg[cmd[1]] -= 1
    else:  # jmz
        if val(cmd[1]) != 0:
            i += int(cmd[2])
            i -= 1  # negate i+=1
    i += 1
print(reg)
