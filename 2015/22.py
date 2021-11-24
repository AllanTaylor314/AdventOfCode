from copy import deepcopy
from queue import Queue

VERBOSE = False

ACTIONS = ('Magic Missile','Drain','Shield','Poison','Recharge')

####### INPUT #######
boss_hit_points = 58
boss_damage = 9
#####################

MAGIC_MISSILE = 0
#     Cost:  53
#   Damage:   4

DRAIN = 1
#     Cost:  73
#   Damage:   2
#     Heal:   2

SHIELD = 2
#     Cost: 113
#    Armor:   7
# Duration:   6

POISON = 3
#     Cost: 173
#   Damage:   3
# Duration:   6

RECHARGE = 4
#     Cost: 229
# Duration:   5
#     Mana: 101

class Effect:
    def __hash__(self): return id(self)
    def __repr__(self): return f"<{type(self).__name__}: duration={self.duration}>"

class EffectShield(Effect):
    def __init__(self, wiz):
        self.duration = 6
        wiz.shield=7
        wiz.mana-=113
        if wiz.mana<0: raise ValueError
        wiz.mana_used+=113
    def use(self,wiz):
        if self.duration:
            wiz.shield=7
            self.duration-=1
            if VERBOSE:
                print(f'Shield is active, timer is {self.duration}')
            if self.duration==0:
                wiz.shield=0
                if VERBOSE: print('Shield lapsed')
                return False
            return True
        

class EffectPosion(Effect):
    def __init__(self, wiz):
        self.duration = 6
        wiz.mana-=173
        if wiz.mana<0: raise ValueError
        wiz.mana_used+=173
    def use(self, wiz):
        if self.duration>0:
            wiz.boss_health-=3
            self.duration-=1
            if VERBOSE: print(f'Poison deals 3 damage, timer is {self.duration}')
        return bool(self.duration)

class EffectRecharge(Effect):
    def __init__(self, wiz):
        self.duration = 5
        wiz.mana-=229
        if wiz.mana<0: raise ValueError
        wiz.mana_used+=229
    def use(self, wiz):
        if self.duration>0:
            wiz.mana+=101
            self.duration-=1
            if VERBOSE: print(f'Recharge adds 101 mana, timer is {self.duration}')
        return bool(self.duration)

EFFECTS = [type(None), type(None), EffectShield, EffectPosion, EffectRecharge]

class WizardSimulator:
    def __init__(self):
        self.mana_used = 0
        self.mana = 500
        self.boss_health = boss_hit_points
        self.boss_damage = boss_damage
        self.health = 50
        self.shield = 0
        self.player_turn = True
        self.effects = []
        self.actions = []

    def play_player(self, action):
        self.actions.append(action)
        assert self.player_turn
        self.player_turn = False
        if VERBOSE:
            print('-- Player turn --')
            print(f'- Player has {self.health} hit points, {self.shield} armour, {self.mana} mana')
            print(f'- Boss has {self.boss_health} hit points')
        effects = self.effects
        self.effects = []
        for effect in effects:
            if effect.use(self):
                self.effects.append(effect)
                if isinstance(effect, EFFECTS[action]):
                    raise ValueError
        if self.boss_health<=0:
            return True
        if action==MAGIC_MISSILE:
            self.mana_used+=53
            self.mana-=53
            self.boss_health-=4
        elif action==DRAIN:
            self.mana_used+=73
            self.mana-=73
            self.boss_health-=2
            self.health+=2
        else:
            self.effects.append(EFFECTS[action](self))
        if VERBOSE:print(f'Player casts {ACTIONS[action]}\n')
        if self.mana<0:
            raise ValueError
        if self.boss_health<=0:
            return True
        return self.play_boss()  # Auto advance

    def play_boss(self):
        assert not self.player_turn
        self.player_turn = True
        if VERBOSE:
            print('-- Boss turn --')
            print(f'- Player has {self.health} hit points, {self.shield} armour, {self.mana} mana')
            print(f'- Boss has {self.boss_health} hit points')
        effects = self.effects
        self.effects = []
        for effect in effects:
            if effect.use(self):
                self.effects.append(effect)
        if self.boss_health<=0:
            return True
        self.health-=self.boss_damage-self.shield
        if VERBOSE: print(f'Boss deals {self.boss_damage-self.shield} damage\n')
        if self.health<=0:
            return False
    
    def __repr__(self):
        effect_str = '\n - '.join(map(repr,self.effects))
        return f"""WizardSimulator
Boss:   {self.boss_health:3d} health
Player: {self.health:3d} health
        {self.mana:3d} mana ({self.mana_used} used)
        {self.shield:3d} armour
Effects:
 - {effect_str or None}

Awaiting {"Player's" if self.player_turn else "Boss's"} move
"""

