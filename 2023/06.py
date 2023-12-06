import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    time_str,distance_str = file.read().splitlines()
td_pairs = list(zip(map(int,time_str.split()[1:]),map(int,distance_str.split()[1:])))

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
def distance_travelled(race_time, time_held):
    speed = time_held
    distance = (race_time-time_held)*speed
    return distance
def num_wins(race_time, distance):
    wins = 0
    for t in range(race_time+1):
        if distance_travelled(race_time, t)>distance:
            wins += 1
    return wins
p1 = 1
for t,d in td_pairs:
    p1 *= num_wins(t,d)

print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
p2 = num_wins(int(time_str.replace(' ','').split(":")[1]),int(distance_str.replace(' ','').split(":")[1]))

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
