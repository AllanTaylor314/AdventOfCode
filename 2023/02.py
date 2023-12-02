import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()

games = {}
for line in lines:
    game_id, data = line.split(": ")
    parts = data.split("; ")
    game_id = int(game_id.split()[1])
    games[game_id] = part_list = []
    for part in parts:
        print(part)
        part_list.append({col:int(n) for n,col in map(str.split,part.split(", "))})
    print(part_list)

def validate_game(game):
    for dct in game:
        if dct.get('red',0) > 12 or dct.get('green',0) > 13 or dct.get('blue',0) > 14:
            return False
    return True

def max_cubes(game):
    out = {'red':0,'green':0,'blue':0}
    for dct in game:
        for s in ('red','green','blue'):
            out[s] = max(out[s],dct.get(s,0))
    return out['red']*out['green']*out['blue']


timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = sum(gid for gid,game in games.items() if validate_game(game))

print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
p2 = sum(max_cubes(game) for gid,game in games.items())

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
