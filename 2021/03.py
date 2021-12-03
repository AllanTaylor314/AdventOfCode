with open('03.txt') as file:
    data=file.read().splitlines()

nums = [int(s,2) for s in data]
bits = ['1' if x.count('1')>x.count('0') else '0' for x in zip(*data)]
gamma = int("".join(bits),2)
epsilon = (2**(len(bits))-1)^gamma
print('Part 1:',gamma*epsilon)

filtered = data.copy()
for i in range(len(bits)):
    new_filtered=[]
    x=[f[i] for f in filtered]
    req='1' if x.count('1')>=x.count('0') else '0'
    if len(filtered)==1: break
    for f in filtered:
        if f[i]==req:
            new_filtered.append(f)
    filtered=new_filtered
oxygen = int(filtered[0],2)

filtered = data.copy()
for i in range(len(bits)):
    new_filtered=[]
    x=[f[i] for f in filtered]
    req='1' if x.count('1')>=x.count('0') else '0'
    if len(filtered)==1: break
    for f in filtered:
        if f[i]!=req:
            new_filtered.append(f)
    filtered=new_filtered
carbon_dioxide = int(filtered[0],2)
print('Part 2:',oxygen*carbon_dioxide)