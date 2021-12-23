from functools import cache

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

def possible_moves(state):
    # Move top amphipod
    for i in range(1,5):
        top_index = 0
        try:
            while state[i][top_index] is None: top_index+=1
        except IndexError:
            continue # Nothing in this room, nothing to do
        mut_state = list(map(list,state))
        amp = mut_state[i][top_index]
        # If everthing under it is in the right place
        if TARGETS[amp]==(-1,2,4,6,8)[i] and all(
            amp==other for other in state[i][top_index:]):
            continue # Don't move it out
        steps = top_index
        mut_state[i][top_index]=None
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
            yield tuple(semi_mut_state),((1+steps+abs(p-DOORS_HALL[i]))*COSTS[amp])
    # Move into room
    for j,amp in enumerate(state[0]):
        if amp is None: continue
        room = ' ABCD'.index(amp)
        room_set = set(state[room])
        room_set.discard(None)
        # If the room doesn't contain only its type, don't bother
        # If there is something there and it isn't me
        if room_set and {amp} != room_set:
            continue # Keep out
        if j<TARGETS[amp]:
            sl = slice(j+1,TARGETS[amp]+1)
        else:
            sl = slice(TARGETS[amp],j)
        # Is the path to my room clear?
        for t in state[0][sl]:
            if t is not None: # Curses... foiled again
                break
        else: # Yep, let's go
            steps = abs(j-TARGETS[amp])
            mut_state = list(map(list,state))
            mut_state[0][j] = None  # Remove from hall
            room_list = mut_state[room]
            for top_index,val in reversed(list(enumerate(room_list))):
                if val is None: break
            assert room_list[top_index] is None  # Verify that we can go here
            room_list[top_index]=amp
            steps+=1+top_index
            yield tuple(map(tuple,mut_state)),steps*COSTS[amp]

@cache
def steps_to_final(state):
    if state==target_state: return 0
    possible_costs = [INF]
    for new_state,cost in possible_moves(state):
        possible_costs.append(cost+steps_to_final(new_state))
    return min(possible_costs)

with open('23.txt') as file:
    data = file.read()
letters = [c for c in data if c.isalpha()]
rows = letters[:4],letters[4:]

state1 = (
    (None,)*11,
) + tuple(zip(*rows))

ROOM_SIZE = len(state1[1])
target_state = (
    (None,)*11,
    (A,)*ROOM_SIZE,
    (B,)*ROOM_SIZE,
    (C,)*ROOM_SIZE,
    (D,)*ROOM_SIZE
)

print('Part 1:',steps_to_final(state1))

#################################### PART 2 ####################################

folded_page = (
    (D,D),
    (C,B),
    (B,A),
    (A,C)
)

state2 = (
    (None,)*11,
) + tuple((a,b,c,d) for (a,d),(b,c) in zip(state1[1:],folded_page))

ROOM_SIZE = len(state2[1])
target_state = (
    (None,)*11,
    (A,)*ROOM_SIZE,
    (B,)*ROOM_SIZE,
    (C,)*ROOM_SIZE,
    (D,)*ROOM_SIZE
)

print('Part 2:',steps_to_final(state2))
