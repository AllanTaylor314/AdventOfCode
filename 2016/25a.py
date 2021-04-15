"""
This solution is specific to my input. It uses the fact that some
of the input code is designed to add two cells or multiply two cells.
These parts are skipped over, cutting time significantly.

Your input may vary
"""


def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


def val(a):
    """Takes a string. Returns an int value from reg or the input

    The Assembunny code takes inputs as plain ints or a reference
    to the register. This helper function returns the input value
    or the value from the register if the arg is a letter in abcd
    """
    global reg
    if a in reg:
        return reg[a]
    else:
        return int(a)


# a = 7 for part 1
reg = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
lines = lines_from_file('25.txt')
cmds = [line.split() for line in lines]
i = 0


def cpy(x, y):
    """copies x (either an integer or the value of a register) into register y."""
    global reg
    reg[y] = val(x)


def inc(a):
    """increases the value of register x by one"""
    global reg
    reg[a] += 1


def dec(a):
    """decreases the value of register x by one"""
    global reg
    reg[a] -= 1


def jnz(x, y):
    """jumps to an instruction y away (positive means forward;
    negative means backward), but only if x is not zero
    """
    global i
    if val(x) != 0:
        i += val(y)
        i -= 1  # counteract i += 1


def tgl(a):
    """toggles the instruction x away (pointing at instructions like jnz does:
    positive means forward; negative means backward)
    inc -> dec
    dec,tgl (1 arg) -> inc
    jnz -> cpy
    cpy (2 arg) -> jnz
    if intruction out of range, do nothing
    """
    global i, cmds
    index = i + val(cmds[i][1])
    if -1 < index < len(cmds):
        print(index, cmds[index], flush=True)
        if cmds[index][0] == 'inc':
            cmds[index][0] = 'dec'
        elif len(cmds[index]) == 2:  # one arg
            cmds[index][0] = 'inc'
        elif cmds[index][0] == 'jnz':
            cmds[index][0] = 'cpy'
        else:
            cmds[index][0] = 'jnz'
    else:
        print('tgl', index, flush=True)


def out(x):
    global output
    print(val(x), end="", flush=True)
    output += str(val(x))
    if val(x) not in {1, 0}:
        quit()


output = ""

# Create a dictionary of functions so that any function can be called
# without ifelifelif...
fun = {'cpy': cpy,
       'inc': inc,
       'dec': dec,
       'jnz': jnz,
       'tgl': tgl,
       'out': out,
       }

# Repeat until you reach the end of the instructions
while i < len(lines):
    # Shortcut - Multiplication
    if i == 3:
        print('Multiplication Shortcut for line', i)
        reg['a'] += reg['c'] * reg['d']
        reg['c'], reg['d'] = 0, 0
        i += 5
    # Shortcut - Addition
    elif i + 2 < len(cmds) and cmds[i + 2][0] == 'jnz' and cmds[i + 2][2] == '-2':
        print('Addition Shortcut for line', i)
        if (cmds[i][0] == 'inc' and cmds[i + 1][0] == 'dec'):
            x, y = cmds[i][1], cmds[i + 1][1]
            reg[x] += reg[y]
            reg[y] = 0
            i += 3
        elif (cmds[i][0] == 'dec' and cmds[i + 1][0] == 'inc'):
            y, x = cmds[i][1], cmds[i + 1][1]
            reg[x] += reg[y]
            reg[y] = 0
            i += 3
        else:
            print('^ False Postive ^')
            fun[cmds[i][0]](*cmds[i][1:])
            i += 1
    # Plain old following instructions :)
    else:
        fun[cmds[i][0]](*cmds[i][1:])
        #print(reg, " ".join(cmds[i]))
        i += 1

print('Register:', reg)
print('Answer:', reg['a'])
