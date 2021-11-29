######### INPUT #########
CHECKSUM_STEPS = 12481997

class TuringMachine:
    def __init__(self):
        self.tape=set()
        self.state=self.A
        self.slot=0
    def A(self):
        if self.slot not in self.tape:
            self.tape.add(self.slot)
            self.slot+=1
            self.state=self.B
        else:
            self.tape.discard(self.slot)
            self.slot-=1
            self.state=self.C
    def B(self):
        if self.slot not in self.tape:
            self.tape.add(self.slot)
            self.slot-=1
            self.state=self.A
        else:
            self.tape.add(self.slot)
            self.slot+=1
            self.state=self.D
    def C(self):
        if self.slot not in self.tape:
            self.tape.discard(self.slot)
            self.slot-=1
            self.state=self.B
        else:
            self.tape.discard(self.slot)
            self.slot-=1
            self.state=self.E
    def D(self):
        if self.slot not in self.tape:
            self.tape.add(self.slot)
            self.slot+=1
            self.state=self.A
        else:
            self.tape.discard(self.slot)
            self.slot+=1
            self.state=self.B
    def E(self):
        if self.slot not in self.tape:
            self.tape.add(self.slot)
            self.slot-=1
            self.state=self.F
        else:
            self.tape.add(self.slot)
            self.slot-=1
            self.state=self.C
    def F(self):
        if self.slot not in self.tape:
            self.tape.add(self.slot)
            self.slot+=1
            self.state=self.D
        else:
            self.tape.add(self.slot)
            self.slot+=1
            self.state=self.A
    def run(self, diagnostic_checksum):
        for _ in range(diagnostic_checksum):
            self.state()
    def __repr__(self):
        return f"Turing({len(self.tape)} ones)"

cpu = TuringMachine()
cpu.run(CHECKSUM_STEPS)
print('Part 1:',len(cpu.tape))
