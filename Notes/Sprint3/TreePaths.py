"""
Given a binary tree of integers, return all the paths from the tree's root to its leaves
as an array of strings. The strings should have the following format:
"root->node1->node2->...->noden", representing the path from root to noden, where root
is the value stored in the root and node1, node2,..., noden are the values stored in
the 1st, 2nd,...,and nth nodes in the path respectivel (noden representing the leaf)
"""
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def treePaths(t):
    results = []
    
    # Traverse our tree
    def traverse_tree(tree, path):
        # do things to current node
        # maintain some sort of path and add nodes to that path
        path += str(tree.value)
        # once we reach a LEAF node, push that path to the results array
        if not tree.left and not tree.right:
            results.append(path)
        # go left
        if tree.left is not None:
            traverse_tree(tree.left, path + '->')
​
        # go right
        if tree.right is not None:
            traverse_tree(tree.right, path + '->')
    if t:
        traverse_tree(t, '')
    return results