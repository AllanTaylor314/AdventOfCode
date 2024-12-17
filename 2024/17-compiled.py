from collections import defaultdict
from itertools import count

target = "2,4,1,5,7,5,1,6,4,2,5,5,0,3,3,0"

def run(A):
    B = C = 0
    O = []
    while True:
        B = A % 8       # 2 4 bst A
        B ^= 5          # 1 5 bxl 5
        C = A >> B      # 7 5 cdv B
        B ^= 6          # 1 6 bxl 6
        B ^= C          # 4 2 bxc X
        O.append(B % 8) # 5 5 out B
        A >>= 3         # 0 3 adv 3
        if A == 0:break # 3 0 jnz 0
    return ",".join(map(str,O))

def run2(A):
    O = []
    while True:
        C = A >> (A & 0b111 ^ 0b101)
        B = A ^ 0b011 ^ C
        O.append(B & 0b111)
        A >>= 3
        if A == 0:break
    return ",".join(map(str,O))

print("Part 1:",run(33940147))

table = defaultdict(list)
for p2 in range(2**19):
    res = run2(p2)
    if res[:5] in target:
        table[res[:5]].append(p2)
print("Done generating 3s")
def merge(size):
    str_size = 2*size-1
    num_new = 0
    for i in range(0,len(target)-2*size,2):
        key = target[i:i+str_size]
        next_key = target[i+2:i+2+str_size]
        vals = table[key]
        next_vals = table[next_key]
        for val in vals:
            for nv in next_vals:
                if ((val >> 3) ^ nv) & (2**(3*size+7)-1) == 0:
                    combo_key = target[i:i+str_size+2]
                    combo_val = val|(nv<<3)
                    assert run2(combo_val).startswith(combo_key)
                    table[combo_key].append(combo_val)
                    num_new += 1
    print(f"Done merging {size}s ({num_new} possibilities)")
for i in range(3,16):
    merge(i)
p2 = min(table[target])
print("Part 2", p2)
assert run(p2) == target
