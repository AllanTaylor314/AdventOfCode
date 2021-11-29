def manhattan_distance(a,b=None):
    if b is None: return sum(map(abs,a))
    d=0
    for j,k in zip(a,b):
        d+=abs(j-k)
    return d

def get_adjacent_coords(coord, out=None):
    global adjacency_dict
    if out is None: out=set()
    for adj_coord in adjacency_dict[coord]:
        if adj_coord not in out:
            out.add(adj_coord)
            get_adjacent_coords(adj_coord, out)
    return out

with open('25.txt') as file:
    data=file.read().splitlines()
coords = [tuple(map(int,l.split(','))) for l in data]
adjacency_dict = {}
for coord in coords:
    adjacency_dict[coord]=[]
    for other_coord in coords:
        if manhattan_distance(coord,other_coord)<=3:
            adjacency_dict[coord].append(other_coord)

constellation_dict={}
for coord in coords:
    constellation_dict[coord]=get_adjacent_coords(coord)

constellations = {tuple(sorted(tuple(adj))) for co,adj in constellation_dict.items()}
print(f'Part 1: {len(constellations)}')