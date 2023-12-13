import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    notes = file.read().split('\n\n')

def is_vertical_mirror(note, index):
    lines = note.splitlines()
    width = len(lines[0])
    reflection_width = min(index, width-index)
    for line in lines:
        left = line[:index]
        right = line[index:]
        assert left
        assert right
        if left[::-1].startswith(right) or right.startswith(left[::-1]):
            pass
        else:
            return False
    return True

def is_horizontal_mirror(note, index):
    lines = note.splitlines()
    assert lines[index-1::-1]
    assert lines[index::]
    return all(a==b for a,b in zip(lines[index-1::-1],lines[index::]))

def score_note(note,ignore=0):
    if note[-1] != '\n':
        note += '\n'
    width = note.index('\n')
    height = len(note.splitlines())
    for i in range(1,width):
        if ignore!=i and is_vertical_mirror(note,i):
            return i
    for i in range(1,height):
        if ignore!=i*100 and is_horizontal_mirror(note,i):
            return i * 100
    raise ValueError("Mirror not found in note")

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
p1 = sum(map(score_note,notes))

print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
p2 = 0
def gen_alts(note):
    for i,c in enumerate(note):
        if c != '\n':
            yield note[:i]+('.#'[c=='.'])+note[i+1:]

for i,note in enumerate(notes):
    old_score = score_note(note)
    for alt in gen_alts(note):
        try:
            new_score = score_note(alt,ignore=old_score)
        except ValueError:
            continue
        else:
            if new_score != old_score:
                p2 += new_score
                break

print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
