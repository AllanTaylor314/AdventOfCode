from operator import*;O=add,mul
C=[(int(a[:-True]),[*map(int,b)])for a,*b in map(str.split,open(False))]
g=lambda l,i=-True:{o(v,l[i])for v in g(l,~-i%len(l))for o in O}if i else{l[i]}
for p in O:print(sum(c*(c in g(n))for c,n in C));O+=lambda*a:int("%d%d"%a),
