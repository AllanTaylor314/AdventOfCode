g=lambda i,j:l[i][j]if len(l)>i>-1<j<len(l[i])else""
*l,e,d=*open(0),enumerate,[(i,j)for i in(-1,0,1)for j in(-1,0,1)]
print(sum(all(c==g(i+n*x,j+n*y)for n,c in e("XMAS"))for i,m in e(l)for j,c in
e(m)for x,y in d),sum(c=="A"and"M"==g(i-x,j-y)==g(i-y,j+x)and"S"==g(i+x,j+y)
==g(i+y,j-x)for i,m in e(l)for j,c in e(m)for x,y in d[::2]))
