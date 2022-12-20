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

PART2 = False

with open("20.txt") as file:
    lines = file.read().splitlines()
nums = list(map(int,lines))
if PART2:nums = [n*811589153 for n in nums]
nodes = list(map(CLLNode,nums))

for a,b in zip(nodes,nodes[1:]+nodes[:1]):
    a.next=b
    b.prev=a

for _ in range(10 if PART2 else 1):
    for node in nodes:
        node.move()

curr = nodes[nums.index(0)]
answer = 0
for i in range(3):
    for _ in range(1000):
        curr=curr.next
    print(curr)
    answer+=curr.item
print(f"Part {1+PART2}:",answer)
