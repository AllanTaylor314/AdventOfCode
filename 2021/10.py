class StackNode:
    def __init__(self,value):
        self.value=value
        self.next_node=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self,value):
        node=StackNode(value)
        node.next_node=self.head
        self.head=node
    def pop(self):
        node=self.head
        self.head=node.next_node
        return node.value
    def peek(self):
        return self.head.value
    def empty(self):
        return self.head is None

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
    stack=Stack()
    for i,c in enumerate(line):
        if c in OC:
            stack.push(c)
        else:
            if (top:=OC[stack.peek()]) != c:
                print(f'Expected {top}, got {c}')
                points+=POINTS[c]
                break
            stack.pop()
    else:
        score=0
        while not stack.empty():
            score*=5
            score+=POINTS2[OC[stack.pop()]]
        scores.append(score)
scores.sort()

print('Part 1:',points)
print('Part 2:',scores[len(scores)//2])