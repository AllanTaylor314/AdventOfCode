def cutstr(s):
    return s[:len(s)//2],s[len(s)//2:]
def score(c):
    if 'a'<=c<='z':return ord(c)-ord('a')+1
    return ord(c)-ord('A')+27

with open("03.txt") as file:
    lines = file.read().splitlines()
p1 = 0
for line in lines:
    a,b = cutstr(line)
    x,=set(a)&set(b)
    p1 += score(x)
print("Part 1:",p1)
p2 = 0
for a,b,c in zip(lines[::3],lines[1::3],lines[2::3]):
    x,=set(a)&set(b)&set(c)
    p2 += score(x)
print("Part 2:",p2)
