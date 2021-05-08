def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


lines = lines_from_file("05.txt")
mem = list(map(int, lines))
ptr = 0
steps = 0
while ptr in range(len(mem)):
    d = mem[ptr]
    mem[ptr] += 1
    ptr += d
    steps += 1
print('Part 1:', steps)

mem = list(map(int, lines))
ptr = 0
steps = 0
while ptr in range(len(mem)):
    d = mem[ptr]
    mem[ptr] += (1 if d < 3 else -1)
    ptr += d
    steps += 1
print('Part 2:', steps)
