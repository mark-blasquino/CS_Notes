# pseudocode 
# Breadth-First Search
"""
procedure BFS(G, root) is
    let Q be a queue
    label root as discovered
    Q.enqueue(root)
    while Q is not empty do
        v := Q.dequeue()
        if v is the goal then
            return v
        for all edges from v to w in G.adjacentEdges(v) do
            if w is not labeled as discovered then
                label w as discovered
                w.parent := v
                Q.enqueue(w)
"""

from collections import deque

adjList = {
    1: {2, 3},
    2: {4},
    3: {4},
    4: {1}
}

def bfs(graph, startingNode, destinationNode):
    queue = deque()
    visited = set()
    visited.add(startingNode)
    queue.append(startingNode)
    while len(queue) > 0:
        currNode = queue.popleft()
        print(f"visiting node {currNode}")
        if currNode == destinationNode:
            print(f"found dthe destination node {currNode}")
            return currNode
        for neighbor in graph[currNode]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

bfs(adjList, 1, 4)