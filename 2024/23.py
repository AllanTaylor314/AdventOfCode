import os
from pathlib import Path
from time import perf_counter
from collections import defaultdict, Counter
from functools import cache
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
DIRECTIONS = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)][::2]
def add(*ps): return tuple(map(sum,zip(*ps)))
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
pairs = [line.split("-") for line in lines]
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = 0
connected = defaultdict(set)
for a,b in pairs:
    connected[a].add(b)
    connected[b].add(a)

triples = set()
for first, adjs in connected.items():
    for second in adjs:
        for third in adjs&connected[second]-{first,second}:
            triples.add(tuple(sorted((first,second,third))))

good_triples = set(trip for trip in triples if any(t.startswith("t") for t in trip))
p1 = len(good_triples)
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
@cache
def build_fully_connected_subgraph(nodes=frozenset()):
    best = nodes
    for start in connected:
        if start in nodes:
            continue
        if nodes - connected[start]:
            continue
        new = build_fully_connected_subgraph(nodes|{start})
        if len(new) > len(best):
            best = new
    return best

# p2 = ",".join(sorted(build_fully_connected_subgraph()))

# algorithm BronKerbosch1(R, P, X) is
def BronKerbosch(r, p, x):
#   if P and X are both empty then
    if not p and not x:
#       report R as a maximal clique
        yield r
        return
#   for each vertex v in P do
    while p:
        v = p.pop()
        p.add(v)
#       BronKerbosch1(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
        yield from BronKerbosch(r|{v}, p&connected[v], x&connected[v])
#       P := P \ {v}
        p.remove(v)
#       X := X ⋃ {v}
        x.add(v)

p2 = ",".join(sorted(max(BronKerbosch(set(),set(connected),set()),key=len)))

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
