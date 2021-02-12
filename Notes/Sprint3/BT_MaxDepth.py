"""
Given the root of a binary tree, return its maximum depth

A binary tree's maximum depth is the number of nodes along the longest path from the 
root node down to the farthest leaf node

Input: root = [3,9,20,null,null,15,7]
"""

# Definition for a binary tree node:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Understand
    Plan
    Keep track of max depth found
    Use DFS (Depth First) /BFS (Breadth First) to go down the farthest leaf and keep updating max depth found
    """
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.maxDepth = 0
        self.maxDepthHelper(root, 1)
        return self.maxDepth
    
    def maxDepthHelper(root, currDepth):
        if root.left == None and root.right == None: # this is a leaf
            if currDepth > self.maxDepth:
                self.maxDepth = currDepth
            return

        self.maxDepthHelper(root.left, currDepth + 1)
        self.maxDepthHelper(root.right, currDepth + 1)

### other solution ###

# class TreeNode:
#    def __init__(self, data, left = None, right = None):
#       self.data = data
#       self.left = left
#       self.right = right
# def insert(temp,data):
#    que = []
#    que.append(temp)
#    while (len(que)):
#       temp = que[0]
#       que.pop(0)
#       if (not temp.left):
#          if data is not None:
#             temp.left = TreeNode(data)
#          else:
#             temp.left = TreeNode(0)
#          break
#       else:
#          que.append(temp.left)
#       if (not temp.right):
#          if data is not None:
#             temp.right = TreeNode(data)
#          else:
#             temp.right = TreeNode(0)
#          break
#       else:
#          que.append(temp.right)
# def make_tree(elements):
#    Tree = TreeNode(elements[0])
#    for element in elements[1:]:
#       insert(Tree, element)
#    return Tree
# class Solution(object):
#    def maxDepth(self, root):
#       """
#       :type root: TreeNode
#       :rtype: int
#       """
#       return self.solve(root)
#    def solve(self,root,depth = 0):
#       if root == None:
#          return depth
#       return max(self.solve(root.left,depth+1),self.solve(root.right,depth+1))
# tree1 = make_tree([1,2,2,3,4,None,3])
# ob1 = Solution()
# print(ob1.maxDepth(tree1))