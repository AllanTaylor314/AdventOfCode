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

pile = {}
for line in lines:
    card_num, data = line.split(":")
    num = int(card_num.split()[1])
    winning, yours = data.split('|')
    winning = list(map(int,winning.split()))
    yours = list(map(int,yours.split()))
    pile[num] = winning, yours

wins = {card:len(set(win)&set(you)) for card,(win,you) in pile.items()}

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = sum(2**(n-1) for n in wins.values() if n)
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
num_copies = {c:1 for c in pile}
for card_num, num_wins in wins.items():
    for i in range(card_num+1,card_num+1+num_wins):
        num_copies[i]+=num_copies[card_num]
p2 = sum(num_copies.values())
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
