with open("01.txt") as file:
    sums = sorted(list(map(sum,(list(map(int,s.splitlines())) for s in file.read().split("\n\n")))), reverse=True)
print("Part 1:",sums[0],"\nPart 2:",sum(sums[:3]))
