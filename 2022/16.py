import re
from functools import cache
with open("16.txt") as file:
    lines = file.read().splitlines()
valve_rates = {}
valve_map = {}
for line in lines:
    valve,flow,valves = re.match(r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z,\s]+)",line).groups()
    valve_rates[valve]=int(flow)
    valve_map[valve]=valves.split(", ")

edge_weights = {}
q = {('AA',None,'AA',0),*((v,None,v,0) for v,r in valve_rates.items() if r)} # Last hub, prev node, current node, num steps since
while q:
    hub,prev,node,steps = q.pop()
    if steps>len(valve_map):
        print("Chances are there is a loop in the tunnels")
        continue
    if hub!=node and (valve_rates[node] or node=="AA"): # This is another hub
        t = tuple(sorted((hub,node)))
        if edge_weights.get(t,9e9)>steps:
            edge_weights[t] = steps
        continue
    for n in valve_map[node]:
        if n==prev: continue
        q.add((
            hub,
            node,
            n,
            steps+1
        ))
    if len(q)>10000:
        print("q exceeded length. Stopping")
        break
nested_weights = {v:{} for v,f in valve_rates.items() if f}
nested_weights['AA'] = {}
for (a,b),w in edge_weights.items():nested_weights[a][b]=nested_weights[b][a]=w

@cache
def solver(minutes:int, open_valves:frozenset, current:str, part:int):
    if part<=0:return 0
    if minutes<=0:
        if part==1:return 0
        if part==2:return solver(26,open_valves,"AA",1)
    best = 0
    for next_valve, weight in nested_weights[current].items():
        best = max(best,solver(minutes-weight,open_valves,next_valve,part))
    if current not in open_valves:
        best = max(best,(minutes-1)*valve_rates[current]+solver(minutes-1,open_valves|{current},current,part))
    return best

print("Part 1:",solver(30,frozenset(),"AA",1))
print("Part 2:",solver(26,frozenset(),"AA",2))
