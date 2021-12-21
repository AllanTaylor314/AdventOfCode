class Trajectory:
    def __init__(self,x0,y0):
        self.vx=self.x0=x0
        self.vy=self.y0=y0
        self.x=0
        self.y=0
        self.max_y=0
        self.vis_x=[0]
        self.vis_y=[0]
    def step(self):
        self.x+=self.vx
        self.y+=self.vy
        self.vy-=1
        if self.vx>0:self.vx-=1
        elif self.vx<0:self.vx+=1
        self.max_y=max(self.max_y,self.y)
        self.vis_x.append(self.x)
        self.vis_y.append(self.y)
    def in_range(self):
        global MIN_X,MAX_X,MIN_Y,MAX_Y
        return MIN_X<=self.x<=MAX_X and MIN_Y<=self.y<=MAX_Y
    def definitely_out_of_range(self):
        global MIN_X,MAX_X,MIN_Y,MAX_Y
        if self.vx>=0 and self.x>MAX_X:
            return True
        if self.vy<0 and self.y<MIN_Y:
            return True
        return False
    def run(self):
        while not self.definitely_out_of_range():
            self.step()
            if self.in_range():
                return True
        return False
    def __repr__(self):
        return f"<Trajectory({self.x0}, {self.y0}): max_y={self.max_y}>"

with open('17.txt') as file:
    data = file.read()
*t,x,y=data.split()
MIN_X,MAX_X=map(int,x.split('=')[1].strip(',').split('..'))
MIN_Y,MAX_Y=map(int,y.split('=')[1].strip(',').split('..'))

candidates=[]
for x in range(MAX_X+1):
    for y in range(MIN_Y,-MIN_Y):
        # Logic from Reddit for -MIN_Y upper bound:
        # If vy0 is +ve, at y=0, the vy=-vy0
        # Anything starting faster than -MIN_Y
        # will jump past the target box
        t=Trajectory(x,y)
        if t.run():
            candidates.append(t)

print('Part 1:',max(c.max_y for c in candidates))
print('Part 2:',len(candidates))

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
axes = plt.axes()
rect = Rectangle((MIN_X,MIN_Y),MAX_X-MIN_X,MAX_Y-MIN_Y)
axes.add_patch(rect)
for c in candidates:
    axes.plot(c.vis_x,c.vis_y)
