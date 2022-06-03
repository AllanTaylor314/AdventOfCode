from collections import defaultdict

class Stack:
    def __init__(self,iterable=()):
        self.root=None
        for i in iterable:
            self.push(i)
    def push(self,value):
        new=Node(value)
        new.next=self.root
        self.root=new
    def pop(self):
        if self.root is None: raise IndexError("Can't pop from empty stack")
        old = self.root
        self.root = old.next
        return old.value
    def __repr__(self):
        return f"Stack({self.root!r})"
class Node:
    def __init__(self,value):
        self.value = value
        self.next=None
    def __repr__(self):
        return f"<{self.value!r}> -> {self.next!r}"

N,E,W,S = 1j,1,-1,-1j # Use complex numbers for coordinates
news = dict(N=N,E=E,W=W,S=S) # and make them easy to get

inf=lambda:float('inf') # for defaultdict

with open('20.txt') as file:
    data = file.read()

# Shamelessly stolen from https://www.reddit.com/r/adventofcode/comments/a7uk3f/comment/ec5y3lm/
stack = Stack()
pos = {0}  # Start at zero
starts, ends = {0},set()
min_distance = defaultdict(inf,{0:0}) # Shortest path
for c in data:
    if c=='|': # or another path
        ends.update(pos) # include the new endpoints
        pos = starts # and go back to the most recent start
    elif c in news: # a boring old letter
        d = news[c]
        for p in pos: # update the shortest path to this point
            min_distance[p+d]=min(min_distance[p+d],min_distance[p]+1)
        pos = {p+d for p in pos} # and update the points
    elif c=='(':
        stack.push((starts,ends)) # store the current state
        starts, ends = pos, set() # and start branching
    elif c==')':
        pos.update(ends) # save the most recent ends
        starts, ends = stack.pop() # and recombine

print('Part 1:',max(min_distance.values())) # the largest shortest distance
print('Part 2:',sum(v>=1000 for v in min_distance.values())) # the kinda long shortest distances
