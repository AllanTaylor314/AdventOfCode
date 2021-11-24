from itertools import combinations

def sum_subset(superset, target):
    if target<=0:
        yield tuple()
    else:
        if not isinstance(superset,set):
            superset=set(superset)
        for item in list(superset)[::-1]:
            if target==item:
                yield (item,)
            if target<=item:
                continue
            for subset in sum_subset({_ for _ in superset if _>item},target-item):
                yield (item,)+subset

def validate_subset(subset,fullset,target):
    if not isinstance(subset, set):subset=set(subset)
    if not isinstance(fullset, set):fullset=set(fullset)
    try:
        next(sum_subset(fullset-subset,target))
    except StopIteration:
        return False
    return True

def quantum_entanglement(nums):
    j=1
    for n in nums:
        j*=n
    return j

with open('24.txt') as file:
    weights = list(map(int,file.readlines()))
#weights = list(range(1,6))+list(range(7,12))


total_weight = sum(weights)
group_weight = total_weight//3
assert total_weight%3==0  # Gotta be equal sizes

groups = []
smallest = len(weights)
for group in sum_subset(weights,group_weight):
    assert sum(group)==group_weight
    if validate_subset(group,weights,group_weight):
        if len(group)<=smallest:
            if len(group)<smallest:
                smallest=len(group)
                groups = []
            groups.append(group)
    else:
        print(f"{group} is not possible", flush=True)

print('Part 1:',min(map(quantum_entanglement,groups)))


###################### Part 2 #####################

group_weight = total_weight//4
assert total_weight%4==0  # Gotta be equal sizes

groups = []
smallest = len(weights)
for group in sum_subset(weights,group_weight):
    assert sum(group)==group_weight
    if validate_subset(group,weights,group_weight):
        if len(group)<=smallest:
            if len(group)<smallest:
                smallest=len(group)
                groups = []
            groups.append(group)
    else:
        print(f"{group} is not possible", flush=True)

print('Part 2:',min(map(quantum_entanglement,groups)))

# Part 1: 10439961859
# Part 2: 72050269