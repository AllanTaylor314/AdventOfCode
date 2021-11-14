from Intcode import Intcode,load_intcode

class HullBot(Intcode):
    def __init__(self, code):
        super().__init__(code)
        self.x = 0
        self.y = 0
        self.d = 0
        self.out_setting = True
        self.panels = {}
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0
    def _3(s):
        """Input, except it is a 'camera'"""
        s._code[s.par(1)]=s.panels.get((s.x,s.y),0)
        s._i+=2
    def _4(s):
        """Output, except it turns and paints"""
        if s.out_setting:
            s.panels[(s.x,s.y)]=s._code[s.par(1)]
        else:
            if s._code[s.par(1)]:
                s.d-=1
            else:
                s.d+=1
            s.d%=4
            s._move()
        s.out_setting=not s.out_setting
        s._i+=2
    def _move(s):
        """    0
        ^y   3   1
        +->x   2
        """
        if s.d%2:
            s.x+=-1 if s.d//2 else 1
        else:
            s.y+=-1 if s.d//2 else 1
        
        if s.x<s.min_x:s.min_x=s.x
        if s.y<s.min_y:s.min_y=s.y
        if s.x>s.max_x:s.max_x=s.x
        if s.y>s.max_y:s.max_y=s.y
    def display(s):
        for y in range(s.max_y,s.min_y-1,-1):  # y is up, lines come down
            for x in range(s.max_x,s.min_x-1,-1):  # and the x is backwards too
                print(" #"[s.panels.get((x,y),0)],end="")
            print()

ic11_code = load_intcode('11.txt')
bot = HullBot(ic11_code)
bot.run()
print('Part 1:',len(bot.panels))


bot = HullBot(ic11_code)
bot.panels[(0,0)]=1
bot.run()
bot.display()