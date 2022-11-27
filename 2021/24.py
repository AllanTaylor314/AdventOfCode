# Essentially, this is the input - it is just which of the values
# changed in the 18 line blocks
A=[  1,  1,  1,  1,  1,  26,  1, 26, 26,  1, 26, 26, 26, 26]
B=[ 15, 10, 12, 10, 14, -11, 10,-16, -9, 11, -8, -8,-10, -9]
C=[ 13, 16,  2,  8, 11,   6, 12,  2,  2, 15,  1, 10, 14, 10]

# Pairs of indices that must cancel out
opp_pairs = []
stack = []
for i,a in enumerate(A):
    if a==1: stack.append(i)
    else: opp_pairs.append((stack.pop(),i))

pairs = []
for a,b in opp_pairs:
    delta = C[a]+B[b] # Modulo stuff boils down to wo=wi+ci+bo
    for wa in range(9,0,-1):
        wb = wa + delta
        if wb in range(1,10):
            pairs.append((a,wa,b,wb))

def generate_possible_numbers(num_tupl=(0,)*14):
    for pair in pairs:
        a_ind,wa,b_ind,wb = pair
        if num_tupl[a_ind]==0==num_tupl[b_ind]:
            num_copy = list(num_tupl)
            num_copy[a_ind] = wa
            num_copy[b_ind] = wb
            if 0 in num_copy:
                yield from generate_possible_numbers(tuple(num_copy))
            else:
                yield num_copy

print('Part 1: ',*next(generate_possible_numbers()),sep='',flush=True)
pairs.reverse() # So that smaller values are picked first
print('Part 2: ',*next(generate_possible_numbers()),sep='',flush=True)
