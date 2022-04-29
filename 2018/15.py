from collections import deque

WALLS = set()
GOBLINS = set()
ELVES = set()
PART2 = False

class IterQueue:
    """Iterable queue - the power of queues with the simplicity of for loops
    
    You can add to this while iterating through it. As long as your loop will
    stop adding at some point, this iteration can also stop"""
    def __init__(self,*args):
        self._deque = deque(*args)
    def enqueue(self, item):
        self._deque.append(item)
    def dequeue(self):
        return self._deque.popleft()
    def __iter__(self):
        return self
    def __next__(self):
        try:return self.dequeue()
        except IndexError:raise StopIteration
    def __repr__(self):
        return repr(self._deque).replace(self._deque.__class__.__name__,self.__class__.__name__)

class CombatEnded(Exception):pass
class ElfDied(Exception):pass

def adjacent_spaces(x,y):
    """List of ajacent (x,y) coordinates,
    in reading order: up, left, right, down
    """
    return [(x+dx,y+dy) for dy,dx in [(-1,0),(0,-1),(0,1),(1,0)]]

class Combatant:
    hit_points = 200
    damage = 3
    locations = {}
    is_dead = False
    @classmethod
    def reset(cls):
        """Reset the locations dictionary, deleting all previous combatants
        Create new combatants from global sets"""
        cls.locations = {}
        deque(map(Elf,ELVES),maxlen=0)
        deque(map(Goblin,GOBLINS),maxlen=0)
    @classmethod
    def hp_sum(cls):
        """sum of the survivors hit points for calculating combat outcome"""
        return sum(c.hit_points for c in cls.locations.values() if not c.is_dead)
    @classmethod
    def print_state(cls):
        maxx,maxy = max(WALLS) # Assumes borders are all walls
        for y in range(maxy+1):
            for x in range(maxx+1):
                if (x,y) in WALLS:
                    print(end='#')
                elif (x,y) in cls.locations:
                    print(end=type(cls.locations[x,y]).__name__[0])
                else:
                    print(end='.')
            print()
    
    def __init__(self,xy):
        self.x,self.y = xy
        self.locations[self.x,self.y]=self
    
    # MOVEMENT
    def move(self):
        """Attempt to move towards the nearest opponent"""
        try:
            suggested_step = next(self.bfs_targets())[1]
        except (StopIteration, IndexError):
            return # Can't move or already in range - do nothing
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
        """The magic of the 'move' method
        Perform a breadth first search of the area
        Finds and yields possible paths to any opponent's adjacent space,
        shortest first, ties broken by reading order
        If no opponents are left, raises CombatEnded
        """
        # Generate targets
        target_locs = set(self.target_squares())
        if not target_locs:
            raise CombatEnded
        # Try to get there
        blocked = WALLS|set(self.locations) # Can't go through walls or others
        q = IterQueue([[(self.x,self.y)]]) # Start at current location
        for path in q:
            x,y = path[-1] # Current end of the path
            if (x,y) in target_locs:
                yield path
                continue
            for step in adjacent_spaces(x,y):
                if step not in blocked:
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
        """No friendly fire - is the suspect a different type"""
        return not isinstance(suspect, type(self))
    def adjacent_enemies(self):
        """Yields any enemies in attacking range"""
        for xy in adjacent_spaces(self.x,self.y):
            if (target:=self.locations.get(xy)) is not None\
               and self.is_enemy(target):
                yield target
    def take(self,damage):
        """When attacked, take some damage and check if dead"""
        self.hit_points-=damage
        if self.hit_points<=0:
            self.is_dead = True
            del self.locations[self.x,self.y]
    
    def key_turn(self):
        """Sort key used for combat turns (reading order)"""
        return self.y,self.x
    def key_fight(self):
        """Sort key used for attack targets (lowest hp, reading order)"""
        return self.hit_points, self.y, self.x
    def __repr__(self):
        return f"<{self.__class__.__name__}: ({self.x},{self.y}); HP:{self.hit_points}"+" (Dead)"*self.is_dead+">"

class Elf(Combatant):
    def take(self,damage):
        super().take(damage)
        if PART2 and self.is_dead:raise ElfDied
class Goblin(Combatant):
    pass


with open('15.txt') as file:
    data = file.read().splitlines()
loc_sets = {'#':WALLS,'.':set(),'G':GOBLINS,'E':ELVES}
for y,line in enumerate(data):
    for x,c in enumerate(line):
        loc_sets[c].add((x,y))


while True:
    Combatant.reset()
    rounds = 0
    try:
        while True:
            combatants=sorted(Combatant.locations.values(),key=Combatant.key_turn)
            for combatant in combatants:
                if combatant.is_dead: continue # Skip recently dead
                combatant.move()
                combatant.attack()
            rounds+=1
    except CombatEnded:
        print(f'Part {1+PART2}:',rounds*Combatant.hp_sum(), flush=True)
        if PART2: break # Once the elves win without any casualties, stop
        PART2=True
    except ElfDied:
        Elf.damage+=1 # Try again, with MORE POWER!

#Part 1: 191575
#Part 2: 75915
