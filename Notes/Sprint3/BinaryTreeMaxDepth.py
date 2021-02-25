""" 
You are given a binary tree.

Write a function that can find the **maximum depth** of a binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.

Example:

Given the following binary tree

    5
   / \
  12  32
     /  \
    8    4

your function should return the depth = 3.
"""
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def maxDepth(self):
        # Your code here
        # if no left or right
        left_height = 0
        right_height = 0

        if self.right:
            right_height = self.right.maxDepth()

        if self.left:
            left_height = self.left.maxDepth()

        largest_height = max(right_height, left_height)

        return 1 + largest_height