def parse_packet(packet,i=0):
    ver=int(packet[i:i+3],2)
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
        return (ver,pid,lit),j+5,ver
    len_type_id = packet[i+6]
    sub_pacs=[]
    v_sum=ver
    if len_type_id=='0':
        total_len_subpackets = int(packet[i+7:i+22],2)
        j=i+22
        while j<i+22+total_len_subpackets:
            pac,j,v = parse_packet(packet,j)
            sub_pacs.append(pac)
            v_sum+=v
    elif len_type_id=='1':
        num_sub_packets = int(packet[i+7:i+18],2)
        j=i+18
        for _ in range(num_sub_packets):
            pac,j,v = parse_packet(packet,j)
            sub_pacs.append(pac)
            v_sum+=v
    return (ver,pid,sub_pacs),j,v_sum

from math import prod
def gt(v):return int(int.__gt__(*v))
def lt(v):return int(int.__lt__(*v))
def eq(v):return int(int.__eq__(*v))

def process_tree(tree):
    ver,pid,val = tree
    if pid==4:return val
    return (sum,prod,min,max,None,gt,lt,eq)[pid](map(process_tree,val))

def hex2bin(hex_str):return format(int(hex_str,16),f'0{len(hex_str)*4}b')

def tree_view(tree,solve=False,depth=0,last=True,depths=set(),OPS='+*v^#><='):
    """Prints the tree (and optionally, the solved value at each node)
    tree: tuple(version, type_id, [subtrees, ...]|int)
    solve: bool - prints the calculated value of each node"""
    depths.add(depth)
    if last: depths.discard(depth)
    ver,pid,val = tree
    out="".join((' │'[d in depths] for d in range(1,depth)))\
        +('├└'[last] if depth else '')+f"V:{ver};T:{pid} ({OPS[pid]})"
    if isinstance(val,int):
        print(out,f"[{val}]")
    else:
        if solve:
            out+=f" = {process_tree(tree)}"
        print(out)
        for v in val[:-1]:
            tree_view(v,solve,depth+1,False)
        tree_view(val[-1],solve,depth+1)

def evaluate(hex_input,view=True,solve=True):
    binput = hex2bin(hex_input.strip())
    tree,j,ver_sum=parse_packet(binput)
    solution=process_tree(tree)
    if view:
        print('Version Sum:',ver_sum)
        print('Trailing 0s:',binput[j:])
        print('Solution:',solution)
        tree_view(tree,solve)
    return ver_sum,solution

with open('16.txt') as file:
    data = file.read()
print('Part 1: {}\nPart 2: {}'.format(*evaluate(data)))
