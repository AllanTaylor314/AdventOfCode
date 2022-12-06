with open("06.txt") as file:
    data = file.read().strip()

for i,four in enumerate(zip(data,data[1:],data[2:],data[3:]),start=4):
    if len(set(four))==4:
        p1 = i
        break
print("Part 1:",p1)
for i in range(14,len(data)):
    if len(set(data[i-14:i]))==14:
        p2=i
        break
print("Part 2:",p2)
