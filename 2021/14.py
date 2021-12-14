from collections import Counter

with open('14.txt') as file:
    data = file.read()
polymer,_,*subs_str=data.splitlines()
subs={a:b for a,b in (s.split(' -> ') for s in subs_str)}

def polymerise(poly):
    out=""
    for a,b in zip(poly,poly[1:]):
        out+=a+subs.get(a+b,'')
    return out+b

poly=polymer
for _ in range(10):
    poly=polymerise(poly)

c1=Counter(poly)
print('Part 1:',max(c1.values())-min(c1.values()))

pair_count=Counter()
for a,b in zip(polymer,polymer[1:]):
    pair_count[a+b]+=1
for _ in range(40):
    new_pair_count=pair_count.copy()
    for pair,new in subs.items():
        count = pair_count[pair]
        new_pair_count[pair]-=count
        a,b=pair
        new_pair_count[a+new]+=count
        new_pair_count[new+b]+=count
    pair_count=new_pair_count
counter = Counter()
counter2= Counter()
for pair, count in pair_count.items():
    a,b = pair
    counter[a]+=count
    counter2[b]+=count
counter2[polymer[0]]+=1
counter[polymer[-1]]+=1
assert counter==counter2
assert 0 not in counter.values()
print('Part 2:',max(counter.values())-min(counter.values()))
