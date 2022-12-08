with open("08.txt") as file:
    lines = file.read().splitlines()

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

print("Part 1:",len(visible))
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

print("Part 2:",max(scenic_score(x,y) for x in range(len(lines[0])) for y in range(len(lines))))
