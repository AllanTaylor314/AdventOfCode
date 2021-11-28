from time import perf_counter
part1=True
r3_vals = {}

class Computer:
    class InfiniteLoop(Exception):pass
    def __init__(self, program, ip=5, r0=0):
        self.reg = [0]*6
        self.reg[0]=r0
        self.ip=ip
        self.r0=r0
        self.program=program
        self.past_states=set()
        self.steps=0
    def __getitem__(self,*args):
        return self.reg.__getitem__(*args)
    def __setitem__(self,*args):
        return self.reg.__setitem__(*args)
    def addr(reg,a,b,c): reg[c]=reg[a]+reg[b]
    def addi(reg,a,b,c): reg[c]=reg[a]+b
    def mulr(reg,a,b,c): reg[c]=reg[a]*reg[b]
    def muli(reg,a,b,c): reg[c]=reg[a]*b
    def banr(reg,a,b,c): reg[c]=reg[a]&reg[b]
    def bani(reg,a,b,c): reg[c]=reg[a]&b
    def borr(reg,a,b,c): reg[c]=reg[a]|reg[b]
    def bori(reg,a,b,c): reg[c]=reg[a]|b
    def setr(reg,a,b,c): reg[c]=reg[a]
    def seti(reg,a,b,c): reg[c]=a
    def gtir(reg,a,b,c): reg[c]=int(a>reg[b])
    def gtri(reg,a,b,c): reg[c]=int(reg[a]>b)
    def gtrr(reg,a,b,c): reg[c]=int(reg[a]>reg[b])
    def eqir(reg,a,b,c): reg[c]=int(a==reg[b])
    def eqri(reg,a,b,c): reg[c]=int(reg[a]==b)
    def eqrr(reg,a,b,c):
        global part1, r3_vals
        if part1:
            print(f"Part 1: {reg[3]}")
            part1=False
        if reg[3] not in r3_vals:
            r3_vals[reg[3]]=reg.steps
            print(f"{reg.steps:11d}: r3={reg[3]}")
        else:
            print(f"r3={reg[3]} appeared at {r3_vals[reg[3]]} (steps = {self.steps}")
        reg[c]=int(reg[a]==reg[b])
    def operate(self,ops):
        op,a,b,c=ops
        getattr(self,op)(a,b,c)
        self.steps+=1
    def run(self):
        while 0<=self[self.ip]<len(self.program):
            state=tuple(self.reg)
            if state in self.past_states:
                raise InfiniteLoop
            self.past_states.add(state)
            self.operate(program[self[self.ip]])
            self[self.ip]+=1
        return self[0]
    def step(self):
        state=tuple(self.reg)
        #print(state)
        if state in self.past_states:
            raise InfiniteLoop
        self.past_states.add(state)
        self.operate(program[self[self.ip]])
        self[self.ip]+=1
        self.steps+=1
        return 0<=self[self.ip]<len(self.program)

with open('21.txt') as file:
    data = file.read()

header,*lines = data.splitlines()
ip = int(header.split()[1])
program = []
for line in lines:
    op,*pars=line.split()
    program.append([op]+list(map(int,pars)))

computer = Computer(program, ip=ip)#, r0=6132825)
computer.run()

# Part 2
# 11338674 too high
# 2189213 too low
# 8307757 (Solved using 21c.py)