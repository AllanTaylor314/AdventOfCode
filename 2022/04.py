with open("04.txt") as file:
    lines = file.read().splitlines()

def contains(a,b):
    a1,a2=map(int,a.split('-'))
    b1,b2=map(int,b.split('-'))
    return a1<=b1 and a2>=b2
def overlap(a,b):
    a1,a2=map(int,a.split('-'))
    b1,b2=map(int,b.split('-'))
    return a1<=b2 and b1<=a2
p1 = p2 = 0
for line in lines:
    left,right = line.split(',')
    p1+=contains(left,right) or contains(right,left)
    p2+=overlap(left,right)
print("Part 1:",p1)
print("Part 2:",p2)
