from Intcode import Intcode,load_intcode

VERBOSE=False
continuous_video_feed=False

if continuous_video_feed and not VERBOSE:
    print('Warning: continuous_video_feed is useless without VERBOSE')
    VERBOSE=True

CODE=load_intcode("17.txt")

class Scaffold(Intcode):
    def __init__(self, stdin=''):
        super().__init__(CODE)
        del self._out_q
        del self._in_q
        self.out=""
        self.stdin=iter(stdin)
    def _4(s):
        if s.out[-2:]=="\n\n":
            if VERBOSE: print(s.out)
            s.out=''
        s.out+=chr(s._code[s.par(1)])
        s._i+=2
    def _3(s):
        s._code[s.par(1)]=ord(next(s.stdin))
        s._i+=2

camera = Scaffold()
camera.run()
if VERBOSE: print(camera.out)

rows=camera.out.splitlines()
total=0
for x in range(1,len(rows[0])-1):  # No intersections at extremities
    for y in range(1,len(rows)-1):
        if rows[y][x]=='#':
            if '#'==rows[y][x-1]==rows[y][x+1]==rows[y-1][x]==rows[y+1][x]:
                total+=x*y
        elif rows[y][x]=='^':
            start_xy=(x,y)
print(f"Part 1: {total}")


#--- Uncompressed instructions ---
# I could have automated this process, but that would take longer than
# just created the instructions by hand
instructions='''
R,10,L,12,R,6,R,10,L,12,R,6,R,6,R,10,R,12,R,6,R,10,L,12,L,12,R,6,R,10,R,12,R,6,R
,10,L,12,L,12,R,6,R,10,R,12,R,6,R,10,L,12,L,12,R,6,R,10,R,12,R,6,R,10,L,12,R,6
'''.replace('\n','')

# Find repeated substrings, which would make good functions
substrs=[]
s,e=0,3
ins_list=instructions.split(',')
while e<len(ins_list):
    sub=",".join(ins_list[s:e])
    c=instructions.count(sub)
    if c>1 and len(sub)<21:
        substrs.append((c,sub))
        e+=1
    else:
        s=e
        e=s+3
substrs=list(set(substrs))  # Deduplicate
substrs.sort(reverse=True)
if VERBOSE:
    for c,s in substrs:
        print(f"{c:2d}: {s}")

# Find a set of functions that fully cover the instructions
# (It finds the same combo 6 times)
for _,A in substrs:
    for _,B in substrs:
        for _,C in substrs:
            if instructions.replace(A,'').replace(B,'').replace(C,'').replace(',','')=='':
                abc=A,B,C

A,B,C=abc

M=instructions.replace(A,'A').replace(B,'B').replace(C,'C')
n='\n'
cvf='y' if continuous_video_feed else 'n'
stdin = M+n+A+n+B+n+C+n+cvf+n
roomba = Scaffold(stdin=stdin)
roomba._code[0]=2  # Wake up
roomba.run()
print('Part 2:',ord(roomba.out))