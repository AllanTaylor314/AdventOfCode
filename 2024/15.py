import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
DIRECTIONS = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,1)][::2]
UP,RIGHT,DOWN,LEFT = DIRECTIONS
def add(*ps): return tuple(map(sum,zip(*ps)))
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()
mid = lines.index("")
grid = {(i,j):c for i,line in enumerate(lines[:mid]) for j,c in enumerate(line)}
walls = frozenset(ij for ij,c in grid.items() if c=="#")
init_boxes = frozenset(ij for ij,c in grid.items() if c=="O")
init_start ,= (ij for ij,c in grid.items() if c=="@")
arrows = "".join(lines[mid:])
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
def gps(loc):
    i,j = loc
    return 100*i+j
boxes = set(init_boxes)
location = init_start
for arrow in arrows:
    d = DIRECTIONS["^>v<".index(arrow)]
    new_loc = add(location, d)
    if new_loc in walls:
        continue
    if new_loc in boxes:
        next_box = last_box = first_box = new_loc
        while next_box in boxes:
            last_box = next_box
            next_box = add(next_box, d)
        if next_box in walls:
            continue
        boxes.remove(first_box)
        boxes.add(next_box)
    location = new_loc
    assert location not in walls
    assert location not in boxes
    assert len(boxes) == len(init_boxes)
p1 = sum(map(gps,boxes))
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
P2_MAP = {"#":"##","O":"[]",".":"..","@":"@."}
grid = {(i,2*hj+dj):c for i,line in enumerate(lines[:mid]) for hj,oc in enumerate(line) for dj,c in enumerate(P2_MAP[oc])}
walls = frozenset(ij for ij,c in grid.items() if c=="#")
boxes = {ij for ij,c in grid.items() if c=="["}
init_start ,= (ij for ij,c in grid.items() if c=="@")

def display():
    right_boxes = {add(box,RIGHT) for box in boxes}
    for i in range(mid):
        for j in range(100):
            c = ""
            ij = i,j
            if ij in walls:
                c+="#"
            if ij in boxes:
                c+="["
            if ij in right_boxes:
                c+="]"
            if ij == location:
                c+="@"
            if not c:
                c+="."
            assert len(c) == 1
            print(end=c,flush=False)
        print(flush=False)
    print(flush=True)

location = init_start
for arrow in arrows:
    d = DIRECTIONS["^>v<".index(arrow)]
    new_loc = add(location, d)
    if new_loc in walls:
        continue
    related_boxes = set()
    right_boxes = {add(box,RIGHT) for box in boxes}
    if d == LEFT:
        last_box = next_box = first_box = add(new_loc,LEFT)
        if next_box in boxes:
            related_boxes.add(last_box)
            while next_box in boxes:
                last_box = next_box
                related_boxes.add(last_box)
                next_box = add(next_box,LEFT,LEFT)
        if add(last_box,LEFT) in walls:
            continue
    elif d == RIGHT:
        last_box = next_box = first_box = new_loc
        if next_box in boxes:
            related_boxes.add(last_box)
            while next_box in boxes:
                last_box = next_box
                related_boxes.add(last_box)
                next_box = add(next_box,RIGHT,RIGHT)
        if next_box in walls:
            continue
    else:
        next_box = None
        if new_loc in boxes:
            next_box = new_loc
        elif new_loc in right_boxes:
            next_box = add(new_loc, LEFT)
        if next_box is not None:
            stack = {next_box}
            while stack:
                box = stack.pop()
                assert box in boxes
                related_boxes.add(box)
                ld_box = add(box,d)
                if ld_box in boxes:
                    stack.add(ld_box)
                if ld_box in right_boxes:
                    stack.add(add(ld_box,LEFT))
                rd_box = add(box,RIGHT,d)
                if rd_box in boxes:
                    stack.add(rd_box)
                if rd_box in right_boxes:
                    stack.add(add(rd_box,LEFT))
    new_boxes = {add(box,d) for box in related_boxes}
    new_right_boxes = {add(box,RIGHT) for box in new_boxes}
    if (new_boxes|new_right_boxes)&walls:
        continue
    boxes.difference_update(related_boxes)
    boxes.update(new_boxes)
    location = new_loc
    assert location not in walls
    assert location not in boxes
    assert add(location,LEFT) not in boxes
    assert len(boxes) == len(init_boxes)

p2 = sum(map(gps,boxes))
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
