adjList = {
    1: {2, 3},
    2: {4},
    3: {4},
    4: {1}
}

from collections import deque

def dfs(graph, startingNode, destinationNode):
    stack = deque()
    visited = set()
    visited.add(startingNode)
    stack.append(startingNode)
    while len(stack) > 0:
        currNode = stack.pop()
        print(f"visiting node {currNode}")
        if currNode == destinationNode:
            print(f"found the destination node {currNode}")
            return currNode
        for neighbor in graph[currNode]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

dfs(adjList, 1, 4)