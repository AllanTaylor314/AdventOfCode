import matplotlib.pyplot as plt

with open('23.txt') as file:
    data = file.read()

bots=[]
for i,line in enumerate(data.splitlines()):
    x,y,z=map(int, line[5:line.index('>')].split(','))
    r=int(line.split()[1][2:])
    bots.append((x,y,z,r))

fig = plt.figure()
ax = plt.axes(projection='3d')

*xyzs,rs=list(zip(*bots))
ax.scatter3D(*xyzs, c=rs, cmap='Reds')
ax.scatter3D(*(0,)*3,'blue')