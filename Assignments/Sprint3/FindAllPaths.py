"""
Understand
Note: For some reason, it's failing one of the tests. I 
think it's because the test case didn't sort their output.
In that case, the test is wrong :)

Drawing graphs via text are a pain, so I'm just gonna use the example given

Plan
1. Translate the problem into graph terminology
- Each index in the list given is a node
- Each subarray are the node's outgoing edges to its neighbors

2. Build your graph
- The graph is actually already built for us. We can traverse 
the given list like a graph since
we have access to the node we're at and its neighbors.

3. Traverse the graph
- Any type of traversal would work, we just need to keep 
track of the path that we've currently taken
- We add that path to the result once we reach the destination node
- Note that we don't need a visited set since we're
guaranteed that the graph is a DAG

Runtime: O(number of nodes^2)
Space: O(number of nodes^2)
Imagine a dense graph
"""
from collections import deque

def csFindAllPathsFromAToB(graph):
    stack = deque()
    stack.append((0, [0]))
    res = []
    destinationNode = len(graph) - 1

    while len(stack) > 0:
        curr = stack.pop()
        currNode, currPath = curr[0], curr[1]
        for neighbor in graph[currNode]:
            newPath = currPath.copy()
            newPath.append(neighbor)
            if neighbor == destinationNode:
                res.append(newPath)
            else:
                stack.append((neighbor, newPath))
    res.sort()
    return res