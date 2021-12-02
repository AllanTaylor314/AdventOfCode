with open('02.txt') as file:
    data=file.read().splitlines()

x,d=0,0
for line in data:
    ins,num = line.split()
    num=int(num)
    if ins=='forward':
        x+=num
    elif ins=='down':
        d+=num
    else:
        d-=num
print('Part 1:',x*d)

x,d,aim=0,0,0
for line in data:
    ins,num = line.split()
    num=int(num)
    if ins=='forward':
        x+=num
        d+=aim*num
    elif ins=='down':
        aim+=num
    else:
        aim-=num
print('Part 2:',x*d)