import time
init_time = int(time.time())
NUM_ELVES = 3018458  # Puzzle input
elf_presents = {}
keys = list(elf_presents.keys())


def get_opposite_key(index):
    global keys
    # keys = list(elf_presents.keys())  # assumes sorted list
    return keys.pop((index + (len(keys) // 2)) % len(keys))


for i in range(1, NUM_ELVES + 1):
    elf_presents[i] = 1
keys = list(elf_presents.keys())
i = 0
while len(keys):
    i = i % len(keys)  # keep in range - moved to top to avoid Div0
    receiving_elf = keys[i]
    generous_elf = get_opposite_key(i)
    elf_presents[receiving_elf] += elf_presents.pop(generous_elf)
    # i.e. changed val was after i
    if len(keys) > i and receiving_elf == keys[i]:
        i += 1  # next elf in circle
    if not len(keys) % 1000:  # Just let you know that stuff is still happening
        print(f"{(int(time.time()) - init_time):5d}s:{len(keys):10d} elves left")
# slight bug: last elf gets all the prezzies TWICE!
print('Elf', list(elf_presents.keys())[0], 'got all the presents')
# This script takes about 30 minutes to run
