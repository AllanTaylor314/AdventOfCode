import os
from pathlib import Path
from time import perf_counter
from collections import defaultdict, deque
from copy import deepcopy
import networkx as nx
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
pairs = []
for line in lines:
    a,b = line.split(": ")
    c = b.split()
    for d in c:
        pairs.append(tuple(sorted([a,d])))
pair_dict = defaultdict(set)
for a,b in pairs:
    pair_dict[a].add(b)
    pair_dict[b].add(a)
vertices = sorted(pair_dict.keys())
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
def cluster_size(pd):
    root,*_ = pd
    cluster = {root}
    q = [root]
    while q:
        n = q.pop()
        for e in pd[n]:
            if e not in cluster:
                q.append(e)
                cluster.add(e)
    return len(cluster)

def unlink(ps):
    local_copy = deepcopy(pair_dict)
    for a,b in ps:
        local_copy[a].remove(b)
        local_copy[b].remove(a)
    return local_copy

# for i,pr1 in enumerate(pairs):
#     for j,pr2 in enumerate(pairs[i+1:],i+1):
#         for k,pr3 in enumerate(pairs[j+1:],j+1):
#             size = cluster_size(unlink([pr1,pr2,pr3]))
#             if size != len(pair_dict):
#                 p1 = size
#                 print(p1)
#         print(f"Finished {pr1},{pr2}")
#     print(f"Finished {pr1}")

# root,*_ = pair_dict
# node_counts = {p:0 for p in pair_dict}
# q = deque([root])
# while q:
#     p = q.popleft()

# https://en.wikipedia.org/wiki/Karger%27s_algorithm
# def contract(G,t):
#     while 
# def fast_min_cut(G):
#     if len(G)<=6:
#         return contract(G,2)
# triangles = {tuple(sorted([a,b,c])) for a,b in pairs for c in pair_dict[a]&pair_dict[b]}
# tri_pairs = [(a,b) for a in triangles for b in triangles if a is not b and len(set(a)&set(b))]
# quads = {tuple(sorted([a,b,c,d])) for a,b in pairs for c in pair_dict[a] for d in pair_dict[b]&pair_dict[c] if a!=d and b!=c}

G = nx.Graph()
G.add_edges_from(pairs)
cuts = nx.minimum_edge_cut(G)
assert len(cuts) == 3
G.remove_edges_from(cuts)
size = cluster_size(unlink(cuts))
p1 = size*(len(vertices)-size)

print("Part 1:",p1)
timer_part1_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
