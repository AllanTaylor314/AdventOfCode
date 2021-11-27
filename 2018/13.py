DIRS = '^>v<'
CORNER_RULES = {
    ('/', 0):1,
    ('/', 1):0,
    ('/', 2):3,
    ('/', 3):2,
    ('\\',0):3,
    ('\\',1):2,
    ('\\',2):1,
    ('\\',3):0,
}

class Cart:
    class CrashException(Exception):
        pass
    def __init__(self, yx, d):
        self.y,self.x = yx
        self.d = DIRS.index(d)
        self._int_turn = 0  # left, straight, right = 0,1,2 (%3)
        self.exists=True
    def step_forward(self):
        if not self.exists: return
        global intersections, corners, mine_map, cart_locs
        del cart_locs[self.y,self.x]
        if self.d==0:
            self.y-=1
        elif self.d==1:
            self.x+=1
        elif self.d==2:
            self.y+=1
        elif self.d==3:
            self.x-=1
        else: raise ValueError(f'{self.d} not in [0,1,2,3]')
        coord = (self.y,self.x)
        if coord in corners:
            self.d=CORNER_RULES[mine_map[coord],self.d]
        elif coord in intersections:
            self.d+=self._int_turn-1
            self.d%=4
            self._int_turn+=1
            self._int_turn%=3
        if coord in cart_locs:
            self.exists=False
            cart_locs[coord].exists=False
            del cart_locs[coord]
            raise Cart.CrashException(f'Crash at X,Y=({self.x},{self.y})!')
        cart_locs[coord]=self
    def __repr__(self):
        return f"|| yx={self.y,self.x}, d='{DIRS[self.d]}' ||"
    def __lt__(self, elf):
        return (self.y,self.x)<(elf.y,elf.x)

with open('13.txt') as file:
    data = file.read()
mine_map = {}
cart_locs = {}
intersections = set()
corners = set()
for y,line in enumerate(data.splitlines()):
    for x,char in enumerate(line):
        mine_map[(y,x)] = char  # y is first so sorted tuples act correctly
        if char in DIRS:
            cart_locs[y,x]=Cart((y,x),char)
            if char in '^v':
                mine_map[y,x]='|'
            else:
                mine_map[y,x]='-'
        elif char=='+': intersections.add((y,x))
        elif char in '\\/': corners.add((y,x))

cart_list = list(cart_locs.values())

part1=True
tick=0
while len(cart_list)>1:
    cart_list.sort()
    for cart in cart_list:
        try:
            cart.step_forward()
        except Cart.CrashException as e:
            if part1:print('Part 1:',e);part1=False
    cart_list = [c for c in cart_list if c.exists]
    tick+=1
cart ,= cart_list
print('Part 2:', f"{cart.x},{cart.y}")