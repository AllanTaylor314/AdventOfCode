from queue import Queue
from itertools import permutations
global_out = []

class Amplifier():
    def __init__(self, code: list[int], phase: int):
        self._queue = Queue()
        self._queue.put(phase)
        self.phase = phase
        self.next_amp = None
        self._code = code.copy()
        self.halted = False
        self.awaiting_input = False
        self._i = 0
    def put(self, value: int):
        self._queue.put(value)
        self.awaiting_input = False
    def run(self):
        ri=self._code
        i=self._i
        while i < len(ri):
            op_par = ri[i]
            op = op_par % 100
            par = [0] * 10 + list(map(int, str(op_par // 100)))
            par.reverse()
            if op == 1:
                ri[ri[i + 3]] = (ri[i + 1] if par[0] else ri[ri[i + 1]]) + (ri[i + 2] if par[1] else ri[ri[i + 2]])
                i += 4
            elif op == 2:
                ri[ri[i + 3]] = (ri[i + 1] if par[0] else ri[ri[i + 1]]) * (ri[i + 2] if par[1] else ri[ri[i + 2]])
                i += 4
            elif op == 3:
                if self._queue.empty():
                    self.awaiting_input = True
                    self._i=i
                    return
                ri[ri[i + 1]] = self._queue.get_nowait()
                i += 2
            elif op == 4:
                if self.next_amp is None or self.next_amp.halted:
                    global_out.append(ri[ri[i + 1]])
                self.next_amp.put(ri[ri[i + 1]])
                i += 2
            elif op == 5:
                if (ri[i + 1] if par[0] else ri[ri[i + 1]]):
                    i = (ri[i + 2] if par[1] else ri[ri[i + 2]])
                else:
                    i += 3
            elif op == 6:
                if (ri[i + 1] if par[0] else ri[ri[i + 1]]) == 0:
                    i = (ri[i + 2] if par[1] else ri[ri[i + 2]])
                else:
                    i += 3
            elif op == 7:
                ri[ri[i + 3]] = int((ri[i + 1] if par[0] else ri[ri[i + 1]]) < (ri[i + 2] if par[1] else ri[ri[i + 2]]))
                i += 4
            elif op == 8:
                ri[ri[i + 3]] = int((ri[i + 1] if par[0] else ri[ri[i + 1]]) == (ri[i + 2] if par[1] else ri[ri[i + 2]]))
                i += 4
            elif op == 99:
                self.halted = True
                self._i=i
                return
            else:
                print('?')
                i += 1


with open("07.txt") as file:
    raw_data = file.read()
code = list(map(int, raw_data.split(',')))

for a, b, c, d, e in permutations(range(5,10)):
    A=Amplifier(code,a)
    B=Amplifier(code,b)
    C=Amplifier(code,c)
    D=Amplifier(code,d)
    E=Amplifier(code,e)
    A.next_amp=B
    B.next_amp=C
    C.next_amp=D
    D.next_amp=E
    E.next_amp=A
    A.put(0)
    while not all([A.halted,B.halted,C.halted,D.halted,E.halted]):
        A.run()
        B.run()
        C.run()
        D.run()
        E.run()
        if all([A.awaiting_input,B.awaiting_input,C.awaiting_input,D.awaiting_input,E.awaiting_input]):
            print('All awaiting')  # Should never happen

print('Part 2:',max(global_out))
