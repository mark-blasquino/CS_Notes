"""
You are given a binary tree.

Write a function that can return the inorder traversal of node values.

Example:
Input:

   3
    \
     1
    /
   5

Output: [3,5,1]
"""
# Definition for a binary tree node.
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            # the new value, must go left
            if self.left is None:
                # create a new node as a left child of current node
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        else:
            # the value must go right    
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # let the right hand Node figure it out
                self.right.insert(value)


def inorder_traversal(root):
    # Your code here
    our_array = []
    # Recursively? 
    def recursive_traverse(current_node):
        # in-order
        if current_node.left:
            recursive_traverse(current_node.left)

        our_array.append(current_node.value)

        if current_node.right:
            recursive_traverse(current_node.right)

    recursive_traverse(root)
    return our_array
    

root = BSTNode(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(12)
root.insert(11)
root.insert(9)

print(inorder_traversal(root))