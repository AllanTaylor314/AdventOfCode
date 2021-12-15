"""
Full Intcode computer
"""
from queue import Queue

def load_intcode(filename):
    with open(filename) as file:
        return list(map(int,file.read().split(',')))

class MemDict(dict):
    """A subclass of dict that returns 0 for any undefined indices"""
    def __init__(self,*args):
        super().__init__(*args)
    def __getitem__(self, i):
        return self.get(i,0)
    def __repr__(self):
        return super().__repr__()

class Intcode:
    class InvalidOpcodeException(Exception):
        pass
    def __init__(self, code):
        self._code = MemDict(enumerate(code))
        self._i = 0
        self.rel_base = 0
        self._in_q = Queue()
        self._out_q = Queue()
        self.halted = False
        self.awaiting_input = False
    def input(self, data):
        self.awaiting_input = False
        self._in_q.put(data)
    def has_output(self):
        return not self._out_q.empty()
    def output(self):
        if self._out_q.empty():
            raise IndexError
        return self._out_q.get_nowait()
    
    def par(s,o):
        """Index of the parameter for item at o(ffset)"""
        div = 10*10**o
        mod = div*10
        p = s._code[s._i]%mod//div
        if p==0: # Position Mode
            return s._code[s._i+o]
        if p==1: # Immediate Mode
            return s._i+o
        if p==2: # Relative Mode
            return s.rel_base+s._code[s._i+o]
    
    def _1(s):
        """Add"""
        s._code[s.par(3)]=s._code[s.par(1)]+s._code[s.par(2)]
        s._i+=4
    def _2(s):
        """Mul"""
        s._code[s.par(3)]=s._code[s.par(1)]*s._code[s.par(2)]
        s._i+=4
    def _3(s):
        """Input"""
        if s._in_q.empty():
            s.awaiting_input=True
            return
        s._code[s.par(1)]=s._in_q.get_nowait()
        s._i+=2
    def _4(s):
        """Output"""
        s._out_q.put(s._code[s.par(1)])
        #print(s._code[s.par(1)])
        s._i+=2
    def _5(s):
        """Jump if True"""
        if s._code[s.par(1)]:
            s._i = s._code[s.par(2)]
        else:
            s._i+=3
    def _6(s):
        """Jump if False"""
        if s._code[s.par(1)]==0:
            s._i = s._code[s.par(2)]
        else:
            s._i+=3
    def _7(s):
        """Less than"""
        s._code[s.par(3)]=int(s._code[s.par(1)]<s._code[s.par(2)])
        s._i+=4
    def _8(s):
        """Equal"""
        s._code[s.par(3)]=int(s._code[s.par(1)]==s._code[s.par(2)])
        s._i+=4
    def _9(s):
        """Update rel_base"""
        s.rel_base+=s._code[s.par(1)]
        s._i+=2
    def _99(s):
        s.halted=True
    def run(s):
        c=s._code
        while s._i<len(c) and not s.halted and not s.awaiting_input:
            try:
                getattr(s,f"_{s._code[s._i]%100}")()
            except AttributeError:
                raise s.InvalidOpcodeException(f"'{s._code[s._i]}' is an invalid op")
    def ascii_out(s):
        out=''
        while s.has_output():
            out+=chr(s.output())
        return out


def test(*code):
    ic = Intcode(list(code))
    while not ic.halted:
        ic.run()
        if ic.awaiting_input:
            ic.input(int(input('$')))
    while ic.has_output():
        print(ic.output())


if __name__=="__main__":
#-------------------------Day 2-----------------------
    ic2_code = load_intcode('02.txt')
    ic2 = Intcode(ic2_code)
    ic2._code[1]=12
    ic2._code[2]=2
    ic2.run()
    print('2.1:',ic2._code[0])

    for noun in range(100):
        for verb in range(100):
            ic2 = Intcode(ic2_code)
            ic2._code[1]=noun
            ic2._code[2]=verb
            ic2.run()
            if ic2._code[0]==19690720:
                print('2.2:',100*noun+verb)
                break

    del ic2_code
    del ic2


#-------------------------Day 5-----------------------
    ic5_code = load_intcode('05.txt')
    ic5 = Intcode(ic5_code)
    ic5.input(1)
    ic5.run()
    print('5.1 - 0s followed by diagnostic code')
    while ic5.has_output():
        print(ic5.output())

    ic5 = Intcode(ic5_code)
    ic5.input(5)
    ic5.run()
    print('5.2:',ic5.output())

    del ic5_code
    del ic5


#-------------------------Day 9-----------------------
    ic9_code = load_intcode('09.txt')
    ic9=Intcode(ic9_code)
    ic9.input(1)
    ic9.run()
    print('9.1 - diagnostic test')
    while ic9.has_output(): # Should only be one code
        print(ic9.output())

    ic9=Intcode(ic9_code)
    ic9.input(2)
    ic9.run()
    print('9.2 - Coordinates:',ic9.output())

    del ic9_code
    del ic9


#-------------------------Tests-----------------------
    ict1_code = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    ict1=Intcode(ict1_code)
    ict1.run()
    for n in ict1_code:
        assert ict1.output()==n
    assert not ict1.has_output()
    del ict1_code
    del ict1

    ict2_code = [1102,34915192,34915192,7,4,7,99,0]
    ict2=Intcode(ict2_code)
    ict2.run()
    assert ict2.output()==34915192*34915192
    assert not ict2.has_output()
    del ict2_code
    del ict2

    ict3_code = [104,1125899906842624,99]
    ict3=Intcode(ict3_code)
    ict3.run()
    assert ict3.output()==ict3_code[1]
    assert not ict3.has_output()
    del ict3_code
    del ict3