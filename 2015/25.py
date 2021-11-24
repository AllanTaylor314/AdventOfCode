######## INPUT ########
coordinate = 2947, 3029
#######################

INIT = 20151125
MUL = 252533
MOD = 33554393

def rc_to_n(r,c):
    """Take a row and column and find the n that fits there"""
    return 1+(r+c)*(r+c-1)//2-r

def nth_num(n):
    """Finds the code in slot n"""
    BIG = 1000
    i = n-1
    x = INIT
    big_mul = MUL**BIG
    while i>BIG:
        i-=BIG
        x=x*big_mul%MOD
    x=x*MUL**i%MOD
    return x

# Verify rc_to_n
for r in range(1,7):
    for c in range(1,7):
        print(f"{rc_to_n(r,c):3d}",end='')
    print()
print()

# Verify nth_num matches example
for r in range(1,7):
    for c in range(1,7):
        #print(f"{INIT*MUL**(rc_to_n(r,c)-1)%MOD:10d}",end='')
        print(f"{nth_num(rc_to_n(r,c)):10d}",end='')
    print()
print(flush=True)

n=rc_to_n(*coordinate)
print('Part 1:',nth_num(n))