w=WizardSimulator()
# TESTING
#VERBOSE = True
#x=WizardSimulator()
#x.health=10
#x.mana=250
#x.boss_health=13
#x.boss_damage=8
#x.play_player(POISON)
#x.play_player(MAGIC_MISSILE)
#print(f'\n{x}\n\n')
#y=WizardSimulator()
#y.health=10
#y.mana=250
#y.boss_health=14
#y.boss_damage=8
#y.play_player(RECHARGE)
#y.play_player(SHIELD)
#y.play_player(DRAIN)
#y.play_player(POISON)
#y.play_player(MAGIC_MISSILE)
#print(f'\n{y}')
#quit()
##########
q=Queue()
q.put(w)
mana_used = []
min_mana_used = 1362+1  # Known too high
while not q.empty():
    if q.qsize()%1000==0:print(f"Queue @ {q.qsize()} items")
    w=q.get_nowait()
    for action in range(5):
        w_copy = deepcopy(w)
        try:
            result=w_copy.play_player(action)
        except ValueError:  # Invalid move due to mana
            continue  # Skip over this action
        if result is True:
            print(f'Won a game using {w_copy.mana_used}')
            if w_copy.mana_used<min_mana_used:
                min_mana_used=w_copy.mana_used
                best_copy = w_copy
            mana_used.append(w_copy.mana_used)  # We won :)
        elif result is False:
            pass # Lost the game :(
        else: # i.e. None
            if w_copy.mana_used<min_mana_used:
                q.put(w_copy)  # Only add games that are getting better
part1 = min_mana_used
print('Part 1:', part1)

# 854 too low
# 967 too low  - Allowing multiple concurrent spells
# 1362 too high
# Part 1: 1269  - Was accidentally preventing cast new spell on expiration

class HardWizardSimulator(WizardSimulator):
    def __init__(self):
        super().__init__()
    def play_player(self, action):
        self.health-=1
        if self.health<=0:
            return False
        return super().play_player(action)

w=HardWizardSimulator()
q=Queue()
q.put(w)
mana_used = []
min_mana_used = 20000
while not q.empty():
    if q.qsize()%1000==0:print(f"Hard Queue @ {q.qsize()} items")
    w=q.get_nowait()
    for action in range(5):
        w_copy = deepcopy(w)
        try:
            result=w_copy.play_player(action)
        except ValueError:  # Invalid move due to mana
            continue  # Skip over this action
        if result is True:
            print(f'Won a hard game using {w_copy.mana_used}')
            if w_copy.mana_used<min_mana_used:
                min_mana_used=w_copy.mana_used
                best_copy = w_copy
            mana_used.append(w_copy.mana_used)  # We won :)
        elif result is False:
            pass # Lost the game :(
        else: # i.e. None
            if w_copy.mana_used<min_mana_used:
                q.put(w_copy)  # Only add games that are getting better
print()
print('Part 1:', part1)
print('Part 2:', min(mana_used), min_mana_used)
# 1362 too high
# Part 2: 1309 - Shield didn't wear off at the right time