from itertools import cycle, chain, repeat, islice

BASE_PATTERN=(0, 1, 0, -1)
def gen_pattern(pos):
    pattern=cycle(chain(*(repeat(i,pos) for i in BASE_PATTERN)))
    next(pattern)  # Skip the first
    return pattern

def num_to_digits(num):
    return list(map(int,str(num)))

def digits_to_num(digits):
    return int("".join(map(str,digits)))

def flawed_frequency_transmission(digits):
    new_digits=[]
    for pos in range(len(digits)):
        new_digits.append(abs(sum(map(int.__mul__,digits,gen_pattern(pos+1))))%10)
    return new_digits

def new_sum(digits, pos):
    plus_sum = sum(sum(digits[i:i+pos]) for i in range(pos-1,len(digits),4*pos))
    minus_sum = sum(sum(digits[i:i+pos]) for i in range(pos*3-1,len(digits),4*pos))
    return plus_sum-minus_sum

def flawed_frequency_transmission2(digits):
    return [abs(new_sum(digits,pos+1))%10 for pos in range(len(digits))]

test_digits=num_to_digits(12345678)
new_test=flawed_frequency_transmission2(test_digits)
assert digits_to_num(new_test)==48226158

test1_digits = num_to_digits(80871224585914546619083218645595)
for _ in range(100):
    test1_digits=flawed_frequency_transmission2(test1_digits)
assert digits_to_num(test1_digits[:8])==24176176

test2_digits = num_to_digits(19617804207202209144916044189917)
for _ in range(100):
    test2_digits=flawed_frequency_transmission2(test2_digits)
assert digits_to_num(test2_digits[:8])==73745418

test3_digits = num_to_digits(69317163492948606335995924319873)
for _ in range(100):
    test3_digits=flawed_frequency_transmission2(test3_digits)
assert digits_to_num(test3_digits[:8])==52432133


with open('16.txt') as file:
    num = int(file.read().strip())
master_digits = num_to_digits(num)
digits = master_digits.copy()
for _ in range(100):
    digits=flawed_frequency_transmission2(digits)
print('Part 1:',digits_to_num(digits[:8]),flush=True)

#---- Part 2 ----
# Based on https://www.reddit.com/r/adventofcode/comments/ebai4g/comment/fb5n79m
# Still not sure how it works, but something about upper triangular numbers
offset = digits_to_num(master_digits[:7])
from itertools import accumulate
part2_digits = (master_digits*10000)[offset:]
part2_digits.reverse()
for _ in range(100):
    part2_digits = [n%10 for n in accumulate(part2_digits)]
print('Part 2:',digits_to_num(reversed(part2_digits[-8:])))
