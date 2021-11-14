from Intcode import Intcode,load_intcode
from time import sleep
from numpy import sign
from os import system, name
CLEAR = 'cls' if name=='nt' else 'clear'
VISUAL = True

class Arcade(Intcode):
    code = load_intcode('13.txt')
    TILE_ID = " █#―O"
    def __init__(self):
        super().__init__(self.code)
        self.screen = {}
        self.output_mode = 0  # 0:x, 1:y, 2:t
        self.x=None
        self.y=None
        self.max_x = 0
        self.max_y = 0
        self.px=0  # Paddle x
        self.py=0  # Paddle y
        self.bx=0  # Ball x
        self.by=0  # Ball y
        self.pbx=0  # Previous ball x
        self.pby=0  # Previous ball y
        self.projex=0  # Projected x intercept - where the paddle needs to be
        self.j=0  # Joystick
    def find_projex(s):
        dy=s.py-s.by-1
        dx=dy*(s.bx-s.pbx)
        s.projex=s.bx+dx
    def set_joystick(s):
        if s.pby<s.by: # Heading down
            s.find_projex()
            if s.px==s.projex:
                j=0
            else:
                j=sign(s.projex-s.px)
        else:
            j=sign(s.bx-s.px)
        s.j=j
    def _3(s):
        """Input, except it is a joystick"""
        s.set_joystick()
        s._code[s.par(1)]=s.j
        s._i+=2
    def _4(s):
        """Output, except it saves it as x,y,t"""
        o=s._code[s.par(1)]
        if s.output_mode==0:
            s.x=o
        elif s.output_mode==1:
            s.y=o
        elif s.output_mode==2:
            s.screen[(s.x,s.y)]=o
            #------------------------#
            if s.x>s.max_x:s.max_x=s.x
            if s.y>s.max_y:s.max_y=s.y
            #------------------------#
            if o==3:  # Paddle
                s.px = s.x
                s.py = s.y  # Should be constant?
            elif o==4:  # Ball
                s.pbx,s.pby=s.bx,s.by
                s.bx,s.by=s.x,s.y
                if VISUAL:
                    s.display()
        else:
            1/0  # Should never get here!
        s.output_mode+=1
        s.output_mode%=3
        s._i+=2
    def display(s):
        out="\n".join("".join(s.TILE_ID[s.screen.get((x,y),0)]
                              for x in range(0,s.max_x+1))
                      for y in range(0,s.max_y+1))+f"\nScore: {s.screen.get((-1,0),0)}"
        system(CLEAR)
        print(out, flush=True)
        sleep(.01)

a = Arcade()
a.run()
if VISUAL:
    a.display()
    sleep(3)

b = Arcade()
b._code[0]=2
b.run()
if VISUAL:
    b.display()

print("Part 1:",len([0 for _ in a.screen.values() if _==2]))
print("Part 2:",b.screen.get((-1,0),0))