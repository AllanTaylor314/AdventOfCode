import re
from functools import cache

with open("19.txt") as file:
    lines = file.read().splitlines()
blueprints = [tuple(map(int,re.findall(r"\d+",line))) for line in lines]
@cache
def best(setup,time,ore=0,clay=0,obs=0,orebot=1,claybot=0,obsbot=0):
    if time==0:return 0
    bpid,ore_ore,clay_ore,obsidian_ore,obsidian_clay,geode_ore,geode_obsidian=setup
    if orebot>max(ore_ore,clay_ore,obsidian_ore) or claybot>obsidian_clay or obsbot>geode_obsidian:
        return 0 # u/jonathanpaulson If you create more than you can use, it is a bad idea
    out = best(setup,time-1,ore+orebot,clay+claybot,obs+obsbot,orebot,claybot,obsbot)
    if ore>=ore_ore:
        out = max(out,best(setup,time-1,ore+orebot-ore_ore,clay+claybot,obs+obsbot,orebot+1,claybot,obsbot))
    if ore>=clay_ore:
        out = max(out,best(setup,time-1,ore+orebot-clay_ore,clay+claybot,obs+obsbot,orebot,claybot+1,obsbot))
    if ore>=obsidian_ore and clay>=obsidian_clay:
        out = max(out,best(setup,time-1,ore+orebot-obsidian_ore,clay+claybot-obsidian_clay,obs+obsbot,orebot,claybot,obsbot+1))
    if ore>=geode_ore and obs>=geode_obsidian:
        out = max(out,best(setup,time-1,ore+orebot-geode_ore,clay+claybot,obs+obsbot-geode_obsidian,orebot,claybot,obsbot)+(time-1)) # A new geobot
    return out

p1 = 0
for bp in blueprints:
    geodes = best(bp,24)
    best.cache_clear()
    print(f"Blueprint {bp[0]} can produce {geodes} geodes in 24 minutes")
    p1+=bp[0]*geodes
print("Part 1:",p1)
p2 = 1
for bp in blueprints[:3]:
    geodes = best(bp,32)
    best.cache_clear()
    print(f"Blueprint {bp[0]} can produce {geodes} geodes in 32 minutes")
    p2*=geodes
print("Part 2:",p2)
