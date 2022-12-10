with open("10.txt") as file:
    lines = file.read().splitlines()

p1 = 0
clock = 0
x = 1
clocks_that_matter = range(20,221,40)
def do_clock():
    global p1,clock,x,clocks_that_matter
    print(end="██" if abs(clock%40-x)<=1 else "  ")
    clock+=1
    if clock in clocks_that_matter:p1+=x*clock
    if clock%40==0:print()
for line in lines:
    if line=="noop":
        do_clock()
    else:
        do_clock()
        do_clock()
        x+=int(line.split()[1])
print("Part 1:",p1)
