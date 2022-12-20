class CLLNode:
    def __init__(self,item):
        self.next=None
        self.prev=None
        self.item=item
    def __repr__(self):
        return f"<{self.item}>"
    def unlink(self):
        self.prev.next=self.next
        self.next.prev=self.prev
    def move(self):
        if self.item==0:return
        self.unlink()
        curr=self
        if self.item<0:
            for _ in range(-self.item):
                curr=curr.prev
            self.next=curr
            self.prev=curr.prev
            self.prev.next=self
            curr.prev=self
        else:
            for _ in range(self.item):
                curr=curr.next
            self.prev=curr
            self.next=curr.next
            curr.next=self
            self.next.prev=self
        assert self.next.prev is self.prev.next is self
        assert self.next is not self is not self.prev
        


with open("20.txt") as file:
    lines = file.read().splitlines()
nums = list(map(int,lines))
nodes = list(map(CLLNode,nums))
for a,b in zip(nodes,nodes[1:]):
    a.next=b
    b.prev=a
nodes[0].prev=nodes[-1]
nodes[-1].next=nodes[0]
for node in nodes:
    print(end=f"Moving {node}...")
    node.move()
    print("Done")
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
print("Part 1:",p1)
p2 = 0

print("Part 2:",p2)
