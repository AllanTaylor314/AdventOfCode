with open('15.txt') as file:
    data = file.read().splitlines()

nutrition = {}
for line in data:
    name, stats = line.split(': ')
    #cap,dur,flav,tex,cal = 
    nutrition[name]=tuple(map(int,stats.replace(',','').split()[1::2]))

def score(**kwargs):
    global nutrition
    cap,dur,flv,tex = (0,)*4
    for name,q in kwargs.items():
        c,d,f,t,_=nutrition[name]
        cap+=q*c
        dur+=q*d
        flv+=q*f
        tex+=q*t
    if cap<0 or dur<0 or flv<0 or tex<0:
        return 0
    return cap*dur*flv*tex

scores = []
for a in range(101):
    for b in range(101-a):
        for c in range(101-a-b):
            d = 100-a-b-c
            assert a+b+c+d==100
            s=score(
                Sprinkles = a,
                Butterscotch = b,
                Chocolate = c,
                Candy = d
            )
            if s:scores.append(s)
print('Part 1:',max(scores))

def score_cal(**kwargs):
    global nutrition
    cap,dur,flv,tex,cal = (0,)*5
    for name,q in kwargs.items():
        c,d,f,t,e=nutrition[name]
        cap+=q*c
        dur+=q*d
        flv+=q*f
        tex+=q*t
        cal+=q*e
    if cal!=500 or cap<0 or dur<0 or flv<0 or tex<0:
        return 0
    return cap*dur*flv*tex

scores_cal = []
for a in range(101):
    for b in range(101-a):
        for c in range(101-a-b):
            d = 100-a-b-c
            assert a+b+c+d==100
            s=score_cal(
                Sprinkles = a,
                Butterscotch = b,
                Chocolate = c,
                Candy = d
            )
            if s:scores_cal.append(s)
print('Part 2:',max(scores_cal))