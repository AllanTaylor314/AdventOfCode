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
                live_neighbours = 0
                if x!=0 and b[y][x-1]==LIVE:
                    live_neighbours+=1
                if x+1!=max_x and b[y][x+1]==LIVE:
                    live_neighbours+=1
                if y!=0 and b[y-1][x]==LIVE:
                    live_neighbours+=1
                if y+1!=max_y and b[y+1][x]==LIVE:
                    live_neighbours+=1
                if (live_neighbours==1) or (b[y][x]==DEAD and live_neighbours==2):
                    new[y].append(LIVE)
                else:
                    new[y].append(DEAD)
        self._board=new
        if str(self) in self._past_states:
            self.repeat=True
        self._past_states.add(str(self))
    def biodiversity(self):
        return int("".join("".join(_) for _ in self._board).replace(LIVE,'1').replace(DEAD,'0')[::-1],base=2)

with open('24.txt') as file:
    start = file.read()
eris = Conway(start)
while not eris.repeat:
    eris.evolve()
print("Part 1:",eris.biodiversity())