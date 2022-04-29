from day24_input import *

DEBUG = False
## TESTING ##
#immune_system = [
#(17,5390,dict(weak=(radiation,bludgeoning)),4507,fire,2),
#(989,1274,dict(immune=(fire,),weak=(bludgeoning,slashing)),25,slashing,3),
#]

#infection = [
#(801,4706,dict(weak=(radiation,)),116,bludgeoning,1),
#(4485,2961,dict(immune=(radiation,),weak=(fire,cold)),12,slashing,4),
#]
#############

class Unit:
    def __init__(self, army, units, hp, imn_wk, damage, dtype, initiative, boost=0):
        self.army = army
        self.units = units
        self.hp = hp
        self.immunity = set(imn_wk.get('immune',()))
        self.weakness = set(imn_wk.get('weak',()))
        self.damage = damage + boost
        self.damage_type = dtype
        self.initiative = initiative
    def __repr__(self):
        return f"<{self.army} unit: {self.units} units; {self.hp} hp; {self.damage} {self.damage_type} damage>"
    def __str__(self):
        return f"""Unit: {self.army} army
 - HP:    {self.hp:>6}
 - UNITS: {self.units:>6}
 - DAMAGE:{self.damage:>6} {self.damage_type}
 - INIT:  {self.initiative:>6}
 - Immune:{tuple(self.immunity)}
 - Weak:  {tuple(self.weakness)}
"""
    def damage_dealt(self,enemy):
        return (self.units*self.damage
                *(not self.damage_type in enemy.immunity)  # 0 if immune
                *(1+(self.damage_type in enemy.weakness))) #*2 if weak
    def selection_order(self):
        return self.units*self.damage, self.initiative
    def target_order(self,enemy):
        return self.damage_dealt(enemy), enemy.units*enemy.damage, enemy.initiative
    def take_damage(self, damage):
        self.units-=damage//self.hp

def battle(boost=0):
    immune_army = [Unit('immune',*_,boost) for _ in immune_system]
    infect_army = [Unit('infect',*_) for _ in infection]
    all_units = immune_army+infect_army
    while immune_army and infect_army:
        selection_order = sorted(immune_army+infect_army, key=Unit.selection_order, reverse=True)
        available_targets = {'immune':infect_army.copy(),'infect':immune_army.copy()}
        pairings = []
        # TARGET
        for unit in selection_order:
            try:
                target = max(available_targets[unit.army],key=unit.target_order)
            except ValueError:
                ...
            else:
                if unit.damage_dealt(target)==0:
                    if DEBUG: print(unit,'skipped selection')
                    continue
                if DEBUG: print(f"{unit!r} is going to attack {target!r}")
                available_targets[unit.army].remove(target)
                pairings.append((unit,target))
        # ATTACK
        damage_dealt = False
        for unit, target in sorted(pairings, key=lambda _: -_[0].initiative):
            if unit.units>0: # Still has units
                old_units = target.units
                target.take_damage(unit.damage_dealt(target))
                damage_dealt = damage_dealt or old_units>target.units
                if DEBUG: print(f"{unit!r} attacked {target!r}")
        if not damage_dealt: break  # Avoid that infinite loop at boost 42
        # Clear the dead
        immune_army = [_ for _ in immune_army if _.units>0]
        infect_army = [_ for _ in infect_army if _.units>0]
    return sum(_.units for _ in immune_army),sum(_.units for _ in infect_army)

immune_score,infection_score = battle()
print('Part 1:',infection_score,flush=True)
boost = 1
while infection_score:
    immune_score,infection_score = battle(boost)
    print(boost,immune_score,infection_score,flush=True)
    boost+=1
print('Part 2:',immune_score)
# Part 1: 19974
# Part 2: 4606
