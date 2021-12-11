def swap_pos_x_pos_y(password, x, y):
    password[x],password[y]=password[y],password[x]
    return password
def swap_letter_x_letter_y(pw, x, y):
    return swap_pos_x_pos_y(pw,pw.index(x),pw.index(y))
def rotate_left(pw,steps):
    steps%=len(pw)
    return pw[steps:]+pw[:steps]
def rotate_right(pw,steps):
    return rotate_left(pw,-steps)
def rotate_pos_x(pw,x):
    index=pw.index(x)
    pw=rotate_right(pw,1)
    pw=rotate_right(pw,index)
    if index>=4:
        pw=rotate_right(pw,1)
    return pw
def reverse_pos(pw,x,y):
    x,y=sorted((x,y))
    return pw[:x]+pw[y:(x-1 if x>0 else None):-1]+pw[y+1:]
def move_pos(pw,x,y):
    tmp=pw[x]
    pw.insert(y,pw.pop(x))
    assert pw[y]==tmp
    return pw

with open('21.txt') as file:
    data=file.read().splitlines()

def scramble(password='abcdefgh'):
    password=list(password)
    for line in data:
        instruction = line.split()
        if instruction[0]=='swap':
            if instruction[1]=='position':
                password=swap_pos_x_pos_y(password,int(instruction[2]),int(instruction[5]))
            elif instruction[1]=='letter':
                password=swap_letter_x_letter_y(password,instruction[2],instruction[5])
            else:
                raise ValueError(line)
        elif instruction[0]=='rotate':
            if instruction[1]=='left':
                password=rotate_left(password,int(instruction[2]))
            elif instruction[1]=='right':
                password=rotate_right(password,int(instruction[2]))
            elif instruction[1]=='based':
                password=rotate_pos_x(password,instruction[-1])
            else:
                raise ValueError(line)
        elif instruction[0]=='reverse':
            password=reverse_pos(password,int(instruction[2]),int(instruction[4]))
        elif instruction[0]=='move':
            password=move_pos(password,int(instruction[2]),int(instruction[5]))
        else:
            raise ValueError(line)
    return "".join(password)

print('Part 1:',scramble(),flush=True)

from itertools import permutations

for perm in permutations('abcdefgh'):
    if scramble(perm)=='fbgdceah':
        print('Part 2:',"".join(perm))
        break
