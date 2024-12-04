*l,g=*open(0),lambda i,j:l[i][j]if len(l)>i>-1<j<len(l[i])else""
e=enumerate;d=[(i,j)for i in(-1,0,1)for j in(-1,0,1)]
print(*map(sum,zip(*((all(c==g(i+n*x,j+n*y)for n,c in e("XMAS"))
,c=="A"and"M"==g(i-x,j-y)==g(i-y,j+x)and"S"==g(i+x,j+y)==g(i+y,j
-x)and x!=0!=y)for i,m in e(l)for j,c in e(m)for x,y in d))))
