from copy import deepcopy
from collections import deque
from time import sleep
from itertools import combinations
NONE='None'
class State():
    past_states=set()
    def __init__(self):
        self.floors={
            4:set(),
            3:set(),
            2:set(),
            1:set()
        }
        self.elevator_level=1
        self.steps=0
        self.prev_state=None
    def validate_state(self):
        return all(self.validate_floor(f) for f in self.floors) and\
               0<self.elevator_level<5
    def validate_floor(self,f):
        s=self.floors[f]
        gens={i[:-1] for i in s if i[-1]=='G'}
        chips={i[:-1] for i in s if i[-1]=='M'}
        return len(gens)==0 or all(c in gens for c in chips)
    def __repr__(self):
        return f"{self.elevator_level}:{';'.join(','.join(sorted(self.floors[i])) for i in range(1,5))}"
    def __str__(self):
        o=f'State: step {self.steps}'
        for i in range(4,0,-1):
            o+=f'\nF{i} {"E " if self.elevator_level==i else ".|"}{", ".join(self.floors[i])}'
        return o
    def __eq__(self,other):
        """Checks that floors and elevator match (NOTE: steps not checked)"""
        return isinstance(other,State) and\
               self.floors==other.floors and\
               self.elevator_level==other.elevator_level
    def new_states(self):
        prev_state=self.prev_state
        self.prev_state=None  # So that deepcopy doesn't go beserk
        for item in self.floors[self.elevator_level]:
            for new_level in range(max(1,self.elevator_level-1),min(5,self.elevator_level+2)):
                new=deepcopy(self)
                new.elevator_level=new_level
                new.floors[self.elevator_level].remove(item)
                new.floors[new_level].add(item)
                if new.validate_state() and repr(new) not in self.past_states:
                    self.past_states.add(repr(new))
                    new.prev_state=self
                    new.steps+=1
                    yield new
        for items in combinations(tuple(self.floors[self.elevator_level]),r=2):
            for new_level in range(max(1,self.elevator_level-1),min(5,self.elevator_level+2)):
                new=deepcopy(self)
                new.elevator_level=new_level
                new.floors[self.elevator_level]-=set(items)
                new.floors[new_level]|=set(items)
                if new.validate_state() and repr(new) not in self.past_states:
                    self.past_states.add(repr(new))
                    new.prev_state=self
                    new.steps+=1
                    yield new
        self.prev_state=prev_state

def print_previous_states(state):
    if state is None: return
    print_previous_states(state.prev_state)
    print()
    print(state)

init_state_tuple=(
    ('SrG','SrM','PuG','PuM'),
    ('TmG','TmM','RuG','RuM','CmG','CmM'),
    ('TmM',),
    (),
)

# Sample data
#init_state_tuple=(
    #('HM','LM'),
    #('HG',),
    #('LG',),
    #()
#)

init_state=State()
init_state.past_states.add(repr(init_state))
target_state=State()
target_state.elevator_level=4
for i,tupl in enumerate(init_state_tuple):
    init_state.floors[i+1]=set(tupl)
    target_state.floors[4]|=set(tupl)

################# PART 2 #################
#part2_floor1 = {'ElG','ElM','Li2G','Li2M'}
#init_state.floors[1]|=part2_floor1
#target_state.floors[4]|=part2_floor1
##########################################

q=deque()
q.append(init_state)
max_step=0
while size:=len(q):
    if size%1000==0:
        print('qsize',size,'max_step',max_step,flush=True)
    s=q.popleft()
    #print(s)
    if s==target_state:
        print('Part 1:',s)
        break
    for ns in s.new_states():
        max_step=ns.steps
        q.append(ns)
# Part 1: 37
# Part 2: 61

print_previous_states(s)