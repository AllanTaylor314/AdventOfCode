from functools import reduce

AtoG='abcdefg'
NUMBER_SEGMENTS=[
'ABCEFG',
'CF',
'ACDEG',
'ACDFG',
'BCDF',
'ABDFG',
'ABDEFG',
'ACF',
'ABCDEFG',
'ABCDFG'
]

def deduce_line(ten_digits,output):
    omega=set(AtoG.upper())
    candidates={l:set(AtoG) for l in AtoG.upper()}
    ten_digits=sorted(ten_digits,key=len)
    one,seven,four,*_=ten_digits
    fives=ten_digits[3:6]  # 2,3,5
    sixes=ten_digits[6:9]  # 0,6,9
    
    # The easy numbers
    for n,n_set in [
        (1,set(one)),
        (4,set(four)),
        (7,set(seven))
        ]:
        for seg in omega-set(NUMBER_SEGMENTS[n]):
            candidates[seg]-=n_set
        for seg in NUMBER_SEGMENTS[n]:
            candidates[seg]&=n_set
    
    # The five segment numbers
    # A, D, and G are in 2, 3, & 5; nothing else is in all three
    adg=reduce(set.intersection,map(set,fives))
    for seg in 'ADG':
        candidates[seg]&=adg
    for seg in 'BCEF':
        candidates[seg]-=adg
    
    # The six segment numbers
    # F is in 0, 6, & 9; C is not in 6
    candidates['F']&=reduce(set.intersection,map(set,sixes))
    candidates['C']-=candidates['F']
    
    # The ouput numbers
    wire_seg = {}
    for seg,wires in candidates.items():
        wire,=wires
        wire_seg[wire]=seg
    out=0
    for dig in output:
        out*=10
        out+=NUMBER_SEGMENTS.index("".join(sorted(map(wire_seg.get, dig))))
    return out

with open('08.txt') as file:
    data=file.read().splitlines()
digs=[]
outs=[]
for line in data:
    left,right=line.split(' | ')
    digs.append(left.split())
    outs.append(right.split())

all_outs=[]
for out in outs:
    all_outs.extend(out)

easy_outs=[o for o in all_outs if len(o) in {2,4,3,7}]
print('Part 1:',len(easy_outs))

assert deduce_line(*(list(map(str.lower,NUMBER_SEGMENTS))[::-1],)*2)==9876543210
print('Part 2:',sum(map(deduce_line,digs,outs)))
