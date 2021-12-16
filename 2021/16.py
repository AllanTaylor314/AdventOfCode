from functools import reduce
VERSION_SUM=0

def parse_packet(packet,i=0):
    ver=int(packet[i:i+3],2)
    global VERSION_SUM
    VERSION_SUM+=ver
    pid=int(packet[i+3:i+6],2)
    if pid==4: # Literal value
        j=i+6
        rep=''
        while True:
            rep+=packet[j+1:j+5]
            if packet[j]=='0':
                break
            j+=5
        lit = int(rep,2)
        return (ver,pid,lit),j+5
    len_type_id = packet[i+6]
    if len_type_id=='0':
        total_len_subpackets = int(packet[i+7:i+22],2)
        j=i+22
        sub_pacs=[]
        while j<i+22+total_len_subpackets:
            pac,j = parse_packet(packet,j)
            sub_pacs.append(pac)
        return (ver,pid,sub_pacs),j
    elif len_type_id=='1':
        num_sub_packets = int(packet[i+7:i+18],2)
        j=i+18
        sub_pacs=[]
        for _ in range(num_sub_packets):
            pac,j = parse_packet(packet,j)
            sub_pacs.append(pac)
        return (ver,pid,sub_pacs),j
    else: raise ValueError(len_type_id)

def process_tree(tree):
    ver,pid,val = tree
    if isinstance(val,int):
        return val
    vals=map(process_tree,val)
    if pid==0:
        return sum(vals)
    if pid==1:
        return reduce(int.__mul__,vals)
    if pid==2:
        return min(vals)
    if pid==3:
        return max(vals)
    a,b = vals
    if pid==5:
        return int(a>b)
    if pid==6:
        return int(a<b)
    if pid==7:
        return int(a==b)

def tree_view(tree,solve=False,depth=0,last=True,depths=set(),OPS='+*v^ ><='):
    """Prints the tree (and optionally, the solved value at each node)
    tree: tuple(version, type_id, [subtrees, ...]|int)
    solve: bool - prints the calculated value of each node"""
    depths.add(depth)
    if last: depths.discard(depth)
    ver,pid,val = tree
    out="".join((' │'[d in depths] for d in range(depth)))\
        +('├└'[last])+f"V:{ver};T:{pid} ({OPS[pid]})"
    if isinstance(val,int):
        print(out[:-4],f"[{val}]")
    else:
        if solve:
            out+=f" = {process_tree(tree)}"
        print(out)
        for v in val[:-1]:
            tree_view(v,solve,depth+1,False)
        tree_view(val[-1],solve,depth+1)

with open('16.txt') as file:
    data = file.read().strip()

packet=format(int(data,16),f'0{len(data)*4}b')
tree,_ = parse_packet(packet)

print('Part 1:',VERSION_SUM)
print('Part 2:',process_tree(tree))
tree_view(tree,True)
