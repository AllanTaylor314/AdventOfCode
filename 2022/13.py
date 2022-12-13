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
    for lsub,rsub in zip(left,right):
        sub = is_in_order(lsub, rsub)
        if sub is not None: return sub
    if len(left)<len(right):return True
    if len(left)>len(right):return False
    return None


with open("13.txt") as file:
    blocks = file.read().split("\n\n")
pairs = [tuple(map(eval,block.splitlines())) for block in blocks]

print("Part 1:",sum(i for i,p in enumerate(pairs,1) if is_in_order(*p)))
pk2,pk6 = PacketWrapper([[2]]),PacketWrapper([[6]])
packets = [pk2,pk6]
for p in pairs:
    for a in p:
        packets.append(PacketWrapper(a))
packets.sort()
p2 = (packets.index(pk2)+1)*(packets.index(pk6)+1)
print("Part 2:",p2)
