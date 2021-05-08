import turtle


def min_steps(path):
    """The smallest number of hex steps to get to the lost child"""
    a = [abs(path.count('n') - path.count('s')),
         abs(path.count('ne') - path.count('sw')),
         abs(path.count('nw') - path.count('se')),
         ]
    # Of the three directions left, no two can be opposite, and the min can be cancelled
    return sum(a) - min(a)


with open('11.txt', encoding='utf-8') as file:
    path = file.read().replace('\n', '').split(',')

counts = {}
print('Steps each way')
for d in ['n', 'ne', 'se', 's', 'sw', 'nw']:
    counts[d] = path.count(d)
    print(f"{d:2}{counts[d]:10}")
print('Net steps')
for d1, d2 in [('n', 's'), ('ne', 'sw'), ('nw', 'se')]:
    print(f"{d1:2}{counts[d1]-counts[d2]:10}")

print('Part 1:', (counts['n'] - counts['s']) + (counts['nw'] - counts['se']))

best = 0
for i in range(1, len(path) + 1):
    curr = min_steps(path[:i])
    if curr > best:
        best = curr

print('Part 2:', best)


# Hey look, a lost turtle
ws = turtle.Screen()
geekyTurtle = turtle.Turtle()
geekyTurtle.speed(0)
turtle.tracer(0, 0)
headings = {'n': 90, 'ne': 30, 'se': -30, 's': -90, 'sw': -150, 'nw': 150}
for d in path:
    geekyTurtle.setheading(headings[d])
    geekyTurtle.forward(0.1)
turtle.update()
turtle.done()
# 697 is too high
# 628 is too low
# 644 is too high
# 636 is wrong
# 636 is wrong
# 640 is wrong
# 643 was right (s\n at end of file didn't count as s!)
