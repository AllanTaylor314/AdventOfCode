class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = self


def print_nodes(node):
    """Print all the nodes in the cycle"""
    n = node
    while n.next is not node:
        print(n.data, end=" -> ")
        n = n.next
    print(n.data)


s = 356

spinlock = [0]
i = 0
for y in range(1, 2018):
    #print(i, spinlock)
    i = (i + s) % len(spinlock) + 1
    spinlock.insert(i, y)
print('Part 1:', spinlock[spinlock.index(2017) + 1], flush=True)
# 808

node0 = Node(0)
node = node0
for y in range(1, 50000001):
    if y % 50000 == 0:
        print(f"{y / 500000:3.2f}%", flush=True)
    for _ in range(s):
        node = node.next
    new_node = Node(y)
    new_node.next = node.next
    node.next = new_node
    node = new_node
print("Part 2:", node0.next.data)
# 47465686
