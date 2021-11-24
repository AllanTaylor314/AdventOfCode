from itertools import combinations
from math import ceil

shop="""
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
""".strip()

#### INPUT ####
boss="""
Hit Points: 109
Damage: 8
Armor: 2
""".strip()
###############

# RULES
# - Only 1 weapon
# - Armour optional
# - 0-2 Rings
# Max one of each (no duplicates)


# PARSE
weapons_str,armour_str,rings_str = shop.split('\n\n')

head,*weapon_strs = weapons_str.splitlines()
head,*armour_strs = armour_str.splitlines()
head,*rings_strs = rings_str.splitlines()

weapons = {name:(int(cost),int(damage),int(shield))
        for name,cost,damage,shield in map(str.split,weapon_strs)}
armour = {name:(int(cost),int(damage),int(shield))
        for name,cost,damage,shield in map(str.split,armour_strs)}
rings = {f"{name} {plus}":(int(cost),int(damage),int(shield))
        for name,plus,cost,damage,shield in map(str.split,rings_strs)}

boss_stats = tuple(map(int,boss.split()[2::2]))


armour['None'] = (0,0,0)

def fight(damage,shield,health=100,boss_stats=boss_stats):
    b_health,b_damage,b_shield = boss_stats
    turns = ceil(b_health/max(damage-b_shield,1))
    req_health = (turns-1)*(b_damage-shield)
    return req_health<health

# Fight
costs = []
loss_costs = []
for w_cost,w_damage,_w_shield in weapons.values():
    for a_cost,_a_damage,a_shield in armour.values():
        if fight(w_damage,a_shield):
            costs.append(w_cost+a_cost)
        else:
            loss_costs.append(w_cost+a_cost)
        for r_cost,r_damage,r_shield in rings.values():
            if fight(w_damage+r_damage,a_shield+r_shield):
                costs.append(w_cost+a_cost+r_cost)
            else:
                loss_costs.append(w_cost+a_cost+r_cost)
        for (r1_cost,r1_damage,r1_shield),(r2_cost,r2_damage,r2_shield) in combinations(rings.values(),2):
            r_cost=r1_cost+r2_cost
            r_damage=r1_damage+r2_damage
            r_shield=r1_shield+r2_shield
            if fight(w_damage+r_damage,a_shield+r_shield):
                costs.append(w_cost+a_cost+r_cost)
            else:
                loss_costs.append(w_cost+a_cost+r_cost)

print('Part 1:',min(costs))
print('Part 2:',max(loss_costs))