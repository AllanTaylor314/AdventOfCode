from collections import deque

WALLS = set()

class IterQueue:
    def __init__(self,*args):
        self._deque = deque(*args)
    def enqueue(self, item):
        self._deque.append(item)
    def dequeue(self):
        return self._deque.popleft()
    def __iter__(self):
        return self
    def __next__(self):
        try:
            return self.dequeue()
        except IndexError:
            raise StopIteration
    def __repr__(self):
        return repr(self._deque).replace(self._deque.__class__.__name__,self.__class__.__name__)

class CombatEnded(Exception):
    pass

def adjacent_spaces(x,y):
    return [(x+dx,y+dy) for dy,dx in [(-1,0),(0,-1),(0,1),(1,0)]]

class Combatant:
    hit_points = 200
    damage = 3
    locations = {}
    is_dead = False
    def __init__(self,xy):
        self.x,self.y = xy
        self.locations[self.x,self.y]=self
    
    # MOVEMENT
    def move(self):
        try:
            suggested_step = next(self.bfs_targets())[1]
        except (StopIteration, IndexError):
            return # Already in range - do nothing
        del self.locations[self.x,self.y]
        self.x,self.y = suggested_step
        self.locations[self.x,self.y]=self
    def adj_spaces(self):
        """List of spaces adjacent to oneself (where an enemy could attack from)"""
        return adjacent_spaces(self.x,self.y)
    def target_squares(self):
        """Yields locations that you could attempt to move to"""
        for xy, target in self.locations.items():
            if self.is_enemy(target):
                yield from target.adj_spaces()
    def bfs_targets(self):
        """Try up, left, right, down"""
        # Gen targets
        target_locs = set(self.target_squares())
        if not target_locs:
            raise CombatEnded
        # Try to get there
        blocked = WALLS|set(self.locations)
        q = IterQueue([[(self.x,self.y)]])
        for path in q:
            x,y = path[-1]
            if (x,y) in target_locs:
                yield path
                continue
            for step in adjacent_spaces(x,y):
                if step not in blocked and not step in path:
                    q.enqueue(path+[step])
                    blocked.add(step) # Don't go in circles
    # ATTACKS
    def attack(self):
        try:
            target = min(self.adjacent_enemies(),key=Combatant.key_fight)
        except ValueError:
            return # No attack, no enemies in range
        target.take(self.damage)
    def is_enemy(self, suspect):
        return isinstance(suspect, Combatant) and\
               not isinstance(suspect, type(self))
    def adjacent_enemies(self):
        for xy in adjacent_spaces(self.x,self.y):
            if (target:=self.locations.get(xy)) is not None\
               and self.is_enemy(target):
                yield target
    def key_turn(self):
        """Sort key used for combat turns"""
        return self.y,self.x
    def key_fight(self):
        """Sort key used for attack targets"""
        return self.hit_points, self.y, self.x
    def take(self,damage):
        self.hit_points-=damage
        if self.hit_points<=0:
            self.is_dead = True
            del self.locations[self.x,self.y]
    def __repr__(self):
        return f"{self.__class__.__name__}: ({self.x},{self.y}); HP:{self.hit_points}"+" (Dead)"*self.is_dead
class Elf(Combatant):
    pass
class Goblin(Combatant):
    pass

with open('15.txt') as file:
    data = file.read().splitlines()

cavern_map = [list(row) for row in data]

opens = set()
goblins = set()
elves = set()
loc_sets = {'#':WALLS,'.':opens,'G':goblins,'E':elves}
for y,line in enumerate(data):
    for x,c in enumerate(line):
        loc_sets[c].add((x,y))

combatants = list(map(Elf,elves))+list(map(Goblin,goblins))

rounds = 0
try:
    while True:
        combatants = [c for c in combatants if not c.is_dead] # Remove dead guys
        combatants.sort(key=Combatant.key_turn)
        for combatant in combatants:
            if combatant.is_dead: continue # Skip recently dead guys
            combatant.move()
            combatant.attack()
        rounds+=1
except CombatEnded:
    hp_sum = sum(c.hit_points for c in combatants if not c.is_dead)
    print('Part 1:',rounds*hp_sum)

# 191575