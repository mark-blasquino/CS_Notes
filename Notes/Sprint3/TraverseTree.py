"""
Understand
     1
   /   \
  2     4
   \   /
    3 5
output: [1,2,4,3,5]

Plan
This is just simple level-order traversal

Runtime: O(n)
Space:(max number of nodes in last level of perfect binary tree)
"""
def traverseTree(t):
    if t == None:
        return []
    queue = deque()
    queue.append(t)
    res = []
    while len(queue) > 0:
        curr = queue.popleft()
        res.append(curr.value)
        if curr.left != None:
            queue.append(curr.left)
        if curr.right != None:
            queue.append(curr.right)
    return res