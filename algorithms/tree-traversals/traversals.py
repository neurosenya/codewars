# Pre-order traversal
# Starting from the root go around the tree counterclockwise.
# Print each node when you pass its left side

def traverse(tree):
    if tree:
        print(tree.getRootVal())
        traverse(tree.getLeftChild())
        traverse(tree.getRightChild())

"""
In-order traversal
Starting from the root, go around the tree counterclockwise. Print each node
when you pass its bottom side
"""
def traverse(tree):
    if tree:
        traverse(tree.getLeftChild())
        print(tree.getRootVal())
        traverse(tree.getRightChild())

"""
Post-otder traversal
Starting from the root, go around the tree counteclockwise.
Print each node when you pass its right side.
"""
def traverse(tree):
    if tree:
        traverse(tree.getLeftChild())
        traverse(tree.getRightChild())
        print(tree.getRootVal())

