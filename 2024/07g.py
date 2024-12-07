from operator import*;O=add,mul
C=[(int(a),[*map(int,b.split())])for a,b in(l.split(":")for l in open(False))]
g=lambda l,i=-True:{o(v,l[i])for v in g(l,~-i%len(l))for o in O}if i else{l[i]}
for p in O:print(sum(c*(c in g(n))for c,n in C));O+=lambda a,b:int(f"{a}{b}"),
