import os
from pathlib import Path
from time import perf_counter
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
timer_parse_start=perf_counter()
############################## PARSER ##############################
def parse_block(block:str):
    top, *lines = block.splitlines()
    dst,_,src = top.split()[0].split('-')
    body = [tuple(map(int,line.split())) for line in lines]
    return dst,src,body

with open(INPUT_PATH) as file:
    header,*blocks = file.read().split("\n\n")

seeds = list(map(int,header.split()[1:]))
data = list(map(parse_block,blocks)) # maps are in logical order

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################
class RangeMap:
    def __init__(self,dst,src,size):
        self.dst = dst
        self.src = src
        self.size = size
    def __contains__(self,key):
        return self.src <= key < self.src+self.size
    def __getitem__(self,key):
        if key not in self:
            raise KeyError()
        return self.dst + key - self.src
    def __repr__(self):
        return f"RangeMap({self.dst}, {self.src}, {self.size})"
    @property
    def start(self):
        return self.src
    @property
    def end(self):
        return self.src+self.size

things = seeds
for in_type, out_type, mapping in data:
    new_things = []
    ranges = [RangeMap(*q) for q in mapping]
    for thing in things:
        for rang in ranges:
            if thing in rang:
                new_things.append(rang[thing])
                break
        else:
            new_things.append(thing) # no mapping: same
    print(things)
    things = new_things
p1 = min(things)
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
p2 = 0
seed_pairs = list(zip(seeds[::2],seeds[1::2]))
class SimpleRange:
    def __init__(self,start,size):
        self.start = start
        self.size = size
    def __add__(self,num):
        return SimpleRange(self.start+num,self.size)
    def __repr__(self):
        return f"SimpleRange({self.start}, {self.size})"
    def __contains__(self, val):
        return self.start<=val<self.end
    @property
    def end(self):
        return self.start+self.size

class MultiRange:
    def __init__(self, ranges:"list[SimpleRange|MultiRange]"):
        self.ranges = []
        for rang in ranges:
            if isinstance(rang, SimpleRange):
                self.ranges.append(rang)
            elif isinstance(rang, MultiRange):
                self.ranges.extend(rang.ranges)
            else:
                raise TypeError()
    def __add__(self, num):
        return MultiRange(rang+num for rang in self.ranges)
    def __repr__(self):
        return f"MultiRange({self.ranges!r})"
    def min(self):
        return min(r.start for r in self.ranges)

class MultiRangeMap:
    def __init__(self, range_maps:"list[RangeMaps]"):
        self.range_maps = range_maps.copy()
    def __getitem__(self, item):
        if isinstance(item, int):
            for range_map in self.range_maps:
                try:
                    return range_map[item]
                except KeyError:
                    pass
            return item # not in range
        
        if isinstance(item, SimpleRange):
            cut_locations = [item.start]
            start = item.start
            end = item.end
            for range_map in self.range_maps:
                if range_map.start <= end and range_map.end >= start:
                    if range_map.start in item:
                        cut_locations.append(range_map.start)
                    if range_map.end in item:
                        cut_locations.append(range_map.end)
            cut_locations.append(item.end)
            cut_locations = sorted(set(cut_locations))
            return MultiRange([SimpleRange(self[i],j-i) for i,j in zip(cut_locations,cut_locations[1:])])

        if isinstance(item, MultiRange):
            return MultiRange([self[rang] for rang in item.ranges])

mr = seed_multirange = MultiRange([SimpleRange(*pair) for pair in seed_pairs])
maps = [MultiRangeMap([RangeMap(*d) for d in c]) for a,b,c in data]
for m in maps:
    mr = m[mr]
p2 = mr.min()
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
