from Intcode import Intcode,load_intcode

VERBOSE=True
PART1=False
PART2=True

CODE=load_intcode('19.txt')
SIZE=100
CACHE={}

def get_status(x,y):
    if (x,y) in CACHE: return CACHE[(x,y)]
    scanner = Intcode(CODE)  # Reinit for each run
    scanner.input(x)
    scanner.input(y)
    scanner.run()
    out=scanner.output()
    CACHE[(x,y)]=out
    return out

def verify(x,y):
    global SIZE
    return get_status(x,y) and get_status(x+SIZE-1,y) and \
           get_status(x,y+SIZE-1) and get_status(x+SIZE-1,y+SIZE-1)

if PART1:
    count=0
    for y in range(50):
        for x in range(50):
            out=get_status(x,y)
            if VERBOSE:print('.#'[out],end='')
            count+=out
        if VERBOSE:print()
    print('Part 1:',count,flush=True)

if not PART2:quit()
def find_square(x0=0,prev_x=10,STEP=10,y0=0,yf=1111,x_buffer=10):
    start_x=x0
    for y in range(y0,yf,STEP):
        #if VERBOSE:print(' '*start_x,end='') # Keep stuff in line
        if VERBOSE: print(f"{start_x},{y}: ",end="")
        await_start=True
        for x in range(start_x,prev_x+x_buffer):
            #print(x,y,get_status(x,y))
            out=get_status(x,y)
            if VERBOSE:print('.#'[out],end='')
            if await_start and out:
                await_start=False
                start_x=x
            if not await_start and not out:
                break
            if verify(x,y):
                return x,y
                #print(f'Part 2: {x*10000+y}')
            #if out and get_status(x+SIZE,y)and get_status(x,y+SIZE) and get_status(x+SIZE,y+SIZE):
                        #print(f'Look at {(x,y)}')
                        #quit()
            #if VERBOSE:print(' '*SIZE,end='')
        prev_x=x
        #if prev_x-start_x>2*SIZE:
            #print(start_x,y)
            #break  # Not quite done, but close
        if VERBOSE:print()

#x0,y0=find_square()
x0,y0=669,1100
x,y=find_square(x0=x0-100,prev_x=x0+100,STEP=1,y0=1090,yf=1110,x_buffer=100)
print(f'\nPart 2: {x*10000+y}')