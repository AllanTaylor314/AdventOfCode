from copy import deepcopy
class Node:
    """Node class:
        v: value       (None, int)
        x: left child  (Node, None)
        y: right child (Node, None)
    Either set v OR (x AND y)
    """
    __slots__=('v','x','y')
    def __init__(self,v=None,x=None,y=None):
        assert v is None or x is y is None
        self.v=v
        self.x=x
        self.y=y
    def _iot(self):
        """In order traversal - leaf nodes only"""
        if self.x is not None:
            yield from self.x._iot()
        if self.v is not None:
            yield self
        if self.y is not None:
            yield from self.y._iot()
    def _d4t(self,d=0):
        """depth>=4 (in order) traversal
        Every parent of two leaf nodes where the parent has a depth>=4
        """
        if not self.is_leaf(): # A leaf node is useless here
            if self.x is not None:
                yield from self.x._d4t(d+1)
            if d>=4 and self.x.is_leaf() and self.y.is_leaf():
                yield self
            if self.y is not None:
                yield from self.y._d4t(d+1)
    def split(self):
        """Split (in place)
        Turns one leaf node (self) into the parent of two leaf nodes
        (floor(v/2), ceil(v/2))"""
        v=self.v
        a=v//2
        b=v-a
        self.v=None
        self.x=Node(v=a)
        self.y=Node(v=b)
    def is_leaf(self):
        """Does this node have a value, not children"""
        return self.v is not None is self.x is self.y
    def try_split(self):
        """Recursively attempt to split a leaf if the value is
        at least 10
        Return True if the node (or a descendant of the node) is split"""
        if self.is_leaf():
            if self.v>=10:
                self.split()
                return True
            return False
        return self.x.try_split() or self.y.try_split()
    @classmethod
    def build_from(cls, array):
        """Turn a list of lists (len=2) OR ints into a tree structure"""
        if isinstance(array, list):
            a,b = array
            return cls(x=cls.build_from(a),y=cls.build_from(b))
        else:
            return cls(v=array)
    def __repr__(self):
        """Leaf nodes are represented by their contents
        Other nodes are represented by their children (recursively)"""
        return f"[{self.x}, {self.y}]" if self.v is None else f"{self.v}"
    def magnitude(self):
        """Magnitude of leaf nodes is their value
        Magnitude of other nodes is 3*mag_left+2*mag_right"""
        if self.is_leaf():
            return self.v
        return 3*self.x.magnitude()+2*self.y.magnitude()

class Tree:
    __slots__=('root',)
    def __init__(self, array=None):
        self.root = None if array is None else Node.build_from(array)
    def in_order_traversal(self):
        """All leaf nodes, in order"""
        yield from self.root._iot()
    def depth_4_traversal(self):
        """All parent nodes of two leaf nodes where the depth
        of the parent is at least 4 (i.e. child depth > 4)"""
        yield from self.root._d4t()
    def __add__(self,other):
        """Combine trees (or list in tree structure)
        Uses deepcopy to avoid side effects on new tree
        Calls reduce on new tree so that it is a valid
        Snailfish Number"""
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
        """Inplace add - only accepts list in tree structure
        Reduces tree to keep it as a valid Snailfish Number"""
        self.root = Node(x=self.root,y=Node.build_from(other))
        self.reduce()
        temp_repr = repr(self)
        self.reduce()
        assert repr(self)==temp_repr
        return self
    def __repr__(self):
        """The tree is literally a root node and some wrapper functions,
        so the repr reflects this fact"""
        return f"Tree({self.root})"
    def explode(self,target):
        """Any pair deeper than 4 is combined with the in order predecessor and
        in order successor of leaf nodes"""
        prev = None
        iot=self.in_order_traversal()
        for n in iot:
            if n is target.x: break
            prev=n
        # Eat the second half of the pair and ensure that it is a pair
        assert next(iot) is target.y
        try:
            nex = next(iot)
        except StopIteration: # No more leaves, oh well
            nex = None
        if prev is not None:
            prev.v+=target.x.v
        if nex is not None:
            nex.v+=target.y.v
        # Set the pair to be a leaf node with v=0
        target.v=0
        target.x=None
        target.y=None
    def reduce(self):
        """Working left to right, explode everything, then split anything
        If anything becomes explodable after a split, explode it
        If nothing explodes and nothing splits, we're done (break)"""
        while True:
            try:# Get the first explodable pair
                target = next(self.depth_4_traversal())
            except StopIteration:# No explosions :(
                pass
            else:# Yes Rico, Kaboom
                self.explode(target)
                continue
            # If a split happens, keep going
            if self.root.try_split():
                continue
            break # Nothing happened - I quit!
    def magnitude(self):
        """Find the magnitude of the tree (see Node.magnitude)"""
        return self.root.magnitude()

with open('18.txt') as file:
    data = file.read()
#       Scary stuff! vvvv
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
