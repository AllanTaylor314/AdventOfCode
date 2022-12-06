def unique_offset(data,length):
    for i in range(length,len(data)):
        if len(set(data[i-length:i]))==length:
            return i

with open("06.txt") as file:
    data = file.read().strip()

print("Part 1:",unique_offset(data,4))
print("Part 2:",unique_offset(data,14))
