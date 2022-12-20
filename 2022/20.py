class CLLNode:
    LEN=0
    def __init__(self,item):
        self.next=None
        self.prev=None
        self.item=item
        type(self).LEN+=1
    def __repr__(self):
        return f"<{self.item}>"
    def unlink(self):
        self.prev.next=self.next
        self.next.prev=self.prev
    def move(self):
        if self.item%(type(self).LEN-1)==0:return
        self.unlink()
        curr=self
        if self.item<0:
            for _ in range((-self.item)%(type(self).LEN-1)):
                curr=curr.prev
            self.next=curr
            self.prev=curr.prev
            self.prev.next=self
            curr.prev=self
        else:
            for _ in range(self.item%(type(self).LEN-1)):
                curr=curr.next
            self.prev=curr
            self.next=curr.next
            curr.next=self
            self.next.prev=self
        assert self.next.prev is self.prev.next is self
        assert self.next is not self is not self.prev

def print_cll(node):
    print(end=f"[{node!r}")
    curr = node.next
    while curr is not node:
        print(end=f", {curr!r}")
        curr = curr.next
    print("]")

with open("20.txt") as file:
    lines = file.read().splitlines()
nums = list(map(int,lines))
# nums = [1,2,-3,3,-2,0,4]
nums = [n*811589153 for n in nums]
nodes = list(map(CLLNode,nums))
for a,b in zip(nodes,nodes[1:]):
    a.next=b
    b.prev=a
nodes[0].prev=nodes[-1]
nodes[-1].next=nodes[0]
for _ in range(10):
    for node in nodes:
        # print(end=f"Moving {node}...")
        node.move()
        # print("Done")
for node in nodes:
    assert node.next.prev is node.prev.next is node, f"{node} is not quite right"
p1 = 0
curr = nodes[0]
c=0
while curr.item!=0:
    c+=1
    curr=curr.next
    if c>10000:
        exit()
print(curr)
for i in range(3):
    for _ in range(1000):
        curr=curr.next
    print(curr)
    p1+=curr.item
print("Part 2:",p1)
