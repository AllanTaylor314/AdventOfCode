import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
data ,= lines
# data = "2333133121414131402"
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
file_system = []
for i,c in enumerate(data):
    n = int(c)
    fid = i//2
    if i%2: # gap
        file_system.extend((None for _ in range(n)))
    else:
        file_system.extend((fid for _ in range(n)))

left_ptr = 0
while True:
    while left_ptr < len(file_system) and file_system[left_ptr] is not None:
        left_ptr += 1
    if left_ptr >= len(file_system):
        break
    while file_system[-1] is None:
        file_system.pop()
    file_system[left_ptr] = file_system.pop()

p1 = sum(a*b for a,b in enumerate(file_system))
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
class DLLNode:
    def __init__(self, size, contents=None) -> None:
        self.next = None
        self.prev = None
        self.size = size
        self.contents = contents
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.size!r}, {self.contents!r})"
    def replace(self, new_node):
        assert new_node is not self
        new_node.next = self.next
        new_node.prev = self.prev
        self.next = None
        self.prev = None
        if new_node.next is not None:
            new_node.next.prev = new_node
        if new_node.prev is not None:
            new_node.prev.next = new_node
    def insert_before(self, new_node):
        assert new_node is not self
        new_node.next = self
        new_node.prev = self.prev
        self.prev = new_node
        if new_node.prev is not None:
            new_node.prev.next = new_node
    def merge_empty(self):
        right = left = self
        size = self.size
        while left.prev is not None and left.prev.contents is None:
            left = left.prev
            size += left.size
        while right.next is not None and right.next.contents is None:
            right = right.next
            size += right.size
        self.size = size
        self.prev = left and left.prev
        self.right = right and right.prev
        if self.prev is not None:
            self.prev.next = self
        if self.next is not None:
            self.next.prev = self
         
head = None
tail = None
block_nodes = []
for i,c in enumerate(data):
    n = int(c)
    fid = i//2
    if i%2: # gap
        new_node = DLLNode(n,None)
    else:
        new_node = DLLNode(n,fid)
        block_nodes.append(new_node)
    if n == 0:
        continue
    if head is None:
        head = tail = new_node
    else:
        tail.next = new_node
        new_node.prev = tail
        tail = new_node

def print_dll():
    curr = head
    while curr is not None:
        c = "." if curr.contents is None else str(curr.contents)
        print(" ".join(c*curr.size),end="|")
        curr = curr.next
    print()

for node in reversed(block_nodes):
    curr = head
    while curr.contents is not None or curr.size < node.size:
        if curr is None or curr is node:
            break
        curr = curr.next
        if curr is None or curr is node:
            break
    else:
        new_node = DLLNode(node.size,None)
        node.replace(new_node)
        assert curr.size >= node.size
        assert curr.contents is None
        curr.size -= node.size
        if curr.size == 0:
            curr.replace(node)
        else:
            curr.insert_before(node)
        curr.merge_empty()


p2 = 0
i = 0
curr = head
while curr is not None:
    for _ in range(curr.size):
        if curr.contents is not None:
            p2 += curr.contents * i
        i += 1
    curr = curr.next

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
