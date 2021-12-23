from copy import deepcopy
from functools import cache
#import sys
#sys.setrecursionlimit(3000)


A,B,C,D = 'ABCD'
INF = float('inf')
COSTS  = {
    A:1,
    B:10,
    C:100,
    D:1000,
}
DOORS_HALL = {
    1:2,
    2:4,
    3:6,
    4:8
}
DOORS = {2,4,6,8}
TARGETS = dict(zip('ABCD',(2,4,6,8)))

state0 = (
    (None,)*11,
    (B,B),
    (A,C),
    (A,D),
    (D,C)
)

test_state0 = (
    (None,)*11,
    (B,A),
    (C,D),
    (B,C),
    (D,A)
)

target_state = (
    (None,)*11,
    (A,A),
    (B,B),
    (C,C),
    (D,D)
)

one_step = (
    (None, None, None, None, None, None, None, None, None, D, None),
    (A,A),
    (B,B),
    (C,C),
    (None,D)
)

def possible_moves(state):
    # Move top amphipod
    for i in range(1,5):
        mut_state = list(map(list,state))
        if None is not mut_state[i][0] == mut_state[i][1] and DOORS_HALL[i]==TARGETS[mut_state[i][0]]:
            continue
        cost = 0
        if mut_state[i][0] is None:
            if mut_state[i][1] is None:
                continue
            if TARGETS[mut_state[i][1]] == DOORS_HALL[i]:
                continue
            amp = mut_state[i][1]
            mut_state[i][1] = None
            cost+=2*COSTS[amp]
        else:
            if mut_state[i][0]==mut_state[i][1] and TARGETS[mut_state[i][0]] == DOORS_HALL[i]:
                continue
            amp = mut_state[i][0]
            mut_state[i][0] = None
            cost+=COSTS[amp]
        possible_locations = []
        for j in range(DOORS_HALL[i]):
            if j not in DOORS:
                possible_locations.append(j)
            if mut_state[0][j] is not None:
                possible_locations.clear()
        for j in range(DOORS_HALL[i],11):
            if mut_state[0][j] is not None:
                break
            if j not in DOORS:
                possible_locations.append(j)
        semi_mut_state = list(map(tuple,mut_state))
        hall = state[0]
        for p in possible_locations:
            mut_hall = list(hall)
            mut_hall[p]=amp
            semi_mut_state[0]=tuple(mut_hall)
            yield tuple(semi_mut_state),(cost+abs(p-DOORS_HALL[i])*COSTS[amp])
    # Move into room
    for j,amp in enumerate(state[0]):
        if amp is None: continue
        room = ' ABCD'.index(amp)
        if state[room] not in {(None,None),(None,amp)}:
            continue 
        if j<TARGETS[amp]:
            sl = slice(j+1,TARGETS[amp]+1)
        else:
            sl = slice(TARGETS[amp],j)
        for t in state[0][sl]:
            if t is not None:
                break
        else:
            steps = abs(j-TARGETS[amp])
            mut_state = list(map(list,state))
            mut_state[0][j] = None
            room_list = mut_state[room]
            top,bot = room_list
            if bot is None:
                room_list[1] = amp
                steps += 2
            else:
                room_list[0] = amp
                steps += 1
            yield tuple(map(tuple,mut_state)),steps*COSTS[amp]

@cache
def steps_to_final(state):
    if state==target_state: return 0
    possible_costs = [INF]
    for new_state,cost in possible_moves(state):
        possible_costs.append(cost+steps_to_final(new_state))
    #if possible_costs[-1] is INF:
        #print(state)
    return min(possible_costs)

with open('23.txt') as file:
    data = file.read()

print('Part 1:',steps_to_final(state0))
print('Part 2:',)