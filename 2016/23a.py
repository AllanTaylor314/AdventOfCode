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
    if a in reg:
        return reg[a]
    else:
        return int(a)


lines = lines_from_file('23.txt')
cmds = [line.split() for line in lines]
i = 0
reg = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
while i < len(lines):
    #cmd = lines[i].split()
    cmd = cmds[i]
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
    elif cmd[0] == 'jnz':  # jmz
        if val(cmd[1]) != 0:
            i += val(cmd[2])
            i -= 1  # negate i+=1
    elif cmd[0] == 'tgl':
        index = i + val(cmd[1])
        if -1 < index < len(cmds):
            print(index, cmds[index])
            if cmds[index][0] == 'inc':
                cmds[index][0] = 'dec'
            elif len(cmds[index]) == 2:  # one arg
                cmds[index][0] = 'inc'
            elif cmds[index][0] == 'jnz':
                cmds[index][0] = 'cpy'
            else:
                cmds[index][0] = 'jnz'
    i += 1
print(reg)
