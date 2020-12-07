
from collections import Counter
import operator
inpstr = open('6input.txt').read()

coords =  [tuple(map(int,l.split(','))) for l in inpstr.splitlines() ]

topedge= min(coords, key=operator.itemgetter(1))[1]
bottomedge = max(coords, key=operator.itemgetter(1))[1]
leftedge = min(coords, key=operator.itemgetter(0))[0]
rightedge = max(coords, key=operator.itemgetter(0))[0]

def isfinite(c):
    return leftedge < c[0] < rightedge and topedge < c[1] < bottomedge


def find_distance(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def single_min(it):
    s = sorted(it)
    return s[0] != s[1]

def argmin(it):
    min_ = min(it)
    return it.index(min_)


#Part1
count = Counter()

for i in range(leftedge, rightedge):
    for j in range(topedge, bottomedge):
        distances = [find_distance((i,j),c) for c in coords]


        if single_min(distances):
            count[coords[argmin(distances)]]+= 1

maxarea = 0
for c in coords:
    if isfinite(c):
        maxarea = max(maxarea,count[c])

print(maxarea)

#Part 2
count = 0
for i in range(leftedge, rightedge):
    for j in range(topedge, bottomedge):
        distances = [find_distance((i,j),c ) for c in coords]
        if sum(distances) < 10000:
            count+=1

print(count)
