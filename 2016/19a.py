NUM_ELVES = 3018458

elf_presents = {}
for i in range(1, NUM_ELVES + 1):
    elf_presents[i] = 1
i = 1
#q = 0
# while max(elf_presents.values()) < NUM_ELVES): # No one has all the prezzies
while len(elf_presents) > 1:
    # print(elf_presents)
    while i not in elf_presents:
        i = (i + 1) % (NUM_ELVES + 1)
    receiving_elf = i
    i = (i + 1) % (NUM_ELVES + 1)
    while i not in elf_presents:
        i = (i + 1) % (NUM_ELVES + 1)
    generous_elf = i
    #print(receiving_elf, generous_elf)
    elf_presents[receiving_elf] += elf_presents.pop(generous_elf)
    i = (i + 1) % (NUM_ELVES + 1)
    #q += 1
    # if q > 10:
    #    break
print(elf_presents)
