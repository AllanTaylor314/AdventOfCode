def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


password = list('abcdefgh')


def swap_pos(a, b):
    """swap position X with position Y"""
    password[a], password[b] = password[b], password[a]


def swap_letter(a, b):
    """swap letter X with letter Y"""
    ia=password.index(a)
    ib=password.index(b)
    password[ia], password[ib] = b, a


def rotate_steps(direction, steps):
    global password
    steps = steps % len(password)
    password = (password[steps:] + password[:steps]
                ) if direction == 'left' else (password[-steps:] + password[:-steps])


def rotate_pos(a):
    shift = password.index(a)
    shift += 1 + (1 if shift >= 4 else 0)
    rotate_steps('right', shift)


def reverse_pos(a, b):
    global password
    password = (password[:a] +
                password[b:a - 1 if a > 0 else None:-1] +
                password[b + 1:])


def move_pos(a, b):
    """move position X to position Y"""
    password.insert(b, password.pop(a))


lines = lines_from_file('21.txt')
"""
lines = ['swap position 4 with position 0',
         'swap letter d with letter b',
         'reverse positions 0 through 4',
         'rotate left 1 step',
         'move position 1 to position 4',
         'move position 3 to position 0',
         'rotate based on position of letter b',
         'rotate based on position of letter d']
password = list('abcde')
"""

for line in lines:
    cmds = line.split()
    if cmds[0] == 'swap':
        if cmds[1] == 'letter':
            swap_letter(cmds[2], cmds[-1])
        else:
            swap_pos(int(cmds[2]), int(cmds[-1]))
    elif cmds[0] == 'rotate':
        if cmds[1] == 'based':
            rotate_pos(cmds[-1])
        else:
            rotate_steps(cmds[1], int(cmds[2]))
    elif cmds[0] == 'reverse':
        reverse_pos(int(cmds[2]), int(cmds[-1]))
    elif cmds[0] == 'move':
        move_pos(int(cmds[2]), int(cmds[-1]))
    else:
        print(cmds[0], "not a valid command")
        quit()
    print("".join(password), line)
print("".join(password))
