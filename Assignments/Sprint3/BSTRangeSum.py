""" 
You are given the root node of a binary search tree (BST).

You need to write a function that returns the sum of values of all the nodes with a value between lower and upper (inclusive).

The BST is guaranteed to have unique values.
"""


# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBSTRangeSum(root, lower, upper):
    res =  0
    stack = [root]
    while(len(stack) > 0):
        c_node = stack.pop()
        if(c_node.value <= upper and c_node.value >= lower):
            res += c_node.value
        
        if(c_node.left != None):
            if(c_node.value >= lower):
                stack.append(c_node.left)
        
        if(c_node.right != None):
            if(c_node.value <= upper):
                stack.append(c_node.right)
    
    return res