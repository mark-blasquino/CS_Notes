"""
    1
   / \
  2  5
 / \
3  4

Output: ["1->2->3", "1->2->4", "1->5"]

    1
   /
  2
 /
3
Output: ["1->2->3"]

1
Output: ["1"]

Plan
Recursively go through all paths down to leaves, 
while keeping track of the current path you're on
Once you hit a leaf, then you append the path 
that you took to the resulting array

Runtime: O(number of nodes in tree)
Space: O(height of tree)
"""
def treePaths(t):
    if t == None:
        return []
    res = []
    currPath = ""
    treePathsHelper(t, res, currPath)
    return res

def treePathsHelper(root, res, currPath):
    currPath += f"{root.value}"
    if root.left == None and root.right == None:
        res.append(currPath)
        return
    if root.left != None:
        newPath = currPath + "->"
        treePathsHelper(root.left, res, newPath)
    if root.right != None:
        newPath = currPath + "->"
        treePathsHelper(root.right, res, newPath)