ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Step:
    done=set()
    created={}
    def __init__(self, letter):
        if letter not in ALPHABET:
            letter_not_in_ALPHABET = f"The character '{letter}' is not a valid step"
            raise ValueError(letter_not_in_ALPHABET)
        self.letter = letter
        self.duration = ord(letter)-4
        self.created[letter]=self
    def dec(self):
        self.duration-=1
        if self.duration==0:
            self.done.add(self.letter)
    def is_done(self):
        return self.duration<=0
    def __repr__(self):
        return f"{self.letter} ({self.duration})"
    @classmethod
    def next_steps(cls):
        global reqs
        return sorted([a for a,b in reqs.items()
                       if a not in cls.created and
                       not b-cls.done])

with open('07.txt') as file:
    rules = file.read().splitlines()
reqs = {_:set() for _ in ALPHABET}
for line in rules:
    _,req,*_,step,_,_=line.split()
    reqs[step].add(req)

t=0
w=[None]*5
while len(Step.done)<len(ALPHABET):
    next_steps = Step.next_steps()
    while next_steps:
        try:
            ind = w.index(None)
        except ValueError:
            break  # No free workers
        else:
            w[ind]=Step(next_steps.pop(0))
    print(f"{t:3d}",end='')
    for s in w:
        if s is not None:
            print(f'   {repr(s):<8}',end='')
            s.dec()
        else:
            print('     .     ',end='')
    for i in range(len(w)):
        if w[i] is not None and w[i].is_done():
            w[i]=None
    print("".join(sorted(list(Step.done))))
    t+=1

print('Part 2:',t)
# Part 2: 991