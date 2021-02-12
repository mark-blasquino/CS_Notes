"""
You are given a binary tree and you need to write a function that can determine if it is height-balanced.

A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node differ in height by a maximum of 1.

"""
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def get_height(root):
    if root is  None:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))

def balancedBinaryTree(root):
    if root is None:
        return True
    return balancedBinaryTree(root.right) and balancedBinaryTree(root.left) and abs(get_height(root.left) - get_height(root.right)) <= 1
    