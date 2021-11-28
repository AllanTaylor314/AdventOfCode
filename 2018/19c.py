r=[0]*6
r0,r1,r2,r3,r4,r5=r
#r0=1  # Uncomment for Part 2
if r0==0:
    r2=(0+2)**2*19*11+(8*22+18)
elif r0==1:
    r2=((0+2)**2*19*11+(8*22+18))+((27*28+29)*30*14*32)
else:
    raise ValueError()
part = r0+1
r0=0
for r4 in range(1,r2+1):
    if r2%r4==0:
        r0+=r4
    #for r3 in range(1,r2+1):
        #if r4*r3==r2:
            #r0+=r4
print(f"Part {part}: {r0}")