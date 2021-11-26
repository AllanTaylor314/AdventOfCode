from time import perf_counter

OFFSET = 30

with open('12.txt') as file:
    init,_,*rules = file.read().splitlines()
init = init.split()[2]

rule_dict = {llcrr:n for llcrr,n in map(lambda s:s.split(' => '), rules)}

print(' '*OFFSET+'0')
current = '.'*OFFSET+init+'.'*OFFSET
for _ in range(20):
    print(current)
    new = list(current)
    for i in range(2,len(current)-2):
        new[i]=rule_dict[current[i-2:i+3]]
    current=''.join(new)
print(current)

print('Part 1:', sum(i-OFFSET for i,p in enumerate(current) if p=='#'), flush=True)

############# PART 2 ##############
def delta(state):
    sorted_state = sorted(state)
    return tuple(b-a for a,b in zip(sorted_state,sorted_state[1:]))

live = set(i for i,p in enumerate(init) if p=='#')
states = {}
deltas = {}
min_live=min(live)
max_live=max(live)
FIFTY_BILLION=50_000_000_000
start = perf_counter()
for _ in range(FIFTY_BILLION):
    if _%10000==0: print(f'Step {_:11d}: {_/FIFTY_BILLION*100:.5f}% (t={perf_counter()-start:.0f}, {len(live)=})')
    new = set()
    for i in {x+d for x in live for d in range(-2,3)}:
        if rule_dict[''.join('.#'[p in live] for p in range(i-2,i+3))]=='#':
            new.add(i)
    new_state = tuple(new)
    new_delta = delta(new_state)
    states[_]=new_state
    if new_delta in deltas:
        print(f'Delta duplicate ({_} matches {deltas[new_delta]})')
        break
    else:
        deltas[new_delta]=_
    live=new
d_index = deltas[new_delta]
state=states[d_index]
end = perf_counter()
print('Part 2:', sum(state)+(FIFTY_BILLION-d_index-1)*len(state), f"(Time taken: {end-start} seconds)")

# Part 2: 3450000002268