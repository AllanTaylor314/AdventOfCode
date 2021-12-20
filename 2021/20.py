from functools import cache

with open('20.txt') as file:
    data = file.read()
algo,_,*lines = data.splitlines()
ENHANCE_ALGO = algo.translate(str.maketrans('.#','01'))
LIT_PIXELS = {(x,y)for y,l in enumerate(lines)for x,c in enumerate(l)if c=='#'}

@cache
def multi_enhance(ox,oy,depth):
    if depth == 0: return '01'[(ox,oy) in LIT_PIXELS]
    new = []
    for y in range(oy-1,oy+2):
        for x in range(ox-1,ox+2):
            new.append(multi_enhance(x,y,depth-1))
    return ENHANCE_ALGO[int("".join(new),2)]

def solve(reps):
    rng = range(-reps,101+reps)
    count = 0
    for x in rng:
        for y in rng:
            if multi_enhance(x,y,reps)=="1":
                count+=1
    return count

print('Part 1:',solve(2))
print('Part 2:',solve(50))
