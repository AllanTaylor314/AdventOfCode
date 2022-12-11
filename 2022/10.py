class CRT:
    def __init__(self, x=1, width=40, height=6, chars=" █", char_width=2):
        self._x = x
        self.width = 40
        self.height = 6
        self._chars = chars
        self._char_width = char_width
        
        self._clock = 0
        self._clocks_that_matter = range(width//2,width*height,width)
        self.part1 = 0
        self.part2 = ""

    def _do_clock(self):
        self.part2+=(self._chars[abs(self._clock%self.width-self._x)<=1]*self._char_width)
        self._clock+=1
        if self._clock in self._clocks_that_matter:self.part1+=self._x*self._clock
        if self._clock%self.width==0:self.part2+="\n"

    def run(self,steps):
        for step in steps:
            if step=="noop":
                self._do_clock()
            else:
                self._do_clock()
                self._do_clock()
                self._x+=int(step.split()[1])


with open("10.txt") as file:
    lines = file.read().splitlines()
crt = CRT()
crt.run(lines)
print("Part 1:",crt.part1)
print("Part 2:\n"+crt.part2)
