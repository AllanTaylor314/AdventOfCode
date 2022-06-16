from itertools import permutations
from Intcode import Intcode,load_intcode

CODE=load_intcode('07.txt')

class Amplifier(Intcode):
    def __init__(self,phase,next_amp=None):
        super().__init__(CODE)
        self.next_amp=next_amp
        self._in_q.append(phase)
    def _4(s):
        if s.next_amp is None or s.next_amp.halted:
            s._out_q.append(s._code[s.par(1)])
        else:
            s.next_amp.input(s._code[s.par(1)])
        s._i+=2

amp_out=[]
for a, b, c, d, e in permutations(range(5)):
    E=Amplifier(e)
    D=Amplifier(d,E)
    C=Amplifier(c,D)
    B=Amplifier(b,C)
    A=Amplifier(a,B)
    A.input(0)
    A.run()
    B.run()
    C.run()
    D.run()
    E.run()
    amp_out.append(E.output())
print("Part 1:", max(amp_out))

amp2_out=[]
for a, b, c, d, e in permutations(range(5,10)):
    A=Amplifier(a)
    B=Amplifier(b)
    C=Amplifier(c)
    D=Amplifier(d)
    E=Amplifier(e)
    A.next_amp=B
    B.next_amp=C
    C.next_amp=D
    D.next_amp=E
    E.next_amp=A
    A.input(0)
    while not all([A.halted,B.halted,C.halted,D.halted,E.halted]):
        A.run()
        B.run()
        C.run()
        D.run()
        E.run()
        if all([A.awaiting_input,B.awaiting_input,C.awaiting_input,D.awaiting_input,E.awaiting_input]):
            print('All awaiting')  # Should never happen
    amp2_out.append(E.output())
print("Part 2:",max(amp2_out))