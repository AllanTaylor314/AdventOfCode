import re
from collections import deque
with open("16.txt") as file:
    lines = file.read().splitlines()
test_lines="""Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".splitlines()
valve_rates = {}
value_map = {}
for line in lines:
    valve,flow,valves = re.match(r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z,\s]+)",line).groups()
    valve_rates[valve]=int(flow)
    value_map[valve]=valves.split(", ")

p1 = 0
# mins remaining, total relief, {open valves}, current valve
q = deque([(30,0,set(),None,"AA")])
max_relief = 0
count = 0
while q:
    count+=1
    if count%100000==0:
        print(count, len(q), mins, max_relief)
    mins, relief, open_valves, previous_valve, current_valve = q.pop()
    if relief>max_relief:max_relief=relief
    if mins<=0: continue
    if current_valve not in open_valves and valve_rates[current_valve]:
        q.append((
            mins-1,
            relief+(mins-1)*valve_rates[current_valve],
            open_valves|{current_valve},
            current_valve,
            current_valve
            ))
    for next_valve in value_map[current_valve]:
        if next_valve==previous_valve:continue # No oscillating! (This saved so much time)
        q.append((
            mins-1,
            relief,
            open_valves,
            current_valve,
            next_valve
        ))

print("Part 1:",max_relief) # 1595 (didn't even wait for it to finish)
p2 = 0

print("Part 2:",p2)
