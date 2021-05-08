def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


def pos_at_t(depth, t):
    """Return the position at time=t. 0 is caught"""
    return t % (2 * (depth - 1))  # Only zero matters for now


lines = lines_from_file("13.txt")
scanners = {}
for line in lines:
    layer, depth = line.split(': ')
    scanners[int(layer)] = int(depth)

severity = 0
for ran, dep in scanners.items():
    print(f"t={ran}, d={dep}, pos={pos_at_t(dep, ran)}")
    if pos_at_t(dep, ran) == 0:
        severity += dep * ran

print('Part 1:', severity)
# 1098 too low
# 1504 was right


# Let's just brute force it!!!
i = 0
while True:
    i += 1
    if not i % 1000000:
        print('Testing', i)
    for ran, dep in scanners.items():
        if pos_at_t(dep, ran + i) == 0:
            break
    else:
        print('Part 2:', i)
        quit()
# less than 100000000
# 3823370 was right

