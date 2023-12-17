import os
from pathlib import Path
from time import perf_counter
from collections import defaultdict, deque
import doctest
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
N,E,W,S = -1j,1,-1,1j
L,R = -1j, 1j
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
COSTS = {complex(x,y):int(c) for y,line in enumerate(lines) for x,c in enumerate(line)}

def solver(lower_bound, upper_bound, costs=COSTS):
    r"""Calculate the heat loss
    The crucible can turn (or stop) if the number of lower_bound < number of steps <= upper_bound
    
    >>> part1_test_data = {complex(x,y):int(c) for y,line in enumerate("2413432311323\n3215453535623\n3255245654254\n3446585845452\n4546657867536\n1438598798454\n4457876987766\n3637877979653\n4654967986887\n4564679986453\n1224686865563\n2546548887735\n4322674655533".splitlines()) for x,c in enumerate(line)}
    >>> part2_test_data = {complex(x,y):int(c) for y,line in enumerate("111111111111\n999999999991\n999999999991\n999999999991\n999999999991".splitlines()) for x,c in enumerate(line)}
    >>> solver(0,3,part1_test_data)
    102
    >>> solver(3,10,part1_test_data)
    94
    >>> solver(3,10,part2_test_data)
    71
    """
    last = max(costs,key=abs)
    cost_map = defaultdict(lambda: [1e100]*upper_bound) # (position,src_d): {n_straight:cost}
    cost_map[S,S][0] = costs[S] # The start doesn't count for consecutive blocks nor heat loss
    cost_map[E,E][0] = costs[E]
    todo = deque([S+S,S+E,E+E])
    pending = set(todo)
    while todo:
        coord = todo.popleft()
        pending.discard(coord)
        for src in (N,E,W,S):
            current = cost_map[coord,src]
            old = current.copy()
            current[0] = min(current[0],min(
                                        *cost_map[coord-src,src*L][lower_bound:],
                                        *cost_map[coord-src,src*R][lower_bound:]
                                            )+costs[coord])
            for i in range(1,upper_bound):
                current[i] = min(current[i],cost_map[coord-src,src][i-1]+costs[coord])
            if old != current:
                for new_coord in (coord+d for d in (src,src*L,src*R) if coord+d in costs):
                    if new_coord not in pending:
                        pending.add(new_coord)
                        todo.append(new_coord)
    return min(min(cost_map[last,d][lower_bound:]) for d in (N,E,W,S))
print(doctest.testmod())
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = solver(0,3)
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
p2 = solver(3,10)
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
