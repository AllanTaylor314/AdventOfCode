with open('16.txt') as file:
    moves = file.read().strip().split(',')

moves_pro=[]
moves_loc=[]
for move in moves:
    if move[0]=='p':
        moves_pro.append(move)
    else:
        moves_loc.append(move)

loc_dancers = list(range(16))
for move in moves_loc:
    if move.startswith('s'):
        i = int(move[1:])
        loc_dancers = loc_dancers[-i:] + loc_dancers[:len(loc_dancers) - i]
    else:
        a, b = map(int,move[1:].split('/'))
        loc_dancers[a], loc_dancers[b] = loc_dancers[b], loc_dancers[a]

def apply_loc_moves(formation):
    return [formation[i] for i in loc_dancers]

pro_dancers_init="".join(chr(97+_) for _ in range(16))
pro_dancers=pro_dancers_init
for move in moves_pro:
    a, b = move[1:].split('/')
    pro_dancers=pro_dancers.translate(str.maketrans(a+b,b+a))
trans_pro_dancers = str.maketrans(pro_dancers_init,pro_dancers)

### Part 1 ###
part1=list(pro_dancers_init)
part1=[part1[i] for i in loc_dancers]
part1="".join(part1).translate(trans_pro_dancers)
print('Part 1:',part1)

### Part 2 ###
loc=list(pro_dancers_init)
init=loc.copy()
i=0
while loc!=init or i==0:
    loc=apply_loc_moves(loc)
    i+=1
loc_loop_size=i

pro=pro_dancers_init
j=0
while pro!=pro_dancers_init or j==0:
    pro=pro.translate(trans_pro_dancers)
    j+=1
pro_loop_size=j

BILLION=1_000_000_000
part2=list(pro_dancers_init)
for _ in range(BILLION%loc_loop_size):
    part2=apply_loc_moves(part2)
part2="".join(part2)
for _ in range(BILLION%pro_loop_size):
    part2=part2.translate(trans_pro_dancers)
print('Part 2:',part2)
