# def count(line):
#     c=0
#     m=0 # max so far
#     for h in map(int,line): # counting trees twice!!!!
#         if h>m:
#             c+=1
#             m=h
#     return c

# def count(line): # Still counting outer things twice!!!!!!!
#     c=set()
#     m=-1 # max so far
#     for i,h in enumerate(map(int,line)):
#         if h>m:
#             c.add(i)
#             m=h
#     m=-1 # max so far
#     for i,h in reversed(list(enumerate(map(int,line)))):
#         if h>m:
#             c.add(i)
#             m=h
#     return len(c)

with open("08.txt") as file:
    lines = file.read().splitlines()
# lines = """30373
# 25512
# 65332
# 33549
# 35390
# """.splitlines()
grid = {x+y*1j:int(h) for y,row in enumerate(lines) for x,h in enumerate(row)}

visible = set()
for x in range(len(lines[0])):
    max_for_row = -1
    for y in range(len(lines)):
        if grid[x+y*1j]>max_for_row:
            visible.add(x+y*1j)
            max_for_row = grid[x+y*1j]
    max_for_row = -1
    for y in reversed(range(len(lines))):
        if grid[x+y*1j]>max_for_row:
            visible.add(x+y*1j)
            max_for_row = grid[x+y*1j]
for y in range(len(lines)):
    max_for_col = -1
    for x in range(len(lines[0])):
        if grid[x+y*1j]>max_for_col:
            visible.add(x+y*1j)
            max_for_col = grid[x+y*1j]
    max_for_col = -1
    for x in reversed(range(len(lines[0]))):
        if grid[x+y*1j]>max_for_col:
            visible.add(x+y*1j)
            max_for_col = grid[x+y*1j]

# for row in lines:
#     p1+=count(row)
# for col in zip(*lines):
#     p1+=count(col)
p1=len(visible)
print("Part 1:",p1)
def scenic_score(x,y):
    count_right = count_left = count_up = count_down = 0
    for i in range(x+1,len(lines[0])): # right
        if grid[i+y*1j]<grid[x+y*1j]:
            count_right+=1
        else:
            count_right+=1
            break
    for i in range(x-1,-1,-1): # left
        if grid[i+y*1j]<grid[x+y*1j]:
            count_left+=1
        else:
            count_left+=1
            break
    for j in range(y+1,len(lines)):
        if grid[x+j*1j]<grid[x+y*1j]:
            count_down += 1
        else:
            count_down += 1
            break
    for j in range(y-1,-1,-1):
        if grid[x+j*1j]<grid[x+y*1j]:
            count_up += 1
        else:
            count_up += 1
            break
    return count_right * count_left * count_up * count_down
p2 = max(scenic_score(x,y) for x in range(len(lines[0])) for y in range(len(lines)))

print("Part 2:",p2)
