A=[  1,  1,  1,  1,  1,  26,  1, 26, 26,  1, 26, 26, 26, 26]
B=[ 15, 10, 12, 10, 14, -11, 10,-16, -9, 11, -8, -8,-10, -9]
C=[ 13, 16,  2,  8, 11,   6, 12,  2,  2, 15,  1, 10, 14, 10]

CONSTS = list(zip(A,B,C))

def process(c_index,w,x=0,y=0,z=0):
    a,b,c = CONSTS[c_index]
    x*=0
    x+=z
    x%=26
    z//=a
    x+=b
    x=int(x==w)
    x=int(x==0)
    y*=0
    y+=25
    y*=x
    y+=1
    z*=y
    y*=0
    y+=w
    y+=c
    y*=x
    z+=y
    return z

def process_1(c_index,w,z=0):
    a,b,c = CONSTS[c_index]
    x=int(z%26+b!=w)
    z=z//a*(25*x+1)  # z is either * or // 26
    y=(w+c)*x
    z+=y
    return z

def solve():
    for w in range(9,0,-1):
        ans = rec_solve(0,w)
        if ans is not None:
            return ans
@cache
def rec_solve(ind,w,z=0):
    if ind>=len(CONSTS):
        return [] if z==0 else None
    nz = process_1(ind,w,z=z)
    for nw in range(9,0,-1):
        ans = rec_solve(ind+1,nw,z=nz)
        if ans is not None:
            return [w]+ans

for z in range(1000):
    for w in range(1,10):
        for c_ind in range(len(CONSTS)):
            assert process(c_ind,w,z=z)==process_1(c_ind,w,z=z),(c_ind,w,z)

pos_pairs = [
    (0,13),
    (1,12),
    (2,11),
    (3,8),
    (4,5),
    (6,7),
    (9,10)
]
pairs = []
for a,b in pos_pairs:
    #for b in neg_inds:
    for wa in range(9,0,-1):
        for wb in range(9,0,-1):
            if process_1(b,wb,process_1(a,wa,0))==0:
                pairs.append((a,wa,b,wb))

pair_set = set(pairs)

def generate_possible_numbers(num_tupl=(0,)*14,used=None):
    if used is None: used = set()
    for pair in pairs:
        if pair in used: continue
        a_ind,wa,b_ind,wb = pair
        if num_tupl[a_ind]==0==num_tupl[b_ind]:
            num_copy = list(num_tupl)
            num_copy[a_ind] = wa
            num_copy[b_ind] = wb
            if 0 in num_copy:
                yield from generate_possible_numbers(tuple(num_copy),used|{pair})
            else:
                yield num_copy

print('Part 1: ',*next(generate_possible_numbers()),sep='',flush=True)
pairs.reverse()
print('Part 2: ',*next(generate_possible_numbers()),sep='',flush=True)