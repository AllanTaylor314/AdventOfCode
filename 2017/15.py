A, B = 783, 325


def a_is_b(a, b):
    return ((a & 65535) ^ (b & 65535)) == 0


def a_gen(a):
    while True:
        a = a * 16807 % 2147483647
        if a % 4 == 0:
            yield a


def b_gen(b):
    while True:
        b = b * 48271 % 2147483647
        if b % 8 == 0:
            yield b


a, b = A, B
j = 0
# """
for i in range(40000000):
    a, b = a * 16807 % 2147483647, b * 48271 % 2147483647
    if a_is_b(a, b):
        j += 1
        #print(f"{i:10d}: A={a:10d}, B={b:10d}")
print('Part 1:', j)
# """

gen_a = a_gen(A)
gen_b = b_gen(B)
k = 0
for i, a, b in zip(range(5000000), gen_a, gen_b):
    #a, b = next(gen_a), next(gen_b)
    if a_is_b(a, b):
        k += 1
        #print(f"{i:10d}: A={a:10d}, B={b:10d}")
print('Part 2:', k)
