"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST)

A valid BST is defined as follows:
    - the left subtree of a node contains only nodes with keys < the node's key
    - the right subtree of a node contains only nodes with keys > thhe node's key
    - both the left and right subtrees must also be binary search trees
"""

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:


### other solution ###
"""
To solve this, we will follow these steps –

Create one recursive function called solve(), this will take root, min and max, the method will be like
if root is null, then return true
if value of root <= min or value of root >= max, then return false
return the (solve(left of root, min, root value) AND solve(right of root, root value, max))
call the solve() method initially, by passing root, and – inf as min and inf as max.
"""

def insert(temp, val):
    que = []
    que.append(temp)
    while (len(que)):
        temp = que[0]
        que.pop(0)
        if (not temp.left):
            if val is not None:
                temp.left = TreeNode(val)
            else:
                temp.left = TreeNode(0)
            break
        else:
            que.append(temp.left)
        if (not temp.right):
            if val is not None:
                temp.right = TreeNode(val)
            else:
                temp.right = TreeNode(0)
            break
        else:
            que.append(temp.right)
            
def make_tree(elements):
    Tree = TreeNode(elements[0])
    for element in elements[1:]:
        insert(Tree, element)
    return Tree


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.solve(root, -1000000000000000000000,1000000000000000000000)
    def solve(self, root, min_val, max_val):
        if root == None or root.val == 0:
            return True
        if (root.val <= min_val or root.val >= max_val):
            return False
        return self.solve(root.left, min_val, root.val) and self.solve(root.right, root.val, max_val)
ob1 = Solution()
tree = make_tree([3,1,4,None,2,None,5])
print(ob1.isValidBST(tree))
tree = make_tree([5,1,4,None,None,3,6])
print(ob1.isValidBST(tree))