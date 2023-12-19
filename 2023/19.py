import os
from pathlib import Path
from time import perf_counter
from operator import lt, gt
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
def parse_rule(rule):
    label,rest = rule.split('{')
    return {label:rest[:-1].split(',')}
def parse_part(part):
    return eval(f"dict({part[1:-1]})")
with open(INPUT_PATH) as file:
    rulestr, partstr = file.read().split("\n\n")
rules = {}
for r in rulestr.splitlines():
    rules.update(parse_rule(r))
parts = list(map(parse_part,partstr.splitlines()))
timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
COMP_DICT = {'<':lt,'>':gt}
def workflow(rule:str,part):
    if rule == 'A':
        return True
    if rule == 'R':
        return False
    *conds,default = rules[rule]
    for cond in conds:
        cond,target = cond.split(':')
        xmas = cond[0]
        comp = cond[1]
        val = int(cond[2:])
        if COMP_DICT[comp](part[xmas],val):
            return workflow(target, part)
    return workflow(default,part)

p1 = sum(sum(p.values()) for p in parts if workflow('in',p))
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
MAX_RANGE = range(1,4001)
class QuantumPart:
    def __init__(self,x=MAX_RANGE,m=MAX_RANGE,a=MAX_RANGE,s=MAX_RANGE) -> None:
        self.x = x
        self.m = m
        self.a = a
        self.s = s
    def copy(self):
        return QuantumPart(self.x,self.m,self.a,self.s)
    def apply_cond(self, xmas, comp, value):
        truthy = self.copy()
        falsy = self.copy()
        rating = getattr(self,xmas)
        if comp == '>':
            t = range(value+1,rating.stop)
            f = range(rating.start,value+1)
        elif comp == '<':
            t = range(rating.start,value)
            f = range(value,rating.stop)
        setattr(truthy,xmas,t)
        setattr(falsy,xmas,f)
        return truthy,falsy
    def __len__(self):
        return len(self.x)*len(self.m)*len(self.a)*len(self.s)


def quantum_workflow(rule:str,qpart):
    if rule == 'A':
        return len(qpart)
    if rule == 'R':
        return 0
    *conds,default = rules[rule]
    total = 0
    for cond in conds:
        cond,target = cond.split(':')
        xmas = cond[0]
        comp = cond[1]
        val = int(cond[2:])
        tpart, qpart = qpart.apply_cond(xmas,comp,val)
        total += quantum_workflow(target, tpart)
    return total + quantum_workflow(default, qpart)

p2 = quantum_workflow('in',QuantumPart())
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
