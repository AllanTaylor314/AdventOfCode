import numpy as np
with open('20.txt') as file:
    instructions = file.read().splitlines()
# px,py,pz,vx,vy,vz,ax,ay,az
particles = np.array([[n] + list(map(int, i.replace('p=<', '').replace('>', '').replace(
    ' v=<', '').replace(' a=<', '').split(','))) for n, i in enumerate(instructions)])

p = particles[:, 1:4]
v = particles[:, 4:7]
a = particles[:, 7:]

al = np.sum(np.abs(a), axis=1)
vl = np.sum(np.abs(v), axis=1)
pl = np.sum(np.abs(p), axis=1)
avpl = np.array([al, vl, pl, particles[:, 0]]).T
# avplt = [tuple(r) for r in avpl]
# avplt.sort()
# print(avpl)
#avpl2 = avpl[avpl[:, 0].argsort()]
# print(avpl2)

#print('Part 1:', avpl2[0, 3])
print('Part 1:', np.lexsort(avpl[:, ::-1].T)[0])
# Not quite right??

# 746 too high
# 294 too low
# 316 too high
# 308 was right

quit()
_ = 0
while True:
    v += a
    p += v
    if _ % 1000 == 0:
        pl = list(np.sum(p, axis=1))
        # print(pl)
        print(pl.index(min(pl)))
    # print(np.where(p == min(p, key=sum)))
    _ += 1

pl = list(np.sum(p, axis=1))
print('Part 1:', pl.index(min(pl)))
