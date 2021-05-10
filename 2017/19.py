def move(d, l):
    return l[0] + d[0], l[1] + d[1]
# letters: 'IZMONJCSUT'


with open('19.txt') as file:
    rows = file.read().splitlines()

maze = [list(row) for row in rows]
# (0,0), (0,1)
# (1,0), (1,1)
directions = {
    (1, 0): [(0, 1), (0, -1)],
    (-1, 0): [(0, 1), (0, -1)],
    (0, 1): [(1, 0), (-1, 0)],
    (0, -1): [(1, 0), (-1, 0)]
}
d = (1, 0)
l = (0, 99)  # (0, maze[0].index('|'))
s = 0
letters = ''
while len(letters) < 10:
    c = maze[l[0]][l[1]]
    if c.isalpha():
        letters += c
        print(letters)
    if c == " ":
        raise UserWarning
    if c == "+":
        for pd in directions[d]:
            if maze[l[0] + pd[0]][l[1] + pd[1]] in '-|':
                d = pd
    l = move(d, l)
    s += 1
print('Part 1:', letters)
print('Part 2:', s)
# ITSZCJNMUO
# 17420
