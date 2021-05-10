with open('18.txt') as file:
    lines = file.read().splitlines()

regs = [{"p": 0}, {"p": 1}]
ij = [0, 0]
queues = [[], []]
counter = 0
dl = [False, False]  # Is p in lock?


def val(p, x):
    global regs
    try:
        return int(x)
    except ValueError:
        return regs[p].get(x, 0)


def snd(p, x):
    global queues
    global counter
    queues[(p + 1) % 2].append(val(p, x))
    if p == 1:
        counter += 1


def set_(p, x, y):
    global regs
    regs[p][x] = val(p, y)


def add(p, x, y):
    global regs
    regs[p][x] = val(p, x) + val(p, y)


def mul(p, x, y):
    global regs
    regs[p][x] = val(p, x) * val(p, y)


def mod(p, x, y):
    global regs
    regs[p][x] = val(p, x) % val(p, y)


def rcv(p, x):
    global queues
    global regs
    global ij
    global dl
    if len(queues[p]):
        regs[p][x] = queues[p].pop(0)
        dl[p] = False
    else:
        ij[p] -= 1  # Stay here while waiting for queue
        dl[p] = True


def jgz(p, x, y):
    global ij
    if val(p, x) > 0:
        ij[p] += val(p, y)
        ij[p] -= 1  # Undo step to next


cmd = {
    "snd": snd,
    "set": set_,
    "add": add,
    "mul": mul,
    "mod": mod,
    "rcv": rcv,
    "jgz": jgz,
}
p = 0
rll = range(len(lines))
while not all(dl):
    p = (p + 1) % 2
    if (dl[p] and len(queues[p]) == 0) or ij[p] not in rll:
        continue
    if ij[0] not in rll and ij[1] not in rll:
        break
    c, *a = lines[ij[p]].split()
    cmd[c](p, *a)
    ij[p] += 1
print("Part 2:", counter)

# 15240 too high
# 7620 correct
