import os
from pathlib import Path
from collections import defaultdict
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    rule_text,update_text = file.read().split("\n\n")
rules = [tuple(map(int,rule.split("|"))) for rule in rule_text.splitlines()]
updates = [list(map(int,line.split(","))) for line in update_text.splitlines()]

prereqs = defaultdict(set)
for a,b in rules:
    prereqs[b].add(a)
############################## PART 1 & 2 ##############################
def is_correct_order(pages):
    remaining_pages = set(pages)
    for page in pages:
        remaining_pages.remove(page)
        if remaining_pages & prereqs[page]:
            return False
    return True

def sort_pages(pages):
    remaining_pages = set(pages)
    for i,_ in enumerate(pages):
        for j,page in enumerate(pages):
            if j<i:continue
            if not prereqs[page] & remaining_pages:
                pages[i],pages[j]=pages[j],pages[i]
                remaining_pages.remove(page)
                break
    return pages

p1 = p2 = 0
for pages in updates:
    if is_correct_order(pages):
        p1 += pages[len(pages)//2]
    else:
        p2 += sort_pages(pages)[len(pages)//2]

print("Part 1:",p1)
print("Part 2:",p2)
timer_script_end=perf_counter()
print(f"""Execution times (sec)
Total: {timer_script_end-timer_script_start:3.3f}""")
