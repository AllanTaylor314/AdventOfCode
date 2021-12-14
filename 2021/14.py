from collections import Counter

with open('14.txt') as file:
    data = file.read()
polymer,_,*subs_str=data.splitlines()
subs=[s.split(' -> ') for s in subs_str]
sub_dict={a:b for a,b in subs}

def polymerise(poly):
    out=""
    for a,b in zip(poly,poly[1:]):
        out+=a
        if a+b in sub_dict:
            out+=sub_dict[a+b]
    return out+b

poly=polymer
for _ in range(10):
    poly=polymerise(poly)

c1=Counter(poly)
print('Part 1:',max(c1.values())-min(c1.values()),flush=True)

ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
pair_count={a+b:0 for a in ALPHABET for b in ALPHABET}
for a,b in zip(polymer,polymer[1:]):
    pair_count[a+b]+=1
for _ in range(40):
    new_pair_count=pair_count.copy()
    for pair,new in subs:
        count = pair_count[pair]
        new_pair_count[pair]-=count
        a,b=pair
        new_pair_count[a+new]+=count
        new_pair_count[new+b]+=count
    pair_count=new_pair_count
counter = {a:0 for a in ALPHABET}
counter2= {b:0 for b in ALPHABET}
for pair, count in pair_count.items():
    a,b = pair
    counter[a]+=count
    counter2[b]+=count
counter2[polymer[0]]+=1
counter[polymer[-1]]+=1
assert counter==counter2
non_zero_counts = set(counter.values())
non_zero_counts.discard(0)
print('Part 2:',max(non_zero_counts)-min(non_zero_counts))