def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


ranges = [tuple(map(int, _.split('-'))) for _ in lines_from_file('20.txt')]
ranges.sort()
start_end = {_[0]: _[1] for _ in ranges}
big_start = 0
big_end = start_end[big_start]
count = 0
starts = []
ends = []
for start, end in start_end.items():
    if start - 2 < big_end:
        big_end = max(end, big_end)
    else:
        count += 1
        #print(f'{count:4d}:{big_start:11d} ->{big_end:11d}')
        starts.append(big_start)
        ends.append(big_end)
        big_start = start
        big_end = end

starts.append(big_start)
ends.append(big_end)
starts.append(2**32)

total = 2**32
num_blocked = 0
for i in range(len(ends)):
    # print(starts[i], 'to', ends[i], '(inc) which is', ends[i] - starts[i] + 1)
    num_blocked += ends[i] - starts[i] + 1
print(num_blocked, 'addresses were blocked')
print('for a total of', total - num_blocked, 'allowed ip addresses')

print('The allowed addresses are:')
i = 0
count = 0
while i < len(ends):
    ip = ends[i] + 1
    while ip < starts[i + 1]:
        print(ip)
        count += 1
        ip += 1
    i += 1
print('Total:', count)
