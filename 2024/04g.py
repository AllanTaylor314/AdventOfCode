*l,g=*open(0),lambda i,j:l[i][j]if len(l)>i>-1<j<len(l[i])else""
e,*d=enumerate,-1,0,1
print(*map(sum,zip(*((all(c==g(i+n*x,j+n*y)for n,c in e("XMAS"))
,x!=0!=y!=c=="A"<"M"==g(i-x,j-y)==g(i-y,j+x)<"S"==g(i+x,j+y)==g(
i+y,j-x))for i,m in e(l)for j,c in e(m)for x in d for y in d))))
