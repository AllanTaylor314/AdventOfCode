class Paper:
    def __init__(self,points):
        self.points=set(points)
    def fold_x(self,c):
        for px,py in list(self.points):
            if px>c:
                nx=2*c-px
                self.points.remove((px,py))
                self.points.add((nx,py))
    def fold_y(self,c):
        for px,py in list(self.points):
            if py>c:
                ny=2*c-py
                self.points.remove((px,py))
                self.points.add((px,ny))
    def __repr__(self):
        mx=range(max(self.points)[0]+1)
        my=range(max(self.points,key=lambda a: a[1])[1]+1)
        return"\n".join("".join(' █'[(x,y)in self.points]for x in mx)for y in my)

with open('13.txt') as file:
    data = file.read()

points_str,folds_str=data.split('\n\n')
points=[tuple(map(int,l.split(','))) for l in points_str.splitlines()]
folds = []
for f in folds_str.splitlines():
    *_,d = f.split()
    xy,n=d.split('=')
    folds.append((xy,int(n)))

paper = Paper(points)
p1=True
for xy,c in folds:
    getattr(paper, f'fold_{xy}')(c)
    if p1:p1=print('Part 1:',len(paper.points))
print('Part 2:')
print(paper)