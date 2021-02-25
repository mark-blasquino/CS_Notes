"""
You are given a binary tree. Write a function that returns the binary tree's node values using an in-order traversal.

Example:
Input: [2,None,3,4]

   2
    \
     3
    /
   4
Output: [2,4,3]

[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] array.integer

[Python 3] Syntax Tips
"""

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def binaryTreeInOrderTraversal(root):
    res = []
    if root:
        res = binaryTreeInOrderTraversal(root.left)
        res.append(root.value)
        res = res + binaryTreeInOrderTraversal(root.right)
    return res 

# Other solution:
def binaryTreeInOrderTraversal(root):
    arr = []
    def recursiveTraversal(curr):
        
        if curr.left is not None:
            recursiveTraversal(curr.left)

        arr.append(curr.value)

        if curr.right is not None:
            recursiveTraversal(curr.right)
    
    recursiveTraversal(root)
    return arr