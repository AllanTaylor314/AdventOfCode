inp = "11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11".split()
banks = list(map(int, inp))
seen = set()
while tuple(banks) not in seen:
    seen.add(tuple(banks))
    full = max(banks)
    index = banks.index(full)
    banks[index] = 0
    for _ in range(full):
        banks[(index + _ + 1) % len(banks)] += 1
print("Part 1:", len(seen))

target = tuple(banks)
loop = 0
while tuple(banks) != target or loop == 0:
    full = max(banks)
    index = banks.index(full)
    banks[index] = 0
    for _ in range(full):
        banks[(index + _ + 1) % len(banks)] += 1
    loop += 1
print("Part 2:", loop)
