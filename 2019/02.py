def intcode(ri, n, v):
    ri[1], ri[2] = n, v
    for i in range(0, len(ri), 4):
        op, a, b, o = ri[i:i + 4]
        if op == 1:
            ri[o] = ri[a] + ri[b]
        elif op == 2:
            ri[o] = ri[a] * ri[b]
        elif op == 99:
            return ri[0]


with open("02.txt", encoding='utf-8') as file:
    raw_data = file.read()
ri = list(map(int, raw_data.split(',')))
print("Part 1:", intcode(ri[:], 12, 2))
for n in range(100):
    for v in range(100):
        o = intcode(ri[:], n, v)
        if o == 19690720:
            print("Part 2:", 100 * n + v)
            break
