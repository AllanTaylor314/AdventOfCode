from functools import cache

with open('20.txt') as file:
    data = file.read()
ENHANCE_ALGO,_,*lines = data.splitlines()
INPUT_IMAGE = [list(l) for l in lines]
LIT_PIXELS = {(x,y)for y,l in enumerate(lines)for x,c in enumerate(l)if c=='#'}

def enhance_index(ox,oy):
    b=''
    for y in range(oy-1,oy+2):
        for x in range(ox-1,ox+2):
            b+='01'[(x,y) in LIT_PIXELS]
    return int(b,2)

def double_enhance(ox,oy):
    new = []
    for y in range(oy-1,oy+2):
        for x in range(ox-1,ox+2):
            new.append(ENHANCE_ALGO[enhance_index(x,y)])
    return ENHANCE_ALGO[int("".join(new).translate(str.maketrans('.#','01')),2)]

@cache
def multi_enhance(ox,oy,depth):
    if depth == 0: return '.#'[(ox,oy) in LIT_PIXELS]
    new = []
    for y in range(oy-1,oy+2):
        for x in range(ox-1,ox+2):
            new.append(multi_enhance(x,y,depth-1))
    return ENHANCE_ALGO[int("".join(new).translate(str.maketrans('.#','01')),2)]

new_image = set()
for x in range(-20,121):
    for y in range(-20,121):
        if double_enhance(x,y)=='#':
            new_image.add((x,y))


print('Part 1:',len(new_image))

# Validate that 1 and 2 steps match the previous definitions
assert all(ENHANCE_ALGO[enhance_index(x,y)]==multi_enhance(x,y,1)
           for x in range(100) for y in range(100))
assert all(double_enhance(x,y)==multi_enhance(x,y,2)
           for x in range(100) for y in range(100))

new_image2 = set()
for x in range(-50,151):
    for y in range(-50,151):
        if multi_enhance(x,y,50)=="#":
            new_image2.add((x,y))

print('Part 2:',len(new_image2))
