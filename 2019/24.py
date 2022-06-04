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

def adjacent(cell):
    """
      01234
    0 44444
    1 44844
    2 48+84
    3 44844
    4 44444
    """
    d,x,y = cell # depth and position
    contenders = {(d,x-1,y),(d,x+1,y),(d,x,y-1),(d,x,y+1)}
    if (d,2,2) in contenders:
        if x==2:
            ny = 4 if y==3 else 0
            new=[(d+1,nx,ny) for nx in range(5)]
        if y==2:
            nx = 4 if x==3 else 0
            new=[(d+1,nx,ny) for ny in range(5)]
        contenders.remove((d,2,2))
        contenders.update(new)
    for con in list(contenders):
        cd,cx,cy=con
        if cx==-1:
            contenders.discard(con)
            contenders.add((d-1,1,2))
        if cx==5:
            contenders.discard(con)
            contenders.add((d-1,3,2))
        if cy==-1:
            contenders.discard(con)
            contenders.add((d-1,2,1))
        if cy==5:
            contenders.discard(con)
            contenders.add((d-1,2,3))
    return contenders
def display(struct):
    mind = min(struct)[0]
    maxd = max(struct)[0]
    for d in range(mind,maxd+1):
        print(f'Depth {d}:')
        for y in range(5):
            for x in range(5):
                print(end='?' if x==2==y else'#' if (d,x,y) in struct else '.')
            print()

lives = {(0,x,y) for y,line in enumerate(start.splitlines()) for x,c in enumerate(line) if c==LIVE}
for i in range(200): # 200 mins
    print(f'Minute {i}: {len(lives)} bugs')
    to_check = set(lives)
    for l in lives:
        to_check.update(adjacent(l))
    new_lives = set()
    for cell in to_check:
        unlen = len(lives&adjacent(cell))
        if unlen==1 or (unlen==2 and cell not in lives):
            new_lives.add(cell)
    lives=new_lives
print('Part 2:',len(lives))
