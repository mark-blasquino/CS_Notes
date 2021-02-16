# Depth-First Traversal Iterative Pseudocode
"""
procedure DFT_iterative(G, v) is
    let S be a stack
    S.push(v)
    while S is not empty do
        v = S.pop()
        if v is not labeled as discovered then
            label v as discovered
            for all edges from v to w in G.adjacentEdges(v) do
                S.push(w)
"""
from collections import deque

adjList = {
    1: {2, 3},
    2: {4},
    3: {4},
    4: {1}
}

startingNode = 1
def dftIterative(startingNode, graph):
    stack = deque()
    stack.append(startingNode)
    visited = set()

    while len(stack) > 0:
        currNode = stack.pop()
        if not currNode in visited:
            visited.add(currNode)
            print(currNode)
            for neighbor in graph[currNode]:
                stack.append(neighbor)

dftIterative(startingNode, adjList)