from time import perf_counter

def addr(reg,a,b,c): reg[c]=reg[a]+reg[b]
def addi(reg,a,b,c): reg[c]=reg[a]+b
def mulr(reg,a,b,c): reg[c]=reg[a]*reg[b]
def muli(reg,a,b,c): reg[c]=reg[a]*b
def banr(reg,a,b,c): reg[c]=reg[a]&reg[b]
def bani(reg,a,b,c): reg[c]=reg[a]&b
def borr(reg,a,b,c): reg[c]=reg[a]|reg[b]
def bori(reg,a,b,c): reg[c]=reg[a]|b
def setr(reg,a,b,c): reg[c]=reg[a]
def seti(reg,a,b,c): reg[c]=a
def gtir(reg,a,b,c): reg[c]=int(a>reg[b])
def gtri(reg,a,b,c): reg[c]=int(reg[a]>b)
def gtrr(reg,a,b,c): reg[c]=int(reg[a]>reg[b])
def eqir(reg,a,b,c): reg[c]=int(a==reg[b])
def eqri(reg,a,b,c): reg[c]=int(reg[a]==b)
def eqrr(reg,a,b,c): reg[c]=int(reg[a]==reg[b])
def operate(ops,reg):
    op,a,b,c=ops
    globals()[op](reg,a,b,c)

with open('19.txt') as file:
    data = file.read()

header,*lines = data.splitlines()
ip = int(header.split()[1])
program = []
for line in lines:
    op,*pars=line.split()
    program.append([op]+list(map(int,pars)))

start1 = perf_counter()

reg=[0]*6;reg[0]=1
while reg[ip] in range(len(program)):
    tmp = reg[ip]
    #print(f"ip={tmp}")
    #print(reg,'(before)')
    #print(*program[tmp])
    operate(program[tmp],reg)
    #print(reg,'(after)')
    #print()
    reg[ip]+=1  # Only works when #ip is not 0
    print("{:2d} [{:5d},{:5d},{:5d},{:5d},{:5d},{:5d}]".format(tmp,*reg))

end1 = perf_counter()

print('Part 1:', reg[0], f'(Time taken: {end1-start1}s)', flush=True)

#start2 = perf_counter()
#reg=[1]+[0]*5
#while reg[ip] in range(len(program)):
    #tmp=reg[ip]
    #operate(program[reg[ip]],reg)
    #reg[ip]+=1
    #print("{:2d} [{:9d},{:9d},{:9d},{:9d},{:9d}]".format(tmp,*reg))
#end2 = perf_counter()
#print('Part 2:', reg[0], f'(Time taken: {end2-start2}s)')
#print(f'Total time: {end2-start1}')