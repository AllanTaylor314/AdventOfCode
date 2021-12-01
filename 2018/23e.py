"""Stolen from https://www.reddit.com/r/adventofcode/comments/a8s17l/comment/ecdqzdg/?utm_source=share&utm_medium=web2x&context=3
Shouldn't work but it does ¯\_(ツ)_/¯"""

import re

with open('23.txt') as file:
    data = file.read()

bots = [list(map(int, re.findall("-?\d+", line))) for line in data.splitlines()]
q = []
for x,y,z,r in bots:
    d = abs(x) + abs(y) + abs(z)
    q.append((max(0, d - r),1))
    q.append((d + r + 1,-1))
count = 0
maxCount = 0
result = 0
q.sort(reverse=True)
while q:
    dist,e = q.pop()
    count += e
    if count > maxCount:
        result = dist
        maxCount = count
print('Part 2:',result)