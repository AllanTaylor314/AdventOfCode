PLOT=False
if PLOT:
    from mpl_toolkits import mplot3d
    import numpy as np
    import matplotlib.pyplot as plt

USE_TURTLE=False
if USE_TURTLE:
    from turtle import *

def sign(a):return int(a/abs(a)) if a else 0

class Moon:
    def __init__(self, x, y, z):
        self.x,self.y,self.z=x,y,z
        self.vx,self.vy,self.vz=0,0,0
        self.xs,self.ys,self.zs=[x],[y],[z]
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
        self.xs.append(self.x)
        self.ys.append(self.y)
        self.zs.append(self.z)
        if USE_TURTLE:self.turtle.goto(self.x,self.y)
    def energy(s):
        return sum(map(abs,(s.x,s.y,s.z)))*sum(map(abs,(s.vx,s.vy,s.vz)))
    def __repr__(s):
        return f"p=<{s.x:4d},{s.y:4d},{s.z:4d}>; v=<{s.vx:4d},{s.vy:4d},{s.vz:4d}>"

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

for step in range(1000):
    for moon in moons:
        for other_moon in moons:
            moon.apply_gravity(other_moon)
    for moon in moons:
        moon.apply_velocity()
print('Part 1:',sum(moon.energy() for moon in moons))

if PLOT:
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(Io.xs,Io.ys,Io.zs,'red')
    ax.plot3D(Europa.xs,Europa.ys,Europa.zs,'green')
    ax.plot3D(Ganymede.xs,Ganymede.ys,Ganymede.zs,'blue')
    ax.plot3D(Callisto.xs,Callisto.ys,Callisto.zs,'yellow')