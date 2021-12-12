from functools import cache

SMALL_DECK = 10007
BIG_DECK = 119315717514047
BIG_SHUFFLE_COUNT = 101741582076661

with open('22.txt') as file:
    data = file.read()
instructions = data.splitlines()

def power(x, y, m):
    """(x**y)%m (recursive)
    https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
    """
    if (y == 0):
        return 1
    p = power(x, y // 2, m)
    p = p * p % m
    if(y % 2 == 0):
        return p
    else:
        return x * p % m

def mul_inv(n,m):
    """Multiplicative inverse of n (mod m)
    n and m must be coprime (always true as m is prime in this problem)
    """
    return power(n, m-2, m)

@cache
def shuffle(pos,deck_size=SMALL_DECK):
    global instructions
    for i in instructions:
        *_,n = i.split()
        if n=="stack":
            pos=-pos-1
        elif _[0]=='deal':
            pos = (pos*int(n))
        elif _[0]=='cut':
            pos-=int(n)
        else:
            raise ValueError
        pos%=deck_size
    return pos

@cache
def shuffle_inv(pos,deck_size=SMALL_DECK):
    global instructions
    for i in instructions[::-1]:
        *_,n = i.split()
        if n=="stack":
            pos=-pos-1
        elif _[0]=='deal':
            pos *= power(int(n), deck_size-2, deck_size)
        elif _[0]=='cut':
            pos+=int(n)
        else:
            raise ValueError
        pos%=deck_size
    return pos

def fast_shuffle(n, m=SMALL_DECK):
    """Mathematically find the location of n in an m-sized deck after a shuffle
    Functionally equivalent to shuffle (and uses shuffle to find the init vals)
    """
    ds=shuffle(1,m)-(s0:=shuffle(0,m))
    return (n*ds+s0)%m

# Verify that fast_shuffle matches shuffle
assert all(fast_shuffle(i)==shuffle(i) for i in range(10007))

def fast_shuffle_inv(n, m=SMALL_DECK):
    """Inverse function of fast_shuffle (and indirectly, shuffle)"""
    ds=shuffle(1,m)-(s0:=shuffle(0,m))
    return (n-s0)*mul_inv(ds,m)%m

# Verify that fast_shuffle_inv inverts fast_shuffle
assert all(fast_shuffle(fast_shuffle_inv(i))==i for i in range(10007))

def multi_shuffle(pos,times=1,size=SMALL_DECK):
    """Find the position of pos after times shuffles"""
    for _ in range(times):
        pos=fast_shuffle(pos,size)
    return pos

def multi_shuffle_inv(pos,times=1,size=SMALL_DECK):
    """Inverse of multi_shuffle (and about as slow)"""
    for _ in range(times):
        pos=fast_shuffle_inv(pos,size)
    return pos

def fast_multi_shuffle(n, t=1, m=SMALL_DECK):
    """Functionally equivalent to multi_shuffle, but uses maths not loops
    Used WolframAlpha to find the sum of powers (not sure what it is called)
    https://www.wolframalpha.com/input/?i=Sum%5BPower%5Bs%2Ck%5D%2C%7Bk%2C0%2Ct-1%7D%5D
    """
    ds=shuffle(1,m)-(s0:=shuffle(0,m))
    return (n*power(ds, t, m)+s0*(power(ds, t, m)-1)*mul_inv(ds-1,m))%m

def fast_multi_shuffle_inv(n, t=1, m=SMALL_DECK):
    """Functionally equivalent to multi_shuffle_inv,
    but significantly faster because of maths.
    Rearranged the formula from fast_multi_shuffle to find its inverse
    Uses mul_inv insted of division due to modular arithmetic"""
    ds=shuffle(1,m)-(s0:=shuffle(0,m))
    return (n-s0*(power(ds, t, m)-1)*mul_inv(ds-1,m))*mul_inv(power(ds,t,m),m)%m

# Verify multi_shuffle and multi_shuffle_inv, and their fast counterparts
assert multi_shuffle(2019,10)==fast_multi_shuffle(2019,10)
assert multi_shuffle_inv(multi_shuffle(2019,10),10)==2019
assert fast_multi_shuffle_inv(fast_multi_shuffle(2019,1000),1000)==2019

print('Part 1:', shuffle(2019))
print('Part 2:', fast_multi_shuffle_inv(2020,BIG_SHUFFLE_COUNT,BIG_DECK))
