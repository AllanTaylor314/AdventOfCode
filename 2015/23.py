class Computer:
    def __init__(s,code,a=0,b=0):
        s.c = code
        s.r={}
        s.i,s.r['a'],s.r['b']=0,a,b
    def hlf(s,r):
        s.r[r]//=2
        s.i+=1
    def tpl(s,r):
        s.r[r]*=3
        s.i+=1
    def inc(s,r):
        s.r[r]+=1
        s.i+=1
    def jmp(s,o):
        s.i+=int(o)
    def jie(s,r,o):
        if s.r[r]%2==0:
            s.i+=int(o)
        else:
            s.i+=1
    def jio(s,r,o):
        if s.r[r]==1:
            s.i+=int(o)
        else:
            s.i+=1
    def run(s):
        try:
            while True:
                c,*a=s.c[s.i]
                getattr(s,c)(*a)
        except IndexError:
            return

with open('23.txt') as file:
    code = list(map(str.split,file.read().replace(',','').splitlines()))

x=Computer(code)
x.run()
print('Part 1:',x.r['b'])

y=Computer(code,a=1)
y.run()
print('Part 2:',y.r['b'])