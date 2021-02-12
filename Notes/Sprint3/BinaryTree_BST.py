"""
Binary Tree Inorder Reversal

Given the root of a binary tree, return the inorder traversal of its nodes' values

Examples:
Input: root = [1, null, 2, 3]
Output: [1,3,2]

Plan
- Use recursion to go to the left subtree first
then process the current node,
then use recursion again to the right subtree next

When building a recursive function:
base case, recursive case
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = [] # resulting array, append values to this array
        if root != None:
            inorderTraversalHelper(root, res)
            #traverse
        return res # if not None
    # helper method -- 
    def inorderTraversalHelper(self, root, res): #recursive function
        if root == None: # base case
            return
        # go to left subtree first    
        if root.left != None:
            self.inorderTraversalHelper(root.left, res)
        # process current node
        res.append(root.val)
        # go to right subtree next
        if root.right != None:
            self.inorderTraversalHelper(root.right, res)

root = [1,'null',2,3]
Solution.inorderTraversal(root)


"""
Binary Tree Preorder Traversal


"""
 class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = [] # resulting array, append values to this array
        if root != None:
            inorderTraversalHelper(root, res)
            #traverse
        return res # if not None
    # helper method -- 
    def inorderTraversalHelper(self, root, res): #recursive function
        if root == None: # base case
            return

        # process current node
        res.append(root.val)

        # go to left subtree first    
        if root.left != None:
            self.inorderTraversalHelper(root.left, res)

        # go to right subtree next
        if root.right != None:
            self.inorderTraversalHelper(root.right, res)       




"""
Binary Tree Postorder Traversal


"""
 class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = [] # resulting array, append values to this array
        if root != None:
            inorderTraversalHelper(root, res)
            #traverse
        return res # if not None
    # helper method -- 
    def inorderTraversalHelper(self, root, res): #recursive function
        if root == None: # base case
            return
        # go to left subtree first    
        if root.left != None:
            self.inorderTraversalHelper(root.left, res)

        # go to right subtree next
        if root.right != None:
            self.inorderTraversalHelper(root.right, res)       

        # process current node
        res.append(root.val)