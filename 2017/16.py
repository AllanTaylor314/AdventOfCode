import time
with open('16.txt') as file:
    moves = file.read().split(',')

def s(d, i): return d[-i:] + d[:len(d) - i]


def x(d, a, b):
    d[int(a)], d[int(b)] = d[int(b)], d[int(a)]
    return d


def p(d, a, b):
    i, j = d.index(a), d.index(b)
    d[i], d[j] = b, a
    return d


compiled_moves = []
for move in moves:
    if move[0] == 's':
        i = int(move[1:])
        tmp = eval(f'lambda d: s(d,{i})')
    elif move[0] == 'x':
        a, b = move[1:].split('/')
        tmp = eval(f'lambda d: x(d,{a},{b})')
    elif move[0] == 'p':
        a, b = move[1:].split('/')
        tmp = eval(f'lambda d: p(d,"{a}","{b}")')

        #c, d = dancers.index(a), dancers.index(b)
        #dancers[c], dancers[d] = b, a
    compiled_moves.append(tmp)


def do_dance(dancers):
    for move in moves:
        if move[0] == 's':
            i = int(move[1:])
            dancers = dancers[-i:] + dancers[:len(dancers) - i]
        elif move[0] == 'x':
            a, b = move[1:].split('/')
            dancers[int(a)], dancers[int(
                b)] = dancers[int(b)], dancers[int(a)]
        elif move[0] == 'p':
            a, b = move[1:].split('/')
            c, d = dancers.index(a), dancers.index(b)
            dancers[c], dancers[d] = b, a
    return dancers


def do_dance_2(dancers):
    for move in compiled_moves:
        dancers = move(dancers)
    return dancers


init = "abcdefghijklmnop"

dancers = list(init)

out = "".join(do_dance(dancers))
print('Part 1:', out)

print(init)
print(out)
print()
dancers = list(init)

print(time.perf_counter())
for i in range(1000):
    dancers = do_dance(dancers)
print(time.perf_counter())

for i in range(1000):
    dancers = do_dance(dancers)
print(time.perf_counter())

quit()

# This doesn't account for instruction p
#dance = {}
# for i, c in enumerate(init):
#    dance[out.index(c)] = i
print('Just a moment... (each dot is 1000000 - 1000 dots)', flush=True)
# 999999999
arrangements = ["".join(dancers)]
init_reps = []
for i in range(1000000000):
    if not i % 100:
        print(end='.', flush=True)
    #dancers = [dancers[dance[_]] for _ in range(len(dancers))]
    dancers = do_dance_2(dancers[:])
    arrangements.append("".join(dancers))
    # print(arrangements[-1])
    if "".join(dancers) == init:
        print(i)
        init_reps.append(i)
        if len(init_reps) > 1:
            break

# out2 = "".join(dancers)
print('\nPart 2:', arrangements[1000000000 % (init_reps[-1] - init_reps[-2])
                                if len(init_reps) > 1 else -1])
# bfcdeghijklmnopa is wrong
# fgedchijklmnopab is wrong
