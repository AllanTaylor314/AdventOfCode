from collections import defaultdict
from math import prod
import re

def edges(tile):
    left = "".join(row[0] for row in tile)
    right = "".join(row[-1] for row in tile)
    top = tile[0]
    bottom = tile[-1]
    return [left,right,top,bottom,left[::-1],right[::-1],top[::-1],bottom[::-1]]

def flipy(tile):return tile[::-1]
def flipx(tile):return [r[::-1] for r in tile]
def rot90(tile):
    rotile = [""]*len(tile[0])
    for row in tile[::-1]:
        for i,c in enumerate(row):
            rotile[i]+=c
    return rotile
def perms(tile):
    for _ in range(4):
        yield tile
        yield flipx(tile)
        tile = rot90(tile)

def trim(tile):
    return [row[1:-1] for row in tile[1:-1]]

with open("20.txt") as file:
    inputs = file.read().split("\n\n")[:-1]
tiles = {}
for i in inputs:
    header,*rows = i.splitlines()
    tile_id = int(header.split()[1][:-1])
    tiles[tile_id] = rows

edge_map = defaultdict(list)
for tile_id, tile in tiles.items():
    for edge in edges(tile):
        edge_map[edge].append(tile_id)

num_edges = defaultdict(int)
for edge, tile_ids in edge_map.items():
    if len(tile_ids)>1:
        for tile_id in tile_ids:
            num_edges[tile_id]+=1
for tile_id in num_edges: num_edges[tile_id]//=2

corners = {tile_id for tile_id, ne in num_edges.items() if ne==2}
print("Part 1:", prod(corners))

adj_tiles = defaultdict(set)
for edge, tile_ids in edge_map.items():
    for tile_id in tile_ids:
        for other_id in tile_ids:
            if tile_id!=other_id:
                adj_tiles[tile_id].add(other_id)

layout = {} # x+yj: tile_id, rotated_tile
top_left_id,*_ = corners # Pick a corner
for tile in perms(tiles[top_left_id]):
    left,_,top,*_ = edges(tile)
    if len(edge_map[left])==1==len(edge_map[top]): break
layout[0j] = top_left_id, tile
x=0;y=0
the_tile = trim(tile)
while True:
    _,right,_,bottom,*_ = edges(layout[complex(x,y)][1])
    if len(edge_map[right])==2:
        x+=1
    elif len(edge_map[bottom])==1:
        break
    else:
        x=0
        y+=1
        the_tile+=[""]*(len(tile)-2)
    if x==0:
        prev_id, prev_tile = layout[complex(x,y-1)]
        target = edges(prev_tile)[3] # bottom edge
        tile_id ,= filter(lambda n:prev_id!=n,edge_map[target])
        for tile in perms(tiles[tile_id]):
            if edges(tile)[2]==target: # top edge
                break
    else:
        prev_id, prev_tile = layout[complex(x-1,y)]
        target = edges(prev_tile)[1] # right edge
        tile_id ,= filter(lambda n:prev_id!=n,edge_map[target])
        for tile in perms(tiles[tile_id]):
            if edges(tile)[0]==target: # left edge
                break
    layout[complex(x,y)] = tile_id, tile
    trimmed_tile = trim(tile)
    for i,row in enumerate(trimmed_tile, start=-len(trimmed_tile)):
        the_tile[i]+=row
# The 78 and 77 in this regex are hardcoded for the 96x96 big tile
monster_matcher = re.compile(r"#(?=(?:.|\n){78}(?:(#).{4}(#)){3}(#)(#)(?:.|\n){77}(?:.(#).){6})")
for big_tile in perms(the_tile):
    big_str = "\n".join(big_tile)
    num_monsters=len(monster_matcher.findall(big_str))
    if num_monsters: break
monster_size = """
                  #
#    ##    ##    ###
 #  #  #  #  #  #
""".count('#')
print("Part 2:",big_str.count('#')-num_monsters*monster_size)
