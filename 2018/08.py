class Node:
    """A node that contains more nodes (children) and metadata"""
    def __init__(self, children=0, metadata=0):
        self.children=[]
        self._num_children=children
        self.metadata=[]
        self._num_metadata=metadata
    def __repr__(self):
        """Represent the tree in a linear fashion
        (num children, num metadata) [subtree] <metadata>
        Same order as the input"""
        return f"[({self._num_children}, {self._num_metadata}), {', '.join(map(repr, self.children))}{', ' if self.children else ''}<{', '.join(map(str,self.metadata))}>]"
    def add_child(self, child):
        """Wrapper for child append"""
        assert isinstance(child, type(self))
        self.children.append(child)
    def sum_metadata(self):
        """Recursive sum of metadata (for Part 1)"""
        return sum(self.metadata)+sum(map(Node.sum_metadata, self.children))
    def validate(self):
        """Verify that the tree is valid:
         - length of children correct
         - length of metadata correct
         - all subtrees valid ()
        """
        return len(self.children)==self._num_children and\
               len(self.metadata)==self._num_metadata and\
               all(n.validate() for n in self.children)
    def value(self):
        """Recursive 'value' as defined for Part 2
        if there are no children, the value is the sum of the metadata
        if there are children, the valus the is sum of child values
        using the 1-indexed metadata (ignore out of range metadata)
        """
        if self._num_children==0:
            return sum(self.metadata)
        return sum(self.children[i-1].value() for i in self.metadata if 0<i<=len(self.children))
    def collapse(self):
        """Return the representation of the tree as a list in the same format
        as the input."""
        tree = [self._num_children, self._num_metadata]
        for child in self.children:
            tree.extend(child.collapse())
        tree.extend(self.metadata)
        return tree

def build_tree(tree_list, start=0):
    """Recursive. Returns the length of the child subtree and the child node
    tree_list is a list of integers as given in the puzzle input
    start is the index of the first element of the node's data"""
    parent = Node(*tree_list[start:start+2])
    num_children = tree_list[start]
    num_metadata = tree_list[start+1]
    node = Node(num_children,num_metadata)
    if num_children==0:
        node.metadata.extend(tree_list[start+2:start+2+num_metadata])
        return 2+num_metadata, node
    len_subtree=2
    for i in range(num_children):
        l,n = build_tree(tree_list, start+len_subtree)
        node.add_child(n)
        len_subtree+=l
    node.metadata.extend(tree_list[start+len_subtree:start+len_subtree+num_metadata])
    len_subtree+=num_metadata
    return len_subtree, node


with open('08.txt') as file:
    data = list(map(int, file.read().split()))

tree_size, tree = build_tree(data)
assert tree_size==len(data)  # The tree is the right size
assert tree.validate()  # The number of children and metadata entries are right
assert tree.collapse()==data  # Check that the tree collapses back to the input
print('Part 1:',tree.sum_metadata())
print('Part 2:',tree.value())
