from math import gcd, atan, pi, sqrt

def count_line_of_sight(obs_x,obs_y):
    global asteroid_map
    count=0
    for rise in range(-len(asteroid_map),len(asteroid_map)+1):
        for run in range(-len(asteroid_map[0]),len(asteroid_map[0])+1):
            if gcd(rise,run)==1:
                x,y=obs_x+run,obs_y+rise
                while x>=0 and y>=0:
                    try:
                        if asteroid_map[y][x]==1:
                            count+=1
                            #print(x,y)
                            break
                        y+=rise
                        x+=run
                    except IndexError:
                        break
    return count

with open('10.txt') as file:
    data = file.read().splitlines()

print("\n".join(data))

boolify = {"#":1,".":0}.__getitem__
asteroid_map = [list(map(boolify,line)) for line in data]
counts = [(count_line_of_sight(x,y),x,y)
          for x in range(len(asteroid_map[0]))
          for y in range(len(asteroid_map))
          if asteroid_map[y][x]]
num,ms_x,ms_y=max(counts)
print(f"Part 1: {num} visible from ({ms_x},{ms_y})")


""" New Plan:
Assign every asteroid an angle (atan(x/y), but with div/0 and quadrant handling)
and a distance (sqrt((x-x_0)**2+(y-y_0)**2)). Pop them in angle order, choosing
the closest and ignoring any with the same angle.
"""
import doctest
def get_theta_and_distance(rise,run):
    """
    >>> get_theta_and_distance(-1,0)[0]/pi
    0.0
    >>> get_theta_and_distance(-1,1)[0]/pi
    0.25
    >>> get_theta_and_distance(0,1)[0]/pi
    0.5
    >>> get_theta_and_distance(1,1)[0]/pi
    0.75
    >>> get_theta_and_distance(1,0)[0]/pi
    1.0
    >>> get_theta_and_distance(1,-1)[0]/pi
    1.25
    """
    distance = sqrt(rise**2+run**2)
    if (g:=gcd(rise,run))!=1:
        rise//=g
        run//=g
    if rise==0:
        theta = pi/2 if run>0 else pi*3/2
    elif run==0:
        theta = pi if rise>0 else 0
    else:
        theta = -atan(run/rise)
        if rise>0:
            if run>0:
                # pi/2 .. pi
                theta = pi/2+atan(abs(rise/run))
            else:
                # pi .. 3*pi/2
                theta = pi+atan(abs(run/rise))
        else:
            if run>0:
                # 0..pi
                theta = atan(abs(run/rise))
            else:
                # 3*pi/2..2*pi (0)
                theta = 3*pi/2+atan(abs(rise/run))
    return theta, distance

doctest.testmod()

def print_blast(x,y):
    global asteroid_map
    local_map = asteroid_map
    assert local_map[y][x]
    local_map[y][x]=4
    strify=' 0*@X'.__getitem__
    print(*("".join(map(strify,_)) for _ in local_map),sep="\n")
    local_map[y][x]=2

asteroids = [(x,y)
          for x in range(len(asteroid_map[0]))
          for y in range(len(asteroid_map))
          if asteroid_map[y][x]]
asteroids.remove((ms_x,ms_y))
asteroid_map[ms_y][ms_x]=3
ang_dist = [tuple([*get_theta_and_distance(y-ms_y,x-ms_x),x,y]) for x,y in asteroids]
ang_dist.sort()

blasts = 0
i = 0
while blasts<200:
    theta,dist,x,y=ang_dist.pop(i)
    blasts+=1
    xy=100*x+y
    print(f"Zap {blasts:3d}! bearing {theta:7.4f}, distance {dist:7.4f} destroyed! ({xy:04d})")
    print_blast(*divmod(xy,100))
    while ang_dist[i][0]==theta:
        i+=1
        i%=len(ang_dist)
    i%=len(ang_dist)

print(f"{x,y=}")
print(f"Part 2: {x*100+y}")