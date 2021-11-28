from time import perf_counter
part1=True
r3s=set()
start=perf_counter()

r3 = 0
r2=r3|65536
r3=14070682
while True:
    r1=r2&255
    r3+=r1
    r3&=16777215
    r3*=65899
    r3&=16777215
    if 256>r2:
        if r3 in r3s:
            break
        prev=r3
        r3s.add(r3)
        if part1:
            print(f'Part 1: {r3} ({perf_counter()-start}s)',flush=True)
            part1=False
        r2=r3|65536
        r3=14070682
    else:
        r1=0
        while True:
            r4=r1+1
            r4*=256
            if r4>r2:break
            r1+=1
        r2=r1
print(f'Part 2: {prev} ({perf_counter()-start}s)')
# Part 1: 6132825
# Part 2: 8307757