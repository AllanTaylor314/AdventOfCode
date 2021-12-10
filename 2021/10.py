OC={
    "(":")",
    "[":"]",
    "{":"}",
    "<":">",
}
POINTS={
    ")":3,
    "]":57,
    "}":1197,
    ">":25137,
}
POINTS2={
    ")":1,
    "]":2,
    "}":3,
    ">":4,
}

with open('10.txt') as file:
    data = file.read()
points=0
scores=[]
for line in data.splitlines():
    stack=[]
    for i,c in enumerate(line):
        if c in OC:
            stack.append(c)
        else:
            if OC[stack.pop()] != c:
                points+=POINTS[c]
                break
    else:
        score=0
        while stack:
            score*=5
            score+=POINTS2[OC[stack.pop()]]
        scores.append(score)
scores.sort()

print('Part 1:',points)
print('Part 2:',scores[len(scores)//2])
