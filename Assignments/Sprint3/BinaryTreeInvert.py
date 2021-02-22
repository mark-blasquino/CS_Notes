""" 
Given a binary tree, write a function that inverts the tree.
"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

# Using Recursion
# Perform a pre-order algorithm(root->left->right)
# Starting at the root, we invert the subtrees with root.left and root.right, and continue doing for the rest of the subtrees

def csBinaryTreeInvert(root):
    if root:
        root.left, root.right = csBinaryTreeInvert(root.right), csBinaryTreeInvert(root.left)
        return root