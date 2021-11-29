DIRECTIONS="^>v<"
DX_DY=[(0,-1),(1,0),(0,1),(-1,0)]
class SporificaVirus:
    def __init__(self, infected):
        self.infected=infected
        self.d=0
        self.x=0
        self.y=0
        self.infection_count=0
    def __repr__(s):
        return f"[Virus @ ({s.x}, {s.y}, {DIRECTIONS[s.d]}); {len(s.infected)} infected nodes]"
    def run(self):
        xy=self.x,self.y
        if xy in self.infected:
            self.d=(self.d+1)%4  # Turn right
            self.infected.discard(xy)  # clean
        else:
            self.d=(self.d-1)%4  # Turn left
            self.infected.add(xy)  # infect
            self.infection_count+=1
        dx,dy=DX_DY[self.d]
        self.x+=dx
        self.y+=dy

with open('22.txt') as file:
    data=file.read()
init = [list(l) for l in data.splitlines()]

INFECTED=set()
xo,yo = len(init[0])//2,len(init)//2
for y,row in enumerate(init):
    for x,v in enumerate(row):
        if v=='#':
            INFECTED.add((x-xo,y-yo))

virus = SporificaVirus(INFECTED.copy())
for _ in range(10000):
    virus.run()
print('Part 1:',virus.infection_count)

class SporificaVirusV2:
    def __init__(self, infected):
        self.infected={xy:2 for xy in infected}
        self.d=0
        self.x=0
        self.y=0
        self.infection_count=0
    def __repr__(s):
        return f"[Virus V2 @ ({s.x}, {s.y}, {DIRECTIONS[s.d]})]"
    def run(self):
        xy=self.x,self.y
        if xy not in self.infected:
            self.infected[xy]=0
        # Turn
        self.d+=self.infected[xy]-1
        self.d%=4
        # Change infection level
        self.infected[xy]=(self.infected[xy]+1)%4
        # Increment infection count if node is now infected
        if self.infected[xy]==2: self.infection_count+=1
        dx,dy=DX_DY[self.d]
        # Move
        self.x+=dx
        self.y+=dy
virus2 = SporificaVirusV2(INFECTED)
for _ in range(10000000):
    virus2.run()
print('Part 2:',virus2.infection_count)