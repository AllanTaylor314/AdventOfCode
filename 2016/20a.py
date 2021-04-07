import time
init = int(time.time())


def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


ranges = [tuple(map(int, _.split('-'))) for _ in lines_from_file('20.txt')]
start_end = {_[0]: _[1] for _ in ranges}
start_range = {_[0]: range(*_) for _ in ranges}
#{(x := tuple(_.split('-')))[0]: x[1] for _ in lines_from_file('20.txt')}
i = start_end.get(0, 0)
target = 0
prev_starts = set()
while True:
    if i == 0:
        break
    elif i in prev_starts:
        i -= 1
    elif i in start_end:
        print(i, '->', start_end[i] + 1)
        prev_starts.add(i)
        i = start_end[i] + 1
    else:
        target = max(target, i)
        i -= 1
print(target)
for ran in ranges:
    if target in ran:
        print(target, 'was in range', min(ran), '-', max(ran))
        break
else:
    print(target, 'was not in any blocklists')
# blocked = set()
# i = 0
# for line in lines:
#    start, end = line.split('-')
#    #ip_range = ip_range - set(range(int(start), int(end) + 1))
#    blocked |= set(range(int(start), int(end) + 1))
#    print(f"{i:5}/{len(lines)} t={int(time.time())-init:5} {line:20}")
#    i += 1

#ip_range = set(range(2**32)) - blocked
# print(min(ip_range))
