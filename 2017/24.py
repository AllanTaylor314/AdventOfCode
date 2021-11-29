class Bridge:
    component_drawers={}
    def __init__(self,base_bridge=None):
        if base_bridge is None:
            global ROOT
            base_bridge=[ROOT]
        self._components = base_bridge.copy()
    def next_components(self):
        if len(self._components)>1:
            return list(self.component_drawers[self._components[-1].free_end(self._components[-2])]-set(self._components))
        if self._components:
            return list(self._components[-1].connectable_components)
        return list(self.component_drawers[0])
    def fork(self):
        for nc in self.next_components():
            b=Bridge(self._components)
            b._components.append(nc)
            yield b
    def __repr__(self):
        return ' => '.join(map(str,self._components))
    def __len__(self):
        return len(self._components)
    def strength(self):
        return sum(sum(c.pins) for c in self._components)

class Component:
    def __init__(self, pins):
        self.pins=pins
        self.pin_set=set(pins)
        self.connectable_components=set()
        self.strength=sum(pins)
        for pin in pins:
            if pin not in Bridge.component_drawers:
                Bridge.component_drawers[pin]=set()
            Bridge.component_drawers[pin].add(self)
    def __repr__(self):
        return f'Component({self.pins})'
    def __str__(self):
        return "{}/{}".format(*self.pins)
    def connectable(self,other):
        return len(self.pin_set&other.pin_set)==1  # Don't connect to itself
    def free_end(self,other):
        # Double ended connectors
        if self.pins[0]==self.pins[1]: return self.pins[0]
        return (self.pin_set-other.pin_set).pop()

ROOT=Component((0,0))

with open('24.txt') as file:
    data = file.read()

components=[Component(tuple(map(int,l.split('/')))) for l in data.splitlines()]

for c1 in components:
    for c2 in components:
        if c1.connectable(c2):
            c1.connectable_components.add(c2)
    if ROOT.connectable(c1):
        ROOT.connectable_components.add(c1)

from queue import Queue
q=Queue()
bridge = Bridge()
len_strengths = []
q.put(bridge)
while q.qsize():
    b=q.get_nowait()
    final=True
    for f in b.fork():
        final=False
        q.put(f)
    if final:
        len_strengths.append((len(b),b.strength()))
print('Part 1:',max(len_strengths,key=lambda x:x[1])[1])
print('Part 2:',max(len_strengths)[1])
