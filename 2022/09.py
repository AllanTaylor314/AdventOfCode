with open("09.txt") as file:
    lines = file.read().splitlines()
deltas = [(int(b),1j**"RDLU".index(a)) for a,b in map(str.split,lines)] # num, dir
def sign(n):
    if n==0:return 0
    if n<0:return -1
    return 1
def difference_to_direction(diff: complex):
    return sign(diff.real)+sign(diff.imag)*1j
def solve(length):
    tails = {0}
    rope = [0+0j]*length
    for num,dire in deltas:
        for _ in range(num):
            rope[0]+=dire
            for ti in range(1,len(rope)):
                hi=ti-1 # head index, tail index
                if abs(rope[hi]-rope[ti])>=2: # Up to sqrt2
                    rope[ti]+=difference_to_direction(rope[hi]-rope[ti])
            tails.add(rope[ti]) # last only
    return len(tails)
print("Part 1:",solve(2))
print("Part 2:",solve(10))
