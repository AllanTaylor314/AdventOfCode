PLOT=False
if PLOT:
    from mpl_toolkits import mplot3d
    import numpy as np
    import matplotlib.pyplot as plt

USE_TURTLE=False
if USE_TURTLE:
    from turtle import *

def sign(a):return 1 if a>0 else -1 if a<0 else 0

class Moon:
    def __init__(self, x, y, z):
        self.x,self.y,self.z=x,y,z
        self.vx,self.vy,self.vz=0,0,0
        if PLOT: self.xs,self.ys,self.zs=[x],[y],[z]
        if USE_TURTLE:
            self.turtle=Turtle()
            self.turtle.hideturtle()
            self.turtle.penup()
            self.turtle.goto(self.x,self.y)
            self.turtle.pendown()
    def apply_gravity(self,elf):
        if self is elf: return
        self.vx+=sign(elf.x-self.x)
        self.vy+=sign(elf.y-self.y)
        self.vz+=sign(elf.z-self.z)
    def apply_velocity(self):
        self.x+=self.vx
        self.y+=self.vy
        self.z+=self.vz
        if PLOT:
            self.xs.append(self.x)
            self.ys.append(self.y)
            self.zs.append(self.z)
        if USE_TURTLE:self.turtle.goto(self.x,self.y)
    def energy(s):
        return sum(map(abs,(s.x,s.y,s.z)))*sum(map(abs,(s.vx,s.vy,s.vz)))
    def __repr__(s):
        return f"p=<{s.x:4d},{s.y:4d},{s.z:4d}>; v=<{s.vx:4d},{s.vy:4d},{s.vz:4d}>"
    def get_state(self, axes):
        """Part 2 - x,y,z are independent
        return position, velocity"""
        return getattr(self,axes),getattr(self,f"v{axes}")

def get_all_states():
    global moons
    states = {'x':(),'y':(),'z':()}
    for moon in moons:
        for a in 'xyz':
            states[a]+=moon.get_state(a)
    return states.values() # Note - sorted dict

with open('12.txt') as file:
    data = file.read().splitlines()

moons=[]
for d in data:
    sx,sy,sz=d.split(', ')
    x=int(sx.split('=')[1])
    y=int(sy.split('=')[1])
    z=int(sz.split('=')[1][:-1])
    moons.append(Moon(x,y,z))
Io, Europa, Ganymede, Callisto = moons

state_x = {}
state_y = {}
state_z = {}
xdiff = ydiff = zdiff = None

step = 0
while xdiff is None or ydiff is None or zdiff is None or step<1000:
    for moon in moons:
        for other_moon in moons:
            moon.apply_gravity(other_moon)
    for moon in moons:
        moon.apply_velocity()
    if step==999:
        print('Part 1:',sum(moon.energy() for moon in moons),flush=True)
    x,y,z = get_all_states()
    if xdiff is None:
        if x in state_x:
            xdiff = step-state_x[x]
            print('x',xdiff,flush=True)
        else:
            state_x[x]=step
    if ydiff is None:
        if y in state_y:
            ydiff = step-state_y[y]
            print('y',ydiff,flush=True)
        else:
            state_y[y]=step
    if zdiff is None:
        if z in state_z:
            zdiff = step-state_z[z]
            print('z',zdiff,flush=True)
        else:
            state_z[z]=step
    step+=1

from math import lcm
print('Part 2:',lcm(xdiff,ydiff,zdiff))

if PLOT:
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(Io.xs,Io.ys,Io.zs,'red')
    ax.plot3D(Europa.xs,Europa.ys,Europa.zs,'green')
    ax.plot3D(Ganymede.xs,Ganymede.ys,Ganymede.zs,'blue')
    ax.plot3D(Callisto.xs,Callisto.ys,Callisto.zs,'yellow')