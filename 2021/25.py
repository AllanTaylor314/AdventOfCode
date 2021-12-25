with open('25.txt') as file:
    data = file.read()
easts = set()
souths = set()
empty = set()
for y,line in enumerate(data.splitlines()):
    for x,c in enumerate(line):
        if c=='>':
            easts.add((x,y))
        elif c=='v':
            souths.add((x,y))
        else:
            empty.add((x,y))
x_mod = x+1
y_mod = y+1
all_spaces = easts|souths|empty

def move():
    global easts,souths,empty,all_spaces
    done = True
    remove = set()
    add = set()
    for x,y in easts:
        new = ((x+1)%x_mod,y)
        if new in empty:
            remove.add((x,y))
            add.add(new)
            done = False
    empty-=add
    empty|=remove
    easts|=add
    easts-=remove
    assert not easts&empty
    remove = set()
    add = set()
    for x,y in souths:
        new = (x,(y+1)%y_mod)
        if new in empty:
            remove.add((x,y))
            add.add(new)
            done = False
    empty-=add
    empty|=remove
    souths|=add
    souths-=remove
    assert not souths&empty
    return done

c=1
while not move():
    c+=1
print('Part 1:',c)
