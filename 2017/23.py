with open('23.txt') as file:
    lines = file.read().splitlines()

freq = 0
reg = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}
i = 0
mul_count = 0


def val(x):
    global reg
    try:
        return int(x)
    except ValueError:
        return reg.get(x, 0)


def set_(x, y):
    global reg
    reg[x] = val(y)
    # print(reg)


def sub(x, y):
    global reg
    reg[x] = val(x) - val(y)


def mul(x, y):
    global reg
    global mul_count
    mul_count += 1
    reg[x] = val(x) * val(y)


def jnz(x, y):
    global i
    if val(x) != 0:
        i += val(y)
        i -= 1  # Undo step to next


cmd = {
    "set": set_,
    "mul": mul,
    "jnz": jnz,
    "sub": sub,
}
while -1 < i < len(lines):
    c, *a = lines[i].split()
    # print(f"{i:2d}: {lines[i]}")
    cmd[c](*a)
    print(i, reg)
    i += 1
print('Part 1:', mul_count)
