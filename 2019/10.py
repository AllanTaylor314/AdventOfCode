from math import gcd

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
boolify = {"#":1,".":0}.__getitem__
asteroid_map = [list(map(boolify,line)) for line in data]

counts = [(count_line_of_sight(x,y),x,y)
          for x in range(len(asteroid_map[0]))
          for y in range(len(asteroid_map))
          if asteroid_map[y][x]]
print("Part 1: {} visible from ({},{})".format(*max(counts)))