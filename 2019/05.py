INPUT = 1  # Part 1
INPUT = 5  # Part 2

with open("05.txt") as file:
    raw_data = file.read()
#raw_data = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
ri = list(map(int, raw_data.split(',')))
i = 0
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
        ri[ri[i + 1]] = INPUT
        i += 2
    elif op == 4:
        #print(ri[i:i + 2])
        print(ri[ri[i + 1]])
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
        print('HALT')
        break
    else:
        i += 1

# 663 too low
# 4759 too low
# Part 1: 4887191 was right

# Part 2: 3419022
