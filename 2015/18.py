LIVE = "#"
DEAD = "."

class Conway:
    def __init__(self, start):
        self._board = [list(_) for _ in start.strip().splitlines()]
        self._past_states = set()
        self.repeat=False
    def __str__(self):
        return "\n".join("".join(_) for _ in self._board)
    def evolve(self):
        b=self._board
        new = []
        max_y = len(b)
        max_x = len(b[0])
        for y in range(max_y):
            new.append([])
            for x in range(max_x):
                live_neighbours = (
                 int(x!=0 and b[y][x-1]==LIVE)
                +int(x+1!=max_x and b[y][x+1]==LIVE)
                +int(y!=0 and b[y-1][x]==LIVE)
                +int(y+1!=max_y and b[y+1][x]==LIVE)
                +int(y!=0 and x!=0 and b[y-1][x-1]==LIVE)
                +int(y!=0 and x+1!=max_x and b[y-1][x+1]==LIVE)
                +int(y+1!=max_y and x+1!=max_x and b[y+1][x+1]==LIVE)
                +int(y+1!=max_y and x!=0 and b[y+1][x-1]==LIVE)
                )
                if (live_neighbours==3) or (b[y][x]==LIVE and live_neighbours==2):
                    new[y].append(LIVE)
                else:
                    new[y].append(DEAD)
        self._board=new
        if str(self) in self._past_states:
            self.repeat=True
        self._past_states.add(str(self))
    def count_on(self):
        return str(self).count(LIVE)

class BrokenConway(Conway):
    """Like Conway's Game of Life, except the 4 corners are always on"""
    def __init__(self, start):
        super().__init__(start)
        b=self._board
        max_y = len(b)-1
        max_x = len(b[0])-1
        b[0][0]=LIVE
        b[0][max_x]=LIVE
        b[max_y][0]=LIVE
        b[max_y][max_x]=LIVE
    def evolve(self):
        super().evolve()
        b=self._board
        max_y = len(b)-1
        max_x = len(b[0])-1
        b[0][0]=LIVE
        b[0][max_x]=LIVE
        b[max_y][0]=LIVE
        b[max_y][max_x]=LIVE

with open('18.txt') as file:
    start = file.read()
grid = Conway(start)
for _ in range(100):
    grid.evolve()
print('Part 1:',grid.count_on())

grid2 = BrokenConway(start)
for _ in range(100):
    grid2.evolve()
print('Part 2:',grid2.count_on())