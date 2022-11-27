from Intcode import Intcode,load_intcode,deque

class NAT():
    X=None
    Y=None
    _Y=None
    _X=None
    @classmethod
    def append(cls,value):
        if cls.X is None and cls.Y is not None:
            print('Part 1:',value)
        cls.X=cls.Y
        cls.Y=value
    @classmethod
    def retransmit(cls):
        print('Retransmit',cls.X,cls.Y)
        if cls._Y is not None and cls._Y==cls.Y:
            print('Part 2:',cls.Y)
            return False
        NetworkedComputer.IP[0].append(cls.X)
        NetworkedComputer.IP[0].append(cls.Y)
        cls._X,cls._Y=cls.X,cls.Y
        return True


class NetworkedComputer(Intcode):
    CODE=load_intcode('23.txt')
    IP={255:NAT}
    IDLE=0
    def __init__(self,address):
        super().__init__(self.CODE)
        self.input(address)  # init with network address
        self.IP[address]=self._in_q  # Allows other computers to send packets
        self.out_buffer=[]  # Buffer output into sets of three
    def step(s):
        """Run a single step"""
        getattr(s,f"_{s._code[s._i]%100}")()
    def _3(s):
        """Read packet queue, or -1 if no queue"""
        if s._in_q:
            out=s._in_q.popleft()
            s.IDLE=0
        else:
            out=-1
            s.IDLE+=1
        s._code[s.par(1)]=out
        s._i+=2
    def _4(s):
        """Output packet. Write set of three values to buffer"""
        s.out_buffer.append(s._code[s.par(1)])
        if len(s.out_buffer)>=3:
            des,x,y,*s.out_buffer=s.out_buffer
            s.IP[des].append(x)
            s.IP[des].append(y)
        s._i+=2

def check_idle():
    """Check if all the computers have been idle for a while"""
    global computers
    return all((c.IDLE>1 for c in computers))

computers = [NetworkedComputer(i) for i in range(50)]
while True:
    for computer in computers:
        computer.step()
    if check_idle():
        if not NAT.retransmit(): break
        for c in computers: c.IDLE=0  # Reset IDLE counts
