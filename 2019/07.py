from itertools import permutations


def intcode(og_list, input_list):
    ri = og_list.copy()
    i = 0
    out = []
    while i < len(ri):
        op_par = ri[i]
        op = op_par % 100
        par = [0] * 10 + list(map(int, str(op_par // 100)))
        par.reverse()
        if op == 1:
            #print(ri[i:i + 4])
            ri[ri[i + 3]] = (ri[i + 1] if par[0] else ri[ri[i + 1]]) + \
                (ri[i + 2] if par[1] else ri[ri[i + 2]])
            i += 4
        elif op == 2:
            #print(ri[i:i + 4])
            ri[ri[i + 3]] = (ri[i + 1] if par[0] else ri[ri[i + 1]]) * \
                (ri[i + 2] if par[1] else ri[ri[i + 2]])
            i += 4
        elif op == 3:
            #print(ri[i:i + 2])
            # INPUT HERE:
            ri[ri[i + 1]] = input_list.pop(0)
            i += 2
        elif op == 4:
            #print(ri[i:i + 2])
            out.append(ri[ri[i + 1]])
            i += 2
        elif op == 5:
            if (ri[i + 1] if par[0] else ri[ri[i + 1]]):
                i = (ri[i + 2] if par[1] else ri[ri[i + 2]])
            else:
                i += 3
        elif op == 6:
            if (ri[i + 1] if par[0] else ri[ri[i + 1]]) == 0:
                i = (ri[i + 2] if par[1] else ri[ri[i + 2]])
            else:
                i += 3
        elif op == 7:
            ri[ri[i + 3]] = int((ri[i + 1] if par[0] else ri[ri[i + 1]])
                                < (ri[i + 2] if par[1] else ri[ri[i + 2]]))
            i += 4
        elif op == 8:
            ri[ri[i + 3]] = int((ri[i + 1] if par[0] else ri[ri[i + 1]])
                                == (ri[i + 2] if par[1] else ri[ri[i + 2]]))
            i += 4
        elif op == 99:
            # print('HALT')
            break
        else:
            print('?')
            i += 1
    return out


with open("07.txt") as file:
    raw_data = file.read()
ri = list(map(int, raw_data.split(',')))

amp_out = []
for a, b, c, d, e in permutations(range(5)):
    oa, = intcode(ri, [a, 0])
    ob, = intcode(ri, [b, oa])
    oc, = intcode(ri, [c, ob])
    od, = intcode(ri, [d, oc])
    oe, = intcode(ri, [e, od])
    amp_out.append(oe)

# print(amp_out)
print("Part 1:", max(amp_out))
# 70597
