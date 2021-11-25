with open('19.txt') as file:
    data = file.read().splitlines()

*swaps,_,meds = data

replace_list = []
for line in swaps:
    replace_list.append(tuple(line.split(' => ')))

possible_outcomes = set()
for sub,rep in replace_list:
    i=0
    for n in range(meds.count(sub)):
        while not meds[i:].startswith(sub):
            i+=1
        possible_outcomes.add(meds[:i]+rep+meds[i+len(sub):])
        i+=1
print('Part 1:',len(possible_outcomes), flush=True)


def predecessors(mol):
    global replace_list
    for rep,sub in replace_list:
        i=0
        while (i:=mol.find(sub,i))!=-1:
            yield mol[:i]+rep+mol[i+len(sub):]
            i+=1

CACHE_MIN_STEPS = {'e':0}  # Init with base case
CACHE_LOOKUPS = 0
MIN_DEPTH = float('inf')
def min_steps(mol, depth=0):
    global CACHE_LOOKUPS,MIN_DEPTH
    if depth>MIN_DEPTH:return float('inf')
    if mol=='e' and depth<MIN_DEPTH:MIN_DEPTH=depth;print(f'Found depth {depth}')
    if mol in CACHE_MIN_STEPS:
        CACHE_LOOKUPS+=1
        return CACHE_MIN_STEPS[mol]
    if len(CACHE_MIN_STEPS)%10000==0:
        print(f'Cache @ {len(CACHE_MIN_STEPS)} ({CACHE_LOOKUPS} lookups)',flush=True)
    try:
        steps = min(min_steps(m,depth=depth+1) for m in predecessors(mol))+1
    except ValueError:
        steps = float('inf')
    CACHE_MIN_STEPS[mol]=steps
    return steps

print('Part 2:',min_steps(meds))
# Part 2: 200