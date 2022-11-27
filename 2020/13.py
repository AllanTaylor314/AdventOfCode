def product(xs):
    a=1
    for x in xs: a*=x
    return a
with open("13.txt") as file:
    timestamp_str, bus_str = file.read().splitlines()
timestamp = int(timestamp_str)
buses = {i:int(b) for i,b in enumerate(bus_str.split(',')) if b!='x'}
p1 = min(buses.values(), key=lambda b:-timestamp%b)
print("Part 1:", p1*(-timestamp%p1))
lcm = product(buses.values())
components = {}
for offset, frequency in buses.items():
    components[offset]=small_mod=lcm//frequency
    target = (-offset)%frequency
    while components[offset]%frequency!=target:
        components[offset]+=small_mod
print("Part 2:",sum(components.values())%lcm)
