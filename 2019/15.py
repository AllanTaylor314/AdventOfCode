from Intcode import Intcode,load_intcode
from time import sleep
from random import choice
from os import system,name
VERBOSE=True
CLEAR = 'cls' if name=='nt' else 'clear'

class RepairDroid(Intcode):
    CODE = load_intcode('15.txt')
    CHAR = "█ OX?".__getitem__
    BACK = [0,2,1,4,3].__getitem__
    def __init__(self):
        super().__init__(self.CODE)
        del self._out_q
        del self._in_q
        self.map = {(0,0):3}
        self.map_paths = {(0,0):""}
        self.map_next_steps = {(0,0):iter((1,2,3,4))}
        self.x=0  # Current coordinates
        self.y=0
        self.min_x=-21  # Range for printing
        self.max_x=19  # Set here for consistent size printing
        self.min_y=-19  # Though they could all be initialised to zero
        self.max_y=21  # And the would automatically change to fit
        self.cmd=0  # Most recent direction
        self.ox=0  # Oxygen coordinates
        self.oy=0
    def plot(s,status):
        """Add useful info to map and update x,y"""
        prev_coord = s.x,s.y
        new_coord = s.new_xy()
        if new_coord!=(0,0):  # Leave (0,0) as the origin (3)
            s.map[new_coord]=status
        if status: # Hallway (1) or Oxygen (2)
            new_path = s.reduce(s.map_paths[prev_coord]+" nswe"[s.cmd])
            if new_coord not in s.map_paths or len(new_path)<len(s.map_paths[new_coord]):
                s.map_paths[new_coord]=new_path
            if new_coord not in s.map_next_steps:
                b=s.BACK(s.cmd)  # Direction back to the tile we were just at
                s.map_next_steps[new_coord]=iter(tuple({1,2,3,4}-{b})+(b,))
            s.x,s.y=new_coord  # Move to new position
            if status==2:
                s.ox,s.oy=new_coord
        if VERBOSE:
            s.display()
            sleep(0.01)

    def new_xy(s):
        """Using the most recent command, find the new location (or wall)"""
        x,y=s.x,s.y
        if s.cmd == 1:
            y=s.y+1
            if y>s.max_y:s.max_y=y
        elif s.cmd == 2:
            y=s.y-1
            if y<s.min_y:s.min_y=y
        elif s.cmd == 3:
            x=s.x-1
            if x<s.min_x:s.min_x=x
        elif s.cmd == 4:
            x=s.x+1
            if x>s.max_x:s.max_x=x
        else:
            1/0 # Wut?
        return x,y

    def display(s, current=False):
        """Print the map as a pretty picture"""
        out=""
        for y in range(s.max_y+1,s.min_y-2,-1):
            for x in range(s.min_x-1,s.max_x+2):
                if current and (x,y)==(s.x,s.y):
                    out+='@'
                else:
                    out+=s.CHAR(s.map.get((x,y),-1))
            out+="\n"
        system(CLEAR)
        print(out,flush=True)
    
    @staticmethod
    def reduce(path):
        """Reduce no-ops from a path"""
        l = len(path)+1
        while len(path)!=l:
            l=len(path)
            for pair in ("ns","sn","ew","we"):
                path=path.replace(pair,"")
        return path
    
    def oxygen_distance(s,xy):
        if (s.ox,s.oy)==(0,0):
            raise ValueError('Oxygen not found yet')
        # Reverse the path to the oxygen
        path = s.map_paths[(s.ox,s.oy)][::-1]
        path = path.translate(str.maketrans('nsew','snwe'))
        # Add to path from origin
        path+=s.map_paths[xy]
        # Reduce
        path=s.reduce(path)
        # Measure
        return len(path)
    
    def _3(s):
        try:
            s.cmd=next(s.map_next_steps[(s.x,s.y)])
        except StopIteration:
            s.awaiting_input=True  # Effectively a break
            return
        s._code[s.par(1)]=s.cmd
        s._i+=2

    def _4(s):
        s.plot(s._code[s.par(1)])
        s._i+=2

droid = RepairDroid()
droid.run()
droid.display()
print(f'Part 1: {len(droid.map_paths[(droid.ox,droid.oy)])} @ {(droid.ox,droid.oy)}')

"""
???????????????????????????????????????????
??███?███?███████?███████?█████?███?█████??
?█   █   █       █       █     █   █     █?
?█ █ █ █ █ █ █████ █ █ ███ ███ █ █ █ █ █ █?
?█ █   █   █   █   █ █ █   █ █   █ █ █ █ █?
?█ ████?██████ █ ███ ███ ███ █████ █ █ █ █?
?█ █   █     █ █   █     █       █ █ █ █ █?
?█ █ █ █ ███ █ ███ ███████ █████ █ █ █ ██??
?█   █   █   █     █     █ █     █ █ █   █?
??███?████ ██?██████ █ █ ███ █████ █ ███ █?
?█   █   █ █ █   █   █ █     █     █   █ █?
?█ █ ███ █ █ █ █ █ ███ █████ █ █ ███ ███ █?
?█ █     █ █   █     █   █   █ █ █   █   █?
?█ █ █████ █ ███████████ █ ███ ███ ███ █ █?
?█ █ █   █ █       █     █   █     █ █ █ █?
?█ ███ █ █ █ ███████ ███ █████ █████ █ ██??
?█     █   █ █       █   █   █   █   █   █?
?█ ███████ ███ █████ █████ █ ███ █ █ ███ █?
?█   █   █     █     █     █   █   █ █   █?
??██ █ █ █████████████ ███████ ███ ███ █ █?
?█   █ █         █     █ █     █   █   █ █?
??████ █████████ █ █████ █ █████ ███ ████??
?█   █   █     █ █ █  X█ █   █ █   █     █?
?█ █ ███ █ ███ █ █ █ ███ ███ █ █ ███████ █?
?█ █     █   █     █ █     █ █   █     █ █?
?█ ███████ ███████ █ █ ███ █ █████ ███ █ █?
?█ █   █   █     █ █ █ █ █   █     █ █   █?
?█ █ █ █████ ███ ███ █ █ █████ █████ ███ █?
?█ █ █ █   █   █   █ █ █       █   █     █?
?█ █ █ █ █ ███ ███ █ █ █ █████ █ █ █ ████??
?█   █   █     █ █   █ █ █   █ █ █ █ █   █?
??███████?██████ █████ ███ █ █ █ █ █ █ █ █?
?█       █         █ █   █ █   █ █ █ █ █ █?
?█ ███ █ █████ ███ █ ███ █ █████ █ █ █ █ █?
?█ █   █       █ █     █   █     █ █ █ █ █?
?█ █ ███████████ █████ █████ █████ █ ███ █?
?█ █ █O                  █   █   █ █ █   █?
?█ █ ███████████████████ █ █ █ █ ███ █ ██??
?█ █   █         █     █ █ █   █     █   █?
?█ ███ █ ███████ █ ███ ███ █████████████ █?
?█   █         █     █                   █?
??███?█████████?█████?███████████████████??
???????????????????????????????????????????
"""
running_max = 0
for xy,status in droid.map.items():
    if status:
        dist = droid.oxygen_distance(xy)
        if dist>running_max:
            running_max=dist
            max_coord=xy
print(f"Part 2: {running_max} @ {max_coord}")