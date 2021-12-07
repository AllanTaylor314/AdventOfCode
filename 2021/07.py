def cost2(start,end):
    n=abs(start-end)
    return n*(n+1)//2

with open('07.txt') as file:
    data=list(map(int,file.read().split(',')))

fuel=[]
fuel2=[]
for hp in range(min(data),max(data)+1):
    fuel.append(sum(map(abs,map(hp.__sub__,data))))
    fuel2.append(sum(cost2(hp,c) for c in data))
print('Part 1:',min(fuel))
print('Part 2:',min(fuel2))
