r=[0]*6
r[0]=1  # Part 2
if r[0]==0:
    r[1]=194
    r[2]=1030
elif r[0]==1:
    r[1],r[2]=10550400,10551430
else:
    raise ValueError()
r[0]=0
r[4]=1
while True:
    r[3]=1
    while True:
        r[1]=r[4]*r[3]
        if r[1]==r[2]:
            r[1]=1
            r[0]+=r[4]
        else:r[1]=0
        r[3]+=1
        if r[3]>r[2]:
            r[1]=1
            break
        else:
            r[1]=0
    r[4]+=1
    if r[4]>r[2]:
        r[1]=1
        break
    else:r[1]=0

print(r)