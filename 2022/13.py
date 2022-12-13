class PacketWrapper:
    def __init__(self,packet):
        self._packet = packet
    def __lt__(self,other):
        return is_in_order(self._packet,other._packet)
    def __gt__(self,other):
        return not is_in_order(self._packet,other._packet)
    def __eq__(self,other):
        return self._packet == other
    def __repr__(self) -> str:
        return "<"+repr(self._packet)+">"

def is_in_order(left,right):
    if isinstance(left,int) and isinstance(right,int):
        if left == right:
            return None
        return left < right
    if isinstance(left,int): left = [left]
    if isinstance(right,int): right = [right]
    # if isinstance(left,list) and isinstance(right,list):
    for lsub,rsub in zip(left,right):
        sub = is_in_order(lsub, rsub)
        if sub is not None: return sub
    if len(left)<len(right):return True
    if len(left)>len(right):return False
    return None

    

with open("13.txt") as file:
    blocks = file.read().split("\n\n")
pairs = [tuple(map(eval,block.splitlines())) for block in blocks]
test_blocks = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".split("\n\n")
test_pairs = [tuple(map(eval,block.splitlines())) for block in test_blocks]
for i,p in enumerate(test_pairs,1):print(i,is_in_order(*p))
print("Part 1:",sum(i for i,p in enumerate(pairs,1) if is_in_order(*p)))
pk2,pk6 = PacketWrapper([[2]]),PacketWrapper([[6]])
packets = [pk2,pk6]
for p in pairs:
    for a in p:
        packets.append(PacketWrapper(a))
packets.sort()
p2 = (packets.index(pk2)+1)*(packets.index(pk6)+1)
print("Part 2:",p2)
