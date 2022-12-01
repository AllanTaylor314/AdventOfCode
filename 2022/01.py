with open("01.txt") as file:
    numnums = [list(map(int,s.splitlines())) for s in file.read().split("\n\n")]
sums = sorted(list(map(sum,numnums)), reverse=True)
print("Part 1:",sums[0])
print("Part 2:",sum(sums[:3]))
