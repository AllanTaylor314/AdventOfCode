with open('18.txt') as file:
    lines = file.read().splitlines()

freq = 0
reg = {}
i = 0


def val(x):
    global reg
    try:
        return int(x)
    except ValueError:
        return reg.get(x, 0)


def snd(x):
    global freq
    freq = val(x)
    print(freq)


def set_(x, y):
    global reg
    reg[x] = val(y)
    print(reg)


def add(x, y):
    global reg
    reg[x] = val(x) + val(y)


def mul(x, y):
    global reg
    reg[x] = val(x) * val(y)


def mod(x, y):
    global reg
    reg[x] = val(x) % val(y)


def rcv(x):
    global freq
    if val(x):
        print("Part 1", freq)
        quit()


def jgz(x, y):
    global i
    if val(x) > 0:
        i += val(y)
        i -= 1  # Undo step to next


cmd = {
    "snd": snd,
    "set": set_,
    "add": add,
    "mul": mul,
    "mod": mod,
    "rcv": rcv,
    "jgz": jgz,
}
while -1 < i < len(lines):
    c, *a = lines[i].split()
    # print(f"{i:2d}: {lines[i]}")
    cmd[c](*a)
    i += 1
