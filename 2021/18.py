from copy import deepcopy
class Node:
    __slots__=('v','x','y')
    def __init__(self,v=None,x=None,y=None):
        self.v=v
        self.x=x
        self.y=y
    def _iot(self):
        if self.x is not None:
            yield from self.x._iot()
        if self.v is not None:
            yield self
        if self.y is not None:
            yield from self.y._iot()
    def _d4t(self,d=0):
        if not self.is_leaf():
            if self.x is not None:
                yield from self.x._d4t(d+1)
            if d>=4 and self.x.is_leaf() and self.y.is_leaf():
                yield self
            if self.y is not None:
                yield from self.y._d4t(d+1)
    def split(self):
        v=self.v
        a=v//2
        b=v-a
        self.v=None
        self.x=Node(v=a)
        self.y=Node(v=b)
    def is_leaf(self):
        return self.v is not None is self.x is self.y
    def try_split(self,depth=0):
        if self.is_leaf():
            if self.v>=10:
                self.split()
                return True
            return False
        if self.x.try_split(depth+1):
            return True
        if self.y.try_split(depth+1):
            return True
        return False
    @classmethod
    def build_from(cls, array):
        if isinstance(array, list):
            a,b = array
            return cls(x=cls.build_from(a),y=cls.build_from(b))
        else:
            return cls(v=array)
    def __repr__(self):
        return f"[{self.x}, {self.y}]" if self.v is None else f"{self.v}"
    def magnitude(self):
        if self.is_leaf():
            return self.v
        return 3*self.x.magnitude()+2*self.y.magnitude()

class Tree:
    __slots__=('root',)
    def __init__(self, array=None):
        self.root = None if array is None else Node.build_from(array)
    def in_order_traversal(self):
        yield from self.root._iot()
    def depth_4_traversal(self):
        yield from self.root._d4t()
    def __add__(self,other):
        new=Tree()
        new.root = Node()
        new.root.x = deepcopy(self.root)
        if isinstance(other,list):
            new.root.y = Node.build_from(other)
        else:
            new.root.y = deepcopy(other.root)
        new.reduce()
        return new
    def __iadd__(self,other):
        self.root = Node(x=self.root,y=Node.build_from(other))
        self.reduce()
        temp_repr = repr(self)
        self.reduce()
        assert repr(self)==temp_repr
        return self
    def __repr__(self):
        return f"Tree({self.root})"
    def explode(self,target):
        prev = None
        iot=self.in_order_traversal()
        for n in iot:
            if n is target.x: break
            prev=n
        try:
            assert next(iot) is target.y
            nex = next(iot)
        except StopIteration:
            nex = None
        if prev is not None:
            prev.v+=target.x.v
        if nex is not None:
            nex.v+=target.y.v
        target.v=0
        target.x=None
        target.y=None
    def reduce(self):
        while True:
            try:
                target = next(self.depth_4_traversal())
            except StopIteration:
                pass
            else:
                self.explode(target)
                continue
            if self.root.try_split():
                continue
            break
    def magnitude(self):
        return self.root.magnitude()

with open('18.txt') as file:
    data = file.read()

homework = tuple(map(eval,data.splitlines()))

hw1=iter(homework)
tree = Tree(next(hw1))
for new in hw1:
    tree+=new
print('Part 1:',tree.magnitude(),flush=True)

hw2=list(map(Tree,homework))
mags = []
for a in hw2:
    for b in hw2:
        if a is b: continue
        mags.append((a+b).magnitude())
print('Part 2:',max(mags))
