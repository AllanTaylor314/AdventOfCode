import numpy as np
with open('20.txt') as file:
    instructions = file.read().splitlines()
# instructions = """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
# p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
# p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
# p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>""".splitlines()
# px,py,pz,vx,vy,vz,ax,ay,az
pva = np.array([[n] + list(map(int, i.replace('p=<', '').replace('>', '').replace(
    ' v=<', '').replace(' a=<', '').split(','))) for n, i in enumerate(instructions)])

p = pva[:, 1:4]
v = pva[:, 4:7]
a = pva[:, 7:]
prevlen = 1000
p2 = len(instructions)
for _ in range(1000):
    pva[:, 4:7] += pva[:, 7:]
    pva[:, 1:4] += pva[:, 4:7]
    pval = [tuple(sl) for sl in pva[:, 1:4]]
    singles = {sl for sl in pval if pval.count(sl) == 1}
    fil = [(tuple(val) in singles) for val in pval]
    pva = pva[fil]
    if len(pva) < p2:
        p2 = len(pva)
        print(p2, flush=True)
print('Part 2:', len(pva))
# 504
