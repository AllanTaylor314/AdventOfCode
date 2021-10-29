import turtle
crush = turtle.Turtle()
crush.pencolor('red')
angles = {'U': 90, 'L': 180, 'D': 270, 'R': 0}
with open('03.txt') as f:
    wire_a, wire_b = f.read().splitlines()
"""
y
^
|
L->x
"""
turtle.tracer(0, 0)
xy = [0, 0]
path_a = []
directions_a = wire_a.split(',')
for d in directions_a:
    dire, dist = d[0], int(d[1:])
    m = -1 if dire in 'DL' else 1
    i = dire in 'UD'
    crush.setheading(angles[dire])
    crush.forward(dist / 10)
    for _ in range(dist):
        xy[i] += m
        path_a.append(tuple(xy))
set_path_a = set(path_a)
crush.pencolor('blue')
crush.penup()
crush.setpos(0, 0)
crush.pendown()
xy = [0, 0]
path_b = []
directions_b = wire_b.split(',')
for d in directions_b:
    dire, dist = d[0], int(d[1:])
    m = -1 if dire in 'DL' else 1
    i = dire in 'UD'
    crush.setheading(angles[dire])
    crush.forward(dist / 10)
    for _ in range(dist):
        xy[i] += m
        path_b.append(tuple(xy))
        # if path_b[-1] in set_path_a:
        #    print('Part 1:', path_b[-1])
        #    break
set_path_b = set(path_b)
crosses = set_path_a & set_path_b
md_cross = [sum(map(abs, t)) for t in crosses]
turtle.update()
# 3334 too high
print('Part 1:', min(md_cross))
turtle.done()

combisteps = [path_a.index(c) + path_b.index(c) + 2 for c in crosses]
print('Part 1:', min(combisteps))
